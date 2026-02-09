---
layout: default
title: "Bruno Bogochvol — Portfolio"
---

<link rel="stylesheet" href="{{ "/assets/css/style.css" | relative_url }}">

{% include language_switcher.html current='en' %}

<section class="intro-section">
  <h1>Bruno Bogochvol</h1>
  <p class="fs-4 text-muted">Product Owner & Software Engineer</p>
  
  <p>
    I am a hybrid <strong>business and technology</strong> professional with experience in <strong>product management, software architecture, and Agile methodologies</strong>.<br>
    I operate at the intersection of <strong>discovery, UX, and engineering</strong>, translating product vision into technical delivery—always focused on <strong>value, automation, and quality (BDD/TDD)</strong>.
  </p>

  <p>
    📍 São Paulo, BR <br>
    📧 <a href="mailto:brunobogochvol@gmail.com">brunobogochvol@gmail.com</a> <br>
    🔗 <a href="https://linkedin.com/in/brunobogochvol">LinkedIn</a> · <a href="{{ '/assets/pdf/cv-en.pdf' | relative_url }}">PDF résumé</a>
  </p>
</section>

<hr>

<section>
  <h2>🧭 About Me</h2>
  <p>
    Graduated in <strong>Public Administration at FGV-EAESP</strong>, I transitioned into <strong>Software Engineering</strong> and have since been working as a <strong>technical PO and software architect</strong>, leading squads on web and mobile projects.<br>
    I have multisector experience—<strong>ESG, GovTech, Education, Healthcare, Fintech, and Sustainability</strong>—and I build products rooted in Agile practices, continuous discovery, and a DevOps culture.
  </p>
</section>

<section>
  <h2>⚙️ Stack & Practices</h2>
  <ul>
    <li><strong>Tech:</strong> Node.js (NestJS) · Angular/Ionic · Docker · GitHub Actions · MongoDB/MySQL · Azure</li>
    <li><strong>Product:</strong> PRDs · Roadmaps · Discovery · UX Flows · BPMN · Backlog Management (Jira, Projects v2)</li>
    <li><strong>Practices:</strong> Scrum/Kanban · BDD/TDD · CI/CD · Design Thinking · OKRs</li>
  </ul>
</section>

<hr>

<section>
  <h2>💼 Product Cases</h2>
  <p>Some of the projects below were delivered under a contractor engagement with <strong>Code Tech</strong>. The information was adapted to preserve client confidentiality.</p>

  <div class="project-grid">
    {% for project in site.data.projects %}
    <div class="project-card">
      {% if project.image %}
      <img src="{{ project.image | relative_url }}" alt="{{ project.title }}" class="card-image">
      {% endif %}
      <div class="card-header">
        <h3 class="card-title">{{ project.title }}</h3>
        <span class="card-category">{{ project.category_en }}</span>
      </div>
      
      <div class="card-body">
        <p class="card-description">{{ project.description_en }}</p>
        
        <div class="card-meta">
          <div class="meta-item">
            <span class="meta-label">Role:</span>
            <span class="meta-value">{{ project.role_en }}</span>
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
          <a href="{{ project.links.repo }}" class="btn-sm" target="_blank">💻 Code</a>
        {% endif %}

        {% if project.links.case_en %}
            <a href="{{ project.links.case_en | relative_url }}" class="btn-sm btn-primary">📄 View Case</a>
        {% elsif project.links.case %}
            <a href="{{ project.links.case | relative_url }}" class="btn-sm btn-primary">📄 View Case</a>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>
</section>

<hr>

<section>
  <h2>🧰 Templates & Processes</h2>
  <p>Models and artifacts I rely on daily as a technical PO.</p>
  <ul>
    <li><a href="{{ '/docs/template-PRD.md' | relative_url }}">📝 PRD Template</a></li>
    <li><a href="{{ '/docs/template-BDD.md' | relative_url }}">🧪 BDD Template</a></li>
    <li><a href="{{ '/docs/template-roadmap.md' | relative_url }}">🗺️ Roadmap Template</a></li>
    <li><a href="{{ '/docs/template-BPMN.png' | relative_url }}">📊 BPMN Example</a></li>
  </ul>
</section>

<hr>

<section>
  <h2>🛠️ Contact</h2>
  <p>
    Open to opportunities in <strong>technical product management, software architecture, and AI-driven innovation</strong>.<br>
    📬 Reach out via <a href="https://linkedin.com/in/brunobogochvol">LinkedIn</a> or email: <a href="mailto:brunobogochvol@gmail.com">brunobogochvol@gmail.com</a>.
  </p>
</section>

