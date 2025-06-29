# 🧠 Semantic ETL Pipelines for Heterogeneous Knowledge Graph Construction  
### Estudo de Caso: Políticos do Brasil – Deputados Federais

[🔗 Semantic ETL Pipelines — Relatório Técnico](https://drive.google.com/file/d/1xNdSfGthanTfC1u3vA1sCYyPM3cQwF77/view?usp=sharing)

[🔗 Semantic ETL Pipelines — Apresentação](https://docs.google.com/presentation/d/1brM-k18QR9xEqyejHO81sLAsU7dHI4k65FvbiTpKuYY/edit?usp=sharing)

---

## 📌 Visão Geral

Este projeto implementa uma pipeline **ETL Semântica (Extração, Transformação e Carga)** para a **unificação de dados heterogêneos** sobre deputados federais do Brasil. O objetivo é construir um **Grafo de Conhecimento (HKG - Heterogeneous Knowledge Graph)** que permita análises avançadas e integração semântica para sistemas de perguntas e respostas (QA Systems) e plataformas analíticas.

---

## 🎬 Demonstração em Vídeo

Assista ao vídeo explicativo do pipeline ETL para Deputados Federais:

https://github.com/user-attachments/assets/ef46a564-0394-4665-9ba9-c9405e4b1949

---

## 📊 Arquitetura do Pipeline

A estrutura segue o modelo representado abaixo:

Data Source (Extraction) → Business Layer (Transform) → Knowledge Graph (Load) → Presentation Layer


![Semantic ETL Architecture](./graph/docs/images/etl_semantic_pipeline.png)

[Consulte a arquitetura detalhada do pipeline no arquivo `graph/docs/arquitetura.md`](graph/docs/arquitetura.md)

---

## 📁 Estrutura do Projeto

```
graph_nous/
│
├── graph/               # Código principal da aplicação
│ ├── config.py          # Configurações globais (variáveis, paths, env)
│ ├── interface.py       # Interface Streamlit (frontend)
│ ├── main.py            # Execução local via terminal
│ └── core/              # Lógica de negócio e manipulação de dados
│    ├── etl/            # Extração, transformação e carga de dados (ETL)
│    └── data/           # Lógica de persistência e tecnologias específicas
│    │     ├── rdf/      # Manipulação de dados RDF (triplas, .nt, .ttl)
│    │     └── neo4j/    # Conexão e visualização de grafos Neo4j
│    │
├── dataset/             # Dados usados no projeto
│ ├── raw/               # Dados brutos (ex: CSVs originais)
│ └── processed/         # Dados processados (ex: .nt, .graphml)
│
├── docs/                # Documentação do projeto
│ ├── arquitetura.md     # Arquitetura do sistema
│ ├── requisitos.md      # Requisitos funcionais e não-funcionais
│ └── images/            # Imagens usadas na documentação
│
├── tests/               # Testes automatizados (unitários, integração)
│
├── .env                 # Variáveis de ambiente sensíveis (não versionar)
├── .gitignore           # Arquivos/pastas a serem ignorados pelo Git
├── README.md            # Você está aqui :). Descrição inicial do projeto
├── requirements.txt     # Dependências para produção
├── requirements_dev.txt # Dependências adicionais para desenvolvimento/testes
└── setup.py             # (Opcional) Empacotamento do projeto como módulo Python
```

[Consulte a estrutura detalhada do projeto `graph/docs/estrutura.md`](graph/docs/estrutura.md)

## 🚀 Como Executar

### **Pré-requisitos**

- **Clonar o projeto**

     ```bash
     git clone git@github.com:ronenfilho/graph_nous.git
     ```

- **Python 3.11+** instalado

- **Instale o Neo4J (https://neo4j.com/)**

- Arquivo `.env` configurado com as variáveis de ambiente necessárias

# 1. Criar ambiente virtual

```
python -m venv venv
# (Windows) ou source venv/bin/activate (Linux/Mac)
venv\Scripts\activate  
```
# 2. Instalar dependências

```
pip install -r requirements.txt
```

# 3. Rodar o projeto

```
python graph/main.py
```

## ▶️ Como Executar o Projeto Streamlit

Este guia apresenta os passos para rodar a interface do projeto utilizando o **Streamlit**.

### **Passos para Execução**

1. **Navegue até o diretório do projeto**

     No terminal, acesse o diretório onde está localizado o arquivo `interface.py`:
     ```bash
     cd caminho/para/seu/graph_nous
     ```

2. **Execute o Streamlit**

     Inicie a aplicação com o comando:
     ```bash
     streamlit run graph/interface.py
     ```

3. **Acesse a interface no navegador**

     O Streamlit abrirá automaticamente a interface no navegador.  
     Caso não abra, copie o link exibido no terminal (geralmente `http://localhost:8501`) e cole no navegador.

# Resultados

## Grafo - Nó Deputado

![Grafo - Deputado](./graph/docs/images/img_grafo_deputado.png)

## 🧰 Tecnologias Utilizadas

### 🐍 Python
- **Versão:** 3.11+

---

### 📊 Manipulação e Extração de Dados
- `pandas==2.3.0` — Estrutura de dados e análise tabular  
- `requests==2.32.4` — Requisições HTTP para APIs públicas

---

### 🌐 Semântica e Grafos RDF
- `rdflib==7.1.4` — Construção e serialização de triplas RDF  
- `rdflib_neo4j==1.1` — Integração de triplas RDF com o banco Neo4j  
- **Ontologias:** OWL / SKOS — Enriquecimento semântico e modelagem de conceitos

---

### 🧠 Banco de Grafos
- **GraphDB** — Armazenamento semântico e consultas SPARQL  
- **Neo4j** — Grafo orientado a relações e visualizações dinâmicas

---

### 📈 Visualização
- `matplotlib==3.10.3` — Gráficos analíticos e plots de dados  
- `networkx==3.5` — Modelagem e análise de grafos em Python  
- `pyvis==0.3.2` — Visualização interativa de grafos (HTML / Streamlit)

---

### 🌍 Interface Web
- `streamlit==1.45.1` — Construção de dashboards e aplicações web interativas

---

### ⚙️ Utilitários
- `python-dotenv==1.1.0` — Gerenciamento de variáveis de ambiente (.env)  
- `setuptools==80.9.0` — Empacotamento e instalação como módulo Python

---

### 📦 Criação do requirements.txt

```
pip freeze > requirements.txt
```

- **Gegar versão resumida** 
```
pipreqs . --force
```

---

## 🧪 Próximos Passos (TODO LIST)

- [✅] Carga de Deputados Federais (Brasil).
- [✅] Normalização com identificadores globais.
- [✅] Geração automatizada de triplos RDF a partir de dados limpos.
- [✅] Visualização e consulta semântica com **Neo4j**, **GraphDB** ou **SPARQL endpoints**.
- [✅] Integração com dados de despesas dos deputados.
- [ ] Integração com dados partidos.
- [ ] Integração com dados de proposições legislativas.

---

# 📊 Esquema RDF – Deputados e Despesas Públicas

Este documento descreve a estrutura do grafo RDF gerado a partir dos dados da Câmara dos Deputados, relacionando parlamentares, partidos, unidades federativas e despesas públicas.

---

## 🧠 Estrutura Geral do Grafo

### 🟦 Classe: `Person` (Deputado)
**URI:** `https://dadosabertos.camara.leg.br/recurso/deputado/{id}`

| Predicado                  | Tipo         | Exemplo                                       |
|----------------------------|--------------|-----------------------------------------------|
| `rdf:type`                 | URI          | `schema:Person`                               |
| `schema:name`              | Literal      | `"João Silva"`                                |
| `schema:identifier`        | Literal int  | `1234`                                        |
| `schema:memberOf`          | URI          | `https://.../partido/PL`                      |
| `schema:addressRegion`     | URI          | `https://.../uf/SP`                           |
| `foaf:page`                | URI          | `https://.../deputado/1234`                   |
| `schema:image`             | URI          | `https://.../foto.jpg`                        |
| `schema:email` (opcional)  | Literal      | `"email@camara.leg.br"`                       |
| `pol:legislatura`          | Literal int  | `57`                                          |

---

### 🟦 Classe: `Organization` (Partido)
**URI:** `https://.../partido/{sigla}`

| Predicado        | Tipo     | Exemplo      |
|------------------|----------|--------------|
| `rdf:type`       | URI      | `schema:Organization` |
| `schema:name`    | Literal  | `"PL"`       |

---

### 🟦 Classe: `Place` (Unidade Federativa - UF)
**URI:** `https://.../uf/{sigla}`

| Predicado        | Tipo     | Exemplo |
|------------------|----------|---------|
| `rdf:type`       | URI      | `schema:Place` |
| `schema:name`    | Literal  | `"SP"`  |

---

### 🟩 Classe: `Expense` (Despesa)
**URI:** `https://.../despesa/{codDocumento}`

| Predicado              | Tipo             | Exemplo                                   |
|------------------------|------------------|-------------------------------------------|
| `rdf:type`             | URI              | `pol:Expense`                             |
| `schema:identifier`    | Literal int      | `999999`                                  |
| `pol:expenseType`      | URI              | `https://.../tipo-despesa/Combustível`    |
| `pol:expenseDate`      | Literal dateTime | `"2023-01-01T00:00:00"`                   |
| `pol:amount`           | Literal decimal  | `1350.75`                                 |
| `schema:provider`      | Literal          | `"Posto Central LTDA"`                    |
| `schema:url` (opcional)| URI              | `https://.../nota-fiscal.pdf`             |
| `pol:providerId` (opt.)| Literal          | `"12345678000199"`                        |

---

### 🟩 Classe: `ExpenseCategory` (Tipo de Despesa)
**URI:** `https://.../tipo-despesa/{tipo}`

| Predicado        | Tipo     | Exemplo           |
|------------------|----------|--------------------|
| `rdf:type`       | URI      | `pol:ExpenseCategory` |
| `schema:name`    | Literal  | `"Combustível"`    |

---

## 🔁 Relacionamentos (Arestas RDF com URI como Objeto)

| Sujeito (`@type`) | Predicado               | Objeto (`@type`)           |
|-------------------|--------------------------|-----------------------------|
| `Person`          | `pol:hasExpense`         | `Expense`                   |
| `Expense`         | `pol:expenseType`        | `ExpenseCategory`           |
| `Person`          | `schema:memberOf`        | `Organization`              |
| `Person`          | `schema:addressRegion`   | `Place`                     |
| `Person`          | `foaf:page`              | URI                         |
| `Person`          | `schema:image`           | URI                         |
| `Expense`         | `schema:url`             | URI                         |

---

## 📌 Tipos de Dados

### Literais:
- `schema:name`
- `schema:email`
- `schema:provider`
- `pol:amount`
- `pol:expenseDate`
- `schema:identifier`
- `pol:providerId`

### URIs:
- Todos os identificadores de recursos: `deputado`, `partido`, `uf`, `despesa`, `tipo-despesa`
- `schema:url`, `schema:image`, `foaf:page`

---

## 📘 Observações

- A modelagem utiliza **vocabulários padrão**: `schema.org`, `foaf`, `rdf`, além do vocabulário customizado `pol` (para política).
- Todos os nós são **identificados por URIs únicas**.
- As despesas estão **relacionadas diretamente aos deputados**, com metadados sobre tipo, valor, fornecedor e data.

---

## Cyper

```
CALL db.relationshipTypes()

╒════════════════╕
│relationshipType│
╞════════════════╡
│"addressRegion" │
├────────────────┤
│"image"         │
├────────────────┤
│"page"          │
├────────────────┤
│"memberOf"      │
├────────────────┤
│"hasExpense"    │
├────────────────┤
│"expenseType"   │
├────────────────┤
│"url"           │
└────────────────┘
```

## Resultados

### 🎬 Neo4j

https://github.com/user-attachments/assets/3f42872b-66d5-4519-980d-9aa9b65c188c

### 🎬 GraphDB

https://github.com/user-attachments/assets/707e00eb-198d-43de-93ac-20c67949eb5c

## 👤 Autor

**Ronen Filho**  
Especialização em Inteligência Artificial Aplicada — *IFG Goiás*  
Projeto acadêmico voltado à unificação semântica de dados sobre políticos brasileiros.


