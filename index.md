---
layout: default
title: "Bruno Bogochvol — Portfolio"
---

<link rel="stylesheet" href="{{ "/assets/css/style.css" | relative_url }}">

{% include language_switcher.html current='pt' %}

<section class="intro-section">
  <h1>Bruno Bogochvol</h1>
  <p class="fs-4 text-muted">Product Owner & Software Engineer</p>
  
  <p>
    Sou um profissional híbrido de <strong>negócio e tecnologia</strong>, com experiência em <strong>gestão de produto, arquitetura de software e metodologias ágeis</strong>.<br>
    Atuo na ponte entre <strong>discovery, UX e engenharia</strong>, conectando visão de produto à entrega técnica — sempre com foco em <strong>valor, automação e qualidade (BDD/TDD)</strong>.
  </p>

  <p>
    📍 São Paulo, BR <br>
    📧 <a href="mailto:brunobogochvol@gmail.com">brunobogochvol@gmail.com</a> <br>
    🔗 <a href="https://linkedin.com/in/brunobogochvol">LinkedIn</a> · <a href="{{ '/assets/pdf/cv-pt.pdf' | relative_url }}">CV em PDF</a>
  </p>
</section>

<hr>

<section>
  <h2>🧭 Sobre mim</h2>
  <p>
    Formado em <strong>Administração Pública pela FGV-EAESP</strong>, transicionei para <strong>Engenharia de Software</strong> e venho atuando como <strong>PO técnico e arquiteto de software</strong>, conduzindo squads em projetos web e mobile.<br>
    Tenho experiência multissetorial — <strong>ESG, GovTech, Educação, Saúde, Fintech e Sustentabilidade</strong> — e desenvolvo produtos com base em práticas ágeis, discovery contínuo e cultura DevOps.
  </p>
</section>

<section>
  <h2>⚙️ Stack e Práticas</h2>
  <ul>
    <li><strong>Tech:</strong> Node.js (NestJS) · Angular/Ionic · Docker · GitHub Actions · MongoDB/MySQL · Azure</li>
    <li><strong>Produto:</strong> PRDs · Roadmaps · Discovery · UX Flows · BPMN · Backlog Management (Jira, Projects v2)</li>
    <li><strong>Práticas:</strong> Scrum/Kanban · BDD/TDD · CI/CD · Design Thinking · OKRs</li>
  </ul>
</section>

<hr>

<section>
  <h2>💼 Casos de Produto</h2>
  <p>Alguns projetos foram conduzidos sob contrato PJ com a <strong>Code Tech</strong>, com informações adaptadas para preservar confidencialidade.</p>

  <div class="project-grid">
    {% for project in site.data.projects %}
    <div class="project-card">
      {% if project.image %}
      <img src="{{ project.image | relative_url }}" alt="{{ project.title }}" class="card-image">
      {% endif %}
      <div class="card-header">
        <h3 class="card-title">{{ project.title }}</h3>
        <span class="card-category">{{ project.category }}</span>
      </div>
      
      <div class="card-body">
        <p class="card-description">{{ project.description }}</p>
        
        <div class="card-meta">
          <div class="meta-item">
            <span class="meta-label">Papel:</span>
            <span class="meta-value">{{ project.role }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">Stack:</span>
            <span class="meta-value">{{ project.stack }}</span>
          </div>
        </div>
      </div>

      <div class="card-actions">
        {% if project.links.production %}
          <a href="{{ project.links.production }}" class="btn-sm" target="_blank">🌐 Online</a>
        {% endif %}
        
        {% if project.links.figma %}
          <a href="{{ project.links.figma }}" class="btn-sm" target="_blank">🎨 Design</a>
        {% endif %}

        {% if project.links.repo %}
          <a href="{{ project.links.repo }}" class="btn-sm" target="_blank">💻 Código</a>
        {% endif %}

        {% if project.links.case %}
          <a href="{{ project.links.case | relative_url }}" class="btn-sm btn-primary">📄 Ver Case</a>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>
</section>

<hr>

<section>
  <h2>🧰 Templates e Processos</h2>
  <p>Modelos e artefatos que uso no dia a dia como PO técnico.</p>
  <ul>
    <li><a href="{{ '/docs/template-PRD.md' | relative_url }}">📝 Template de PRD</a></li>
    <li><a href="{{ '/docs/template-BDD.md' | relative_url }}">🧪 Template de BDD</a></li>
    <li><a href="{{ '/docs/template-roadmap.md' | relative_url }}">🗺️ Template de Roadmap</a></li>
    <li><a href="{{ '/docs/template-BPMN.png' | relative_url }}">📊 Exemplo de BPMN</a></li>
  </ul>
</section>

<hr>

<section>
  <h2>🛠️ Contato</h2>
  <p>
    Aberto a oportunidades em <strong>gestão de produto técnico, arquitetura de software e inovação com IA aplicada</strong>.<br>
    📬 Fale comigo pelo <a href="https://linkedin.com/in/brunobogochvol">LinkedIn</a> ou e-mail: <a href="mailto:brunobogochvol@gmail.com">brunobogochvol@gmail.com</a>.
  </p>
</section>

