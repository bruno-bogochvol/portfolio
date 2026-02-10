---
layout: default
title: "🚗 Veiculando — Road Infrastructure Management Platform"
---

# 🚗 Veiculando — Road Infrastructure Management Platform

**Role:** Product Owner · Software Architect · Project Manager  
**Timeline:** 2023–2025  
**Stack:** Node.js (NestJS) · Angular · Docker · SQL Server · GitHub Actions · Azure · Jira

---

## 🎯 Context

Veiculando is a web and mobile ecosystem dedicated to **intelligent road maintenance management**, covering construction, paving, and urban operations.  
The initiative emerged from a public-private partnership to **automate the inspection, execution, and monitoring cycle for roads** across multiple municipalities.

## 📸 Gallery

> *Add screenshots of main screens, dashboards, or diagrams here.*

| | |
|:-------------------------:|:-------------------------:|
| <img width="100%" src="https://placehold.co/600x400?text=Inspection+App" alt="Inspection App"> <br> Inspection App | <img width="100%" src="https://placehold.co/600x400?text=Roadwork+Dash" alt="Roadwork Dash"> <br> Roadwork Monitoring |
| <img width="100%" src="https://placehold.co/600x400?text=Project+Mgmt" alt="Project Mgmt"> <br> GitHub Projects v2 | <img width="100%" src="https://placehold.co/600x400?text=Maintenance+BPMN" alt="Maintenance BPMN"> <br> Maintenance Workflow |

---

---

## 💡 Challenges

- Orchestrate multiple private and public repositories under a single GitHub organization.  
- Ensure traceability and governance of issues, PRs, and milestones across distinct teams.  
- Integrate **frontend, backend, pipelines, and deployments** within consistent DevOps practices.  
- Build a collaboration environment that supported **agile management + technical versioning + compliance**.

---

## ⚙️ Key Deliverables

### 🔁 DevOps & Automation
- Full **GitHub Actions** setup with:
  - Automatic issue intake into Projects v2.  
  - Automated status transitions (`New → Backlog → Sprint → QA → Done`).  
  - Synchronized labels and milestones across repositories.  
  - Automatic issue closure when merging the PR.
- Creation of organizational **PATs** and reusable workflows via a central `.github` repository.  
- Branch protection, CODEOWNERS, and standardized PR templates.

### 🧱 Architecture & Engineering
- Unified **Node/NestJS + Angular/Ionic** stack with JWT authentication and REST endpoints.  
- **Docker Compose** configuration for local environments and CI/CD on Azure.  
- SQL Server data modeling with versioned scripts and migrations.  
- Automated build and deploy pipeline (staging → production).

### 🧭 Product & Delivery
- Structured **roadmap and backlog** within GitHub Projects v2, tracking throughput and cycle time.  
- Refinement of **user stories and BDD acceptance criteria**.  
- Facilitation of Scrum ceremonies (planning, review, and retrospectives).  
- Project dashboard integrated with Notion, consolidating status and velocity metrics.

---

## 📈 Results

- 40% reduction in average integration time between backend and frontend.  
- Full adoption of GitHub Projects as the governance tool—eliminating spreadsheets and task duplication.  
- Stable continuous deployment on Azure with automated rollback.  
- Greater executive visibility into sprint and release progress.

---

## 🧾 Artifacts & References

| Type | Description | Link / Location |
|------|------------|---------------|
| **BPMN** | Road maintenance and inspection cycle flow | `/assets/veiculando-bpmn.png` |
| **PRD** | Requirements and architecture documentation | `/docs/veiculando-PRD.md` |
| **Workflow YAML** | Multi-repository automation and Projects integration | `/workflows/*.yml` |
| **Project Dashboard** | Roadmap with status and velocity | Notion / GitHub Projects |

---

## 🧰 Lessons Learned

- The importance of balancing **technical autonomy and governance** in multi-repo setups.  
- The value of **treating DevOps processes as product**, not just infrastructure.  
- How **lightweight automations (YAML + PATs)** free the team to focus on business outcomes.

---

📎 [Back to Main Portfolio](../../README_EN.html)
