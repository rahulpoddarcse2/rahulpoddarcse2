"""Generate assets/stats-dashboard.svg from live GitHub data (GraphQL)."""
import json, os, sys, urllib.request
from datetime import date, datetime, timezone

LOGIN = os.environ.get("GH_LOGIN", "rahulpoddarcse2")
TOKEN = os.environ["GITHUB_TOKEN"]
OUT = os.environ.get("OUT", "assets/stats-dashboard.svg")
FONT = "'Segoe UI',Helvetica,Arial,sans-serif"

QUERY = """
query($login:String!){ user(login:$login){
  createdAt
  repositories(ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC, first:100){
    totalCount
    nodes{ languages(first:8, orderBy:{field:SIZE, direction:DESC}){ edges{ size node{ name color } } } }
  }
  contributionsCollection{
    totalCommitContributions
    contributionCalendar{ totalContributions weeks{ contributionDays{ date contributionCount } } }
  }
}}"""

req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
    headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json", "User-Agent": "profile-stats"},
)
data = json.load(urllib.request.urlopen(req))
if "errors" in data:
    sys.exit(f"GraphQL error: {data['errors']}")
u = data["data"]["user"]
cc = u["contributionsCollection"]
cal = cc["contributionCalendar"]
days = sorted((d for w in cal["weeks"] for d in w["contributionDays"]), key=lambda d: d["date"])
today = date.today().isoformat()
days = [d for d in days if d["date"] <= today]

# streaks
longest = run = 0
for d in days:
    run = run + 1 if d["contributionCount"] > 0 else 0
    longest = max(longest, run)
cur, seq = 0, days[:]
if seq and seq[-1]["contributionCount"] == 0:
    seq = seq[:-1]
for d in reversed(seq):
    if d["contributionCount"] > 0: cur += 1
    else: break
active = sum(1 for d in days if d["contributionCount"] > 0)

# monthly totals (last 12 calendar months present in data)
months = {}
for d in days:
    months[d["date"][:7]] = months.get(d["date"][:7], 0) + d["contributionCount"]
created = u["createdAt"][:7]
mkeys = [k for k in sorted(months)[-12:] if k >= created]
mvals = [months[k] for k in mkeys]
mlabels = [datetime.strptime(k, "%Y-%m").strftime("%b") for k in mkeys]

# languages
langs = {}
for repo in u["repositories"]["nodes"]:
    for e in repo["languages"]["edges"]:
        n = e["node"]
        l = langs.setdefault(n["name"], {"size": 0, "color": n["color"] or "#8b949e"})
        l["size"] += e["size"]
total = sum(l["size"] for l in langs.values()) or 1
ranked = sorted(langs.items(), key=lambda kv: -kv[1]["size"])
top = ranked[:4]
rest = sum(v["size"] for _, v in ranked[4:])
lang_rows = [(n, v["size"] / total * 100, v["color"]) for n, v in top]
if rest > 0:
    lang_rows.append(("Other", rest / total * 100, "#6e7681"))

kpis = [
    (f'{cal["totalContributions"]:,}', "CONTRIBUTIONS", "#2ea44f"),
    (f'{cc["totalCommitContributions"]:,}', "COMMITS", "#38bdf8"),
    (f'{u["repositories"]["totalCount"]}', "PUBLIC REPOS", "#a78bfa"),
    (f"{active}", "ACTIVE DAYS", "#f0883e"),
    (f"{cur}", "CURRENT STREAK", "#f2c811"),
    (f"{longest}", "LONGEST STREAK", "#3fb950"),
]

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;")
W, PAD = 1000, 24
tw, gap = 148, 12
parts = []

parts.append(f'<text x="{PAD+4}" y="40" font-family="{FONT}" font-size="20" font-weight="700" fill="#f0f6fc">GitHub Overview</text>')
span = "LAST 12 MONTHS" if len(sorted(months)) >= 12 and sorted(months)[-12] >= created else "SINCE " + datetime.strptime(created, "%Y-%m").strftime("%b %Y").upper()
parts.append(f'<text x="{W-PAD-4}" y="38" text-anchor="end" font-family="{FONT}" font-size="11.5" letter-spacing="1.5" fill="#7d8590">{span} · UPDATED {datetime.now(timezone.utc).strftime("%d %b %Y").upper()}</text>')

for i, (num, lab, col) in enumerate(kpis):
    x = PAD + i * (tw + gap)
    parts.append(f'''<g>
  <rect x="{x}" y="64" width="{tw}" height="84" rx="10" fill="#0d1117" stroke="#30363d"/>
  <rect x="{x+14}" y="64" width="{tw-28}" height="3" rx="1.5" fill="{col}"/>
  <text x="{x+16}" y="108" font-family="{FONT}" font-size="28" font-weight="700" fill="#f0f6fc">{num}</text>
  <text x="{x+16}" y="131" font-family="{FONT}" font-size="10.5" letter-spacing="1.5" fill="#8b949e">{lab}</text>
</g>''')

# left panel: monthly bars
parts.append(f'<rect x="{PAD}" y="168" width="584" height="240" rx="10" fill="#0d1117" stroke="#30363d"/>')
parts.append(f'<text x="{PAD+20}" y="196" font-family="{FONT}" font-size="11" letter-spacing="2" fill="#7d8590">CONTRIBUTIONS PER MONTH</text>')
cx0, cw, base, maxh = PAD + 20, 544, 372, 132
slot = cw / max(len(mvals), 1)
mx = max(mvals) if mvals and max(mvals) > 0 else 1
for i, (v, lab) in enumerate(zip(mvals, mlabels)):
    h = max(3, round(v / mx * maxh)) if v > 0 else 3
    barw = min(48, int(slot * 0.58))
    bx = cx0 + i * slot + (slot - barw) / 2
    col = "url(#bar)" if v > 0 else "#21262d"
    parts.append(f'''<rect x="{bx:.1f}" y="{base-h}" width="{barw}" height="{h}" rx="5" fill="{col}">
    <animate attributeName="height" from="0" to="{h}" dur="0.9s" begin="0s" fill="freeze"/>
    <animate attributeName="y" from="{base}" to="{base-h}" dur="0.9s" begin="0s" fill="freeze"/>
  </rect>''')
    if v > 0:
        parts.append(f'<text x="{bx+barw/2:.1f}" y="{base-h-8}" text-anchor="middle" font-family="{FONT}" font-size="11" font-weight="600" fill="#c9d1d9">{v}</text>')
    parts.append(f'<text x="{bx+barw/2:.1f}" y="392" text-anchor="middle" font-family="{FONT}" font-size="11" fill="#7d8590">{mlabels[i]}</text>')
parts.append(f'<line x1="{cx0}" y1="{base+4}" x2="{cx0+cw}" y2="{base+4}" stroke="#30363d"/>')

# right panel: languages
rx = 620
parts.append(f'<rect x="{rx}" y="168" width="356" height="240" rx="10" fill="#0d1117" stroke="#30363d"/>')
parts.append(f'<text x="{rx+20}" y="196" font-family="{FONT}" font-size="11" letter-spacing="2" fill="#7d8590">TOP LANGUAGES</text>')
bx0, bw = rx + 20, 316
parts.append(f'<clipPath id="lc"><rect x="{bx0}" y="212" width="{bw}" height="12" rx="6"><animate attributeName="width" from="0" to="{bw}" dur="1s" begin="0s" fill="freeze"/></rect></clipPath>')
xx, seg = bx0, []
for n, pct, col in lang_rows:
    w = bw * pct / sum(p for _, p, _ in lang_rows)
    seg.append(f'<rect x="{xx:.1f}" y="212" width="{w+0.5:.1f}" height="12" fill="{col}"/>')
    xx += w
parts.append(f'<g clip-path="url(#lc)"><rect x="{bx0}" y="212" width="{bw}" height="12" fill="#21262d"/>{"".join(seg)}</g>')
ry = 258
den = sum(p for _, p, _ in lang_rows)
for n, pct, col in lang_rows:
    parts.append(f'<circle cx="{rx+26}" cy="{ry-4}" r="5" fill="{col}"/>')
    parts.append(f'<text x="{rx+42}" y="{ry}" font-family="{FONT}" font-size="14" fill="#e6edf3">{esc(n)}</text>')
    parts.append(f'<text x="{rx+336}" y="{ry}" text-anchor="end" font-family="{FONT}" font-size="14" font-weight="600" fill="#8b949e">{pct/den*100:.1f}%</text>')
    ry += 30

H = 432
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="GitHub overview: {cal["totalContributions"]} contributions in the last year, {cc["totalCommitContributions"]} commits, {u["repositories"]["totalCount"]} public repositories, current streak {cur} days, longest streak {longest} days.">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="1" stop-color="#101a2c"/></linearGradient>
    <linearGradient id="bar" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#2ea44f"/><stop offset="1" stop-color="#38bdf8"/></linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="url(#bg)" stroke="#30363d"/>
  {chr(10).join(parts)}
</svg>'''
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(svg)
print("wrote", OUT, "| contributions:", cal["totalContributions"], "| streak:", cur, longest, "| langs:", [(n, round(p, 1)) for n, p, _ in lang_rows])
