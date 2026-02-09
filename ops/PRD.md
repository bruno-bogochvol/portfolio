# Documento de Requisitos do Produto (PRD) - Estrutura do Portfólio

Este arquivo documenta a estrutura de pastas e componentes presentes no repositório.

## Visão Geral
O projeto é um site estático gerado via Jekyll, utilizando o tema `jekyll-theme-cayman`. A estrutura é organizada para suportar conteúdo bilíngue (Português e Inglês) e estudos de caso (cases).

## Estrutura de Pastas

### Raiz (`/`)
Arquivos de configuração e pontos de entrada principais.
- **`_config.yml`**: Arquivo de configuração do Jekyll. Define título, descrição e tema.
- **`index.md`**: Página inicial do portfólio (versão em Português).
- **`README.md`**: Documentação do repositório (Português).
- **`README_EN.md`**: Documentação do repositório (Inglês).
- **`.git/`**: Controle de versão Git.
- **`assets/`**: Arquivos estáticos (ex: currículos em PDF).
- **`ops/`**: Pasta de operações e documentação (onde este arquivo reside).

### Diretório de Cases (`/cases`)
Contém os estudos de caso individuais do portfólio. Cada subpasta representa um projeto específico com suas respectivas documentações em ambos os idiomas.
- **`guerreiro-system/`**
  - `README.md`
  - `README_EN.md`
- **`thinksus-esg/`**
  - Conteúdo do case Thinksus ESG.
- **`veiculando/`**
  - Conteúdo do case Veiculando.

### Diretório de Conteúdo em Inglês (`/en`)
Estrutura espelhada para a versão em inglês do site.
- **`index.md`**: Página inicial (versão em Inglês).
- **`README_EN.md`**: (Provável duplicata ou link simbólico para a documentação em inglês).

## Componentes

### Tema e Layout
O projeto utiliza o tema **`jekyll-theme-cayman`**, que provê a estrutura visual básica (layouts, includes, assets).
- Não há pastas locais de `_layouts`, `_includes` ou `_sass` visíveis na raiz, indicando uso direto da gem do tema sem sobrescritas locais neste momento.

### Componentes de Conteúdo
Os "componentes" neste contexto são os blocos de conteúdo markdown:
1.  **Página Inicial (Index)**:
    - Definida em `index.md` (PT) e `en/index.md` (EN).
2.  **Cases (Projetos)**:
    - Cada pasta dentro de `cases/` atua como um componente de projeto isolado.
    - Estrutura interna de cada case consiste em arquivos `README.md` para apresentação.
