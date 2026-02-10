---
layout: default
title: "🚗 Veiculando — Plataforma de Gestão de Infraestrutura Viária"
---

# 🚗 Veiculando — Plataforma de Gestão de Infraestrutura Viária

**Papel:** Product Owner · Arquiteto de Software · Gestor de Projeto  
**Período:** 2023–2025  
**Stack:** Node.js (NestJS) · Angular · Docker · SQL Server · GitHub Actions · Azure · Jira  

---

## 🎯 Contexto

O **Veiculando** é um ecossistema de aplicações web e mobile voltado à **gestão inteligente de manutenção viária**, com foco em obras, pavimentação e operação urbana.  
O projeto nasceu de uma parceria público-privada para **automatizar o ciclo de vistoria, execução e monitoramento de vias** em diversos municípios.

## 📸 Galeria

> *Adicione aqui prints das telas principais, dashboards ou diagramas.*

| | |
|:-------------------------:|:-------------------------:|
| <img width="100%" src="https://placehold.co/600x400?text=App+Vistoria" alt="App Vistoria"> <br> App de Vistoria | <img width="100%" src="https://placehold.co/600x400?text=Dashboard+Obras" alt="Dashboard Obras"> <br> Monitoramento de Obras |
| <img width="100%" src="https://placehold.co/600x400?text=GitHub+Projects" alt="GitHub Projects"> <br> Gestão no GitHub Projects | <img width="100%" src="https://placehold.co/600x400?text=BPMN+Viário" alt="BPMN Viário"> <br> Processo de Manutenção |

---

---

## 💡 Desafios

- Orquestrar múltiplos repositórios privados e públicos sob uma mesma organização no GitHub.  
- Garantir rastreabilidade e governança de issues, PRs e milestones entre times distintos.  
- Integrar **frontend, backend, pipelines e deploys** sob práticas DevOps consistentes.  
- Criar um ambiente de colaboração que suportasse **gestão ágil + versionamento técnico + compliance**.

---

## ⚙️ Entregas Principais

### 🔁 DevOps & Automação
- Configuração completa de **GitHub Actions** com:
  - Auto-add de issues a Projects v2.  
  - Transição automática de status (`New → Backlog → Sprint → QA → Done`).  
  - Sincronização de labels e milestones entre repositórios.  
  - Fechamento automático de issues ao fazer merge do PR.
- Criação de **PATs organizacionais** e workflows reutilizáveis via `.github` central.  
- Setup de **branch protection**, CODEOWNERS e PR templates padronizados.  

### 🧱 Arquitetura e Engenharia
- Stack unificada **Node/NestJS + Angular/Ionic**, com autenticação JWT e endpoints REST.  
- Configuração de **Docker Compose** para ambientes locais e CI/CD na Azure.  
- Modelagem de dados em SQL Server com versionamento de scripts e migrations.  
- Pipeline de build e deploy automatizado (homolog → produção).  

### 🧭 Produto & Gestão
- Estruturação do **roadmap e backlog** via GitHub Projects v2, com métricas de throughput e cycle time.  
- Refinamento de **user stories e critérios de aceite BDD**.  
- Facilitação de cerimônias Scrum (planning, review e retros).  
- Dashboard de progresso integrado ao Notion com status e velocity.  

---

## 📈 Resultados

- Redução de 40% no tempo médio de integração entre backend e frontend.  
- Adoção total do GitHub Projects como ferramenta de gestão — eliminando planilhas e duplicidade de tarefas.  
- Deploy contínuo estável em Azure com rollback automatizado.  
- Maior visibilidade executiva sobre andamento das sprints e releases.  

---

## 🧭 Artefatos e Referências

| Tipo | Descrição | Link / Local |
|------|------------|---------------|
| **BPMN** | Fluxo de manutenção viária e ciclo de vistoria | `/assets/veiculando-bpmn.png` |
| **PRD** | Documento de requisitos e arquitetura | `/docs/veiculando-PRD.md` |
| **Workflows YAML** | Automação multi-repo e integração com Projects | `/workflows/*.yml` |
| **Dashboard de Projeto** | Roadmap com status e velocity | Notion / GitHub Projects |

---

## 🧰 Aprendizados

- A importância de equilibrar **autonomia técnica e governança** em setups multi-repo.  
- O valor de **documentar processos DevOps como produto**, não apenas infraestrutura.  
- Como **automatizações simples (YAML + PATs)** podem liberar o time para focar em valor de negócio.  

---

📎 [Voltar ao Portfólio Principal](../../)
