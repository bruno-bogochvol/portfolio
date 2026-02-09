# Documento de Requisitos do Produto (PRD) - Estrutura do Portfólio

Este arquivo documenta a estrutura de pastas, componentes e a lógica de funcionamento do portfólio.

## Visão Geral
O projeto é um site estático gerado via **Jekyll**, utilizando o tema base `jekyll-theme-cayman`. A estrutura foi modernizada para um layout baseado em **cartões (cards)**, gerenciado por dados estruturados, suportando conteúdo bilíngue (Português e Inglês).

## Estrutura de Pastas

### Raiz (`/`)
Arquivos de configuração e pontos de entrada.
- **`_config.yml`**: Configuração global do Jekyll (Título, descrição, baseurl).
- **`index.md`**: Página inicial (PT). Utiliza Liquid para renderizar os cartões de projetos.
- **`README.md`**: Versão estática e simplificada para visualização direta no GitHub.
- **`_data/`**: Contém o arquivo `projects.yml` que centraliza todos os dados dos projetos (Títulos, stacks, links e imagens).
- **`assets/`**:
  - `css/style.scss`: Folha de estilo principal que estende o tema Cayman com o layout de cartões.
  - `projects/`: Armazena imagens e thumbnails dos projetos.
  - `pdfs/`: Currículos e documentos para download.

### Diretório de Cases (`/cases`)
Estudos de caso detalhados. Cada subpasta representa um projeto.
- **Padronização**: Cada case possui um `index.md` (PT) e um `README_EN.md` (EN).
- **Seção de Galeria**: Todos os cases possuem uma estrutura de galeria visual (`## 📸 Galeria`) para exibição de screenshots e diagramas.

### Diretório de Conteúdo em Inglês (`/en`)
- **`index.md`**: Versão em inglês da página inicial, espelhando a lógica de cartões da raiz.

## Componentes e Funcionalidades

### 1. Sistema de Cartões (Project Cards)
Os projetos não são mais listados em tabelas manuais. Eles são iterados a partir de `_data/projects.yml`.
- **Campos**: `title`, `category`, `role`, `stack`, `description`, `image`, `links` (case, production, figma, repo).
- **Lógica**: O botão de cada link só aparece se o campo correspondente estiver preenchido no YAML.

### 2. Seletor de Idioma (Language Switcher)
Componente flutuante que permite alternar entre as versões PT e EN, mantendo a consistência visual.

### 3. Estilo Customizado (SCSS)
O arquivo `assets/css/style.scss` sobrescreve o tema padrão para implementar:
- Grid responsivo de cartões.
- Efeitos de hover e sombras.
- Ajuste de imagens (`object-fit: cover`).
- Estilização de botões (`btn-sm`, `btn-primary`).

## Fluxo de Manutenção
Para adicionar um novo projeto:
1. Adicione a imagem em `assets/projects/`.
2. Insira os dados no final de `_data/projects.yml`.
3. Crie a pasta correspondente em `cases/` seguindo o template de Galeria.
