<div align="center">

# 👋 Hi, I'm Rahul Poddar

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=22&pause=1200&color=2EA44F&center=true&vCenter=true&width=650&lines=Cloud+%26+DevOps+Engineer;AWS+%7C+Azure+%7C+Terraform+%7C+Kubernetes;CI%2FCD+%7C+Docker+%7C+GitOps+%7C+Monitoring;Building+reliable%2C+automated+infrastructure" alt="Typing SVG" />
</a>

<p>
  <a href="https://www.linkedin.com/in/rahulpoddar-2eab5">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="https://github.com/rahulpoddarcse2">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <a href="mailto:rahulpoddarcse2@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  <a href="https://www.linkedin.com/in/rahulpoddar-2eab5">
    <img src="https://img.shields.io/badge/Open_to_Work-2EA44F?style=for-the-badge&logoColor=white" alt="Open to Work"/>
  </a>
</p>

<img src="https://komarev.com/ghpvc/?username=rahulpoddarcse2&style=flat-square&color=0e75b6" alt="Profile Views"/>

</div>

---

## 👨‍💻 About Me

```yaml
name: Rahul Poddar
location: India
role: Cloud & DevOps Engineer

education:
  degree: BCA
  specialization: Cloud Data Engineering & DevOps

cloud:
  - AWS
  - Microsoft Azure

currently_learning:
  - Kubernetes & Helm
  - GitHub Actions & GitOps
  - Advanced Terraform
  - DevSecOps

availability:
  - Full-time opportunities
  - Immediate joiner
```

I work on **cloud infrastructure, automation, and deployment pipelines** —
turning "it works on my machine" into something reproducible, monitored,
and safe to hand off to a team.

```text
Code → Build → Test → Containerize → Deploy → Monitor → Improve
```

---

## 🛠️ Technical Skills

<p align="center">

**Cloud & Infrastructure**
<br/>
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS"/>
<img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="Azure"/>
<img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform"/>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux"/>

<br/><br/>

**CI/CD & GitOps**
<br/>
<img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white" alt="Jenkins"/>
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/Azure_DevOps-0078D7?style=for-the-badge&logo=azuredevops&logoColor=white" alt="Azure DevOps"/>
<img src="https://img.shields.io/badge/ArgoCD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white" alt="ArgoCD"/>

<br/><br/>

**Containers & Orchestration**
<br/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes"/>
<img src="https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white" alt="Helm"/>
<img src="https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Compose"/>

<br/><br/>

**Monitoring & Observability**
<br/>
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus"/>
<img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana"/>
<img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx"/>

<br/><br/>

**Programming & Scripting**
<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash"/>
<img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL"/>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>

</p>

---

## 🚀 Featured Projects

<details open>
<summary><b>☁️ Automated Preview Environments — Terraform + GitHub Actions</b> (AWS & Azure)</summary>
<br/>

**Terraform · GitHub Actions · AWS · Azure · Docker**

<a href="https://github.com/rahulpoddarcse2/automated-preview-environments">
<img src="https://img.shields.io/badge/View_Project-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repository"/>
</a>

Every open pull request gets its own live, disposable cloud environment —
created automatically when the PR opens, destroyed automatically when it's
merged or closed.

**Key Features**
- Parameterized Terraform modules for AWS and Azure, sharing one interface
- S3 remote state with DynamoDB locking, one state file per PR
- GitHub Actions workflows for create (`opened`/`synchronize`) and destroy (`closed`)
- Bot comment on the PR with the live preview URL

```text
PR opened → build image → terraform apply → comment preview URL
PR merged/closed → terraform destroy → comment "environment destroyed"
```

</details>

<details>
<summary><b>☸️ CI/CD Integration — Microservices on Kubernetes</b></summary>
<br/>

**Jenkins · Docker · Kubernetes · ArgoCD · Prometheus · Grafana**

<a href="https://github.com/rahulpoddarcse2/cicd-app-repo">
<img src="https://img.shields.io/badge/View_Project-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repository"/>
</a>

A three-tier microservices application deployed on Kubernetes through a
complete CI/CD + GitOps workflow.

**Key Features**
- Two-repository GitOps architecture (app repo + GitOps repo)
- Jenkins CI pipeline with automated Docker builds and pushes
- ArgoCD-based continuous deployment with self-healing sync
- Prometheus & Grafana monitoring

```text
Developer → GitHub → Jenkins CI → Docker Image → GitOps Repo
    → ArgoCD → Kubernetes → Services/Pods → Prometheus → Grafana
```

**Repositories:** [Application](https://github.com/rahulpoddarcse2/cicd-app-repo) · [GitOps](https://github.com/rahulpoddarcse2/cicd-gitops-repo)

</details>

<details>
<summary><b>🌦️ Weather Alert Service</b></summary>
<br/>

**Flask · PostgreSQL · Docker · Nginx · GitHub Actions**

<a href="https://github.com/rahulpoddarcse2/weather-alert-service">
<img src="https://img.shields.io/badge/View_Project-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repository"/>
</a>

Containerized weather-alerting platform with automated CI/CD.

**Key Features**
- Flask backend with background weather polling and email alerts
- Multi-stage, non-root Docker builds with container health checks
- Nginx reverse proxy in front of the app
- GitHub Actions pipeline: test → build → push → deploy

</details>

<details>
<summary><b>🐳 Task Manager — Docker Production Stack</b></summary>
<br/>

**React · Node.js · PostgreSQL · Nginx · Docker**

<a href="https://github.com/rahulpoddarcse2/task-manager-docker">
<img src="https://img.shields.io/badge/View_Project-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repository"/>
</a>

Production-oriented three-tier containerized application, orchestrated
with Docker Compose.

**Key Features**
- React frontend + Node.js REST API + PostgreSQL, each in its own container
- Nginx reverse proxy, health checks, persistent volumes
- Internal container networking, no ports exposed beyond what's needed

```text
Nginx → React (static) 
      → Node.js API → PostgreSQL
```

</details>

<details>
<summary><b>📊 E-Commerce Executive Dashboard</b></summary>
<br/>

**Python · Pandas · Scikit-learn · Power BI**

<a href="https://github.com/rahulpoddarcse2/ecommerce-executive-dashboard">
<img src="https://img.shields.io/badge/View_Project-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repository"/>
</a>

End-to-end BI project combining a Python ETL pipeline, customer
segmentation, and a Power BI dashboard for business-facing insights.

**Key Features**
- Python ETL: cleaning, transformation, feature engineering
- Customer Lifetime Value analysis + K-Means segmentation
- Star-schema data model feeding a Power BI dashboard

</details>

---

## 🏆 Certifications & Learning

| Technology    | Focus                          | Status      |
| ------------- | ------------------------------- | ----------- |
| ☁️ AWS        | Cloud Practitioner Concepts     | 🔄 Learning |
| 🐳 Docker     | Production Docker & Compose     | ✅ Completed |
| ☸️ Kubernetes | Kubernetes & Helm Fundamentals  | 🔄 Learning |
| ⚙️ Terraform  | IaC & AWS Provisioning          | 🔄 Learning |
| 📊 Power BI   | Data Modeling & DAX             | ✅ Completed |

---

## 📈 GitHub Statistics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=rahulpoddarcse2&show_icons=true&hide_border=true&count_private=true&theme=tokyonight&cache_seconds=1800" alt="Rahul's GitHub Stats" height="165"/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=rahulpoddarcse2&layout=compact&theme=tokyonight&hide_border=true&langs_count=8&cache_seconds=1800" alt="Top Languages" height="165"/>

<br/><br/>

<img src="https://streak-stats.demolab.com/?user=rahulpoddarcse2&theme=tokyonight&hide_border=true" alt="GitHub Streak"/>

</div>

---

## 🏆 GitHub Profile Trophy

<div align="center">

<img src="https://github-profile-trophy.vercel.app/?username=rahulpoddarcse2&theme=tokyonight&no-frame=true&no-bg=true&column=-1&margin-w=12" alt="GitHub Trophies"/>

</div>

---

## 📊 GitHub Activity

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=rahulpoddarcse2&theme=tokyo-night&hide_border=true" alt="GitHub Activity Graph"/>

</div>

---

## 📫 Let's Connect

<div align="center">

### 💼 Open to Cloud & DevOps opportunities

**Cloud Infrastructure • DevOps • CI/CD • Kubernetes • Terraform • Cloud Automation**

📍 India&nbsp;&nbsp;|&nbsp;&nbsp;🌐 Open to Remote

<br/>

<a href="https://www.linkedin.com/in/rahulpoddar-2eab5">
<img src="https://img.shields.io/badge/Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
<a href="mailto:rahulpoddarcse2@gmail.com">
<img src="https://img.shields.io/badge/Send_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
</a>

<br/><br/>

*"Automate. Deploy. Monitor. Improve."*

</div>
