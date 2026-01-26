
# ⚙️ Backend: Motor de Análise Participa DF (Core)

Este diretório contém o núcleo lógico do projeto **Participa DF – Acesso à Informação**, construído com **Python** e **Flask**. O backend é responsável pelo processamento de linguagem natural (NLP), validação de segurança via Regex e gestão de persistência de dados local.

---

## 🏗️ Arquitetura do Sistema

O backend opera como um pipeline de processamento de texto estruturado:

1.  **Sanitização:** Limpeza do texto e normalização de caracteres.
2.  **Parser Semântico:** Identificação de verbos de solicitação e sua conjugação.
3.  **Validação de Segurança:** Cruzamento de termos encontrados com a lista de termos sensíveis (LGPD).
4.  **Rastreabilidade:** Extração de padrões de documentos (CPF, RG, SEI) via Expressões Regulares.
5.  **Score Engine:** Cálculo de índices de criticidade, pessoalidade e contexto jurídico.



---

## 🛠️ Tecnologias e Stack

* **Linguagem:** Python 3.x
* **Framework Web:** Flask
* **Banco de Dados:** **SQLite** (Armazenamento local em arquivo, sem necessidade de servidor externo)
* **Processamento de Texto:** * Engine de Regex (`re`) para documentos oficiais.
    * Algoritmo de conjugação para verbos regulares e tratamento de irregulares.

---

## 🔌 API Reference

### 1. Análise de Texto
`POST /api/solicitar_analise`

**Payload:**
```json
{
  "texto": "Solicito acesso ao CPF do servidor X."
}

```

**Resposta:**

```json
{
  "Status": "NAO",
  "Validacao": "Esse pedido solicita acesso a informacoes pessoais.",
  "Motivo": "Solicitação detectada (\"solicito\") com termo inválido (\"cpf\")"
}

```

### 2. Gestão de Dados (SQLite)

* `GET /api/solicitacoes`: Retorna a lista paginada de registros salvos no `database.db`.
* `GET /api/estatisticas_30dias`: Agrega dados do SQLite para gerar métricas de volumetria.
* `GET /api/solicitacoes/info`: Retorna metadados sobre o volume de dados armazenados.

---

## 📂 Configuração e Parâmetros

A inteligência do motor é baseada em arquivos JSON/YAML de configuração, permitindo ajustes sem mexer no código:

* **`termos_sensiveis`**: Dicionário de termos que bloqueiam a solicitação.
* **`verbos_solicitacao`**: Base de dados para o parser identificar intenções.
* **`parametros_juridicos`**: Termos que validam o embasamento legal do pedido.

---

## 🛡️ Segurança e Regras de Negócio

O backend aplica filtros rigorosos via Regex para identificar:

* **CPF:** `\d{3}\.\d{3}\.\d{3}-\d{2}`
* **RG:** Padrões numéricos variados.
* **Contatos:** E-mails e números de telefone.
* **Processos:** Padrões de numeração do Sistema Eletrônico de Informações (SEI).

---

## 🚀 Inicialização Técnica

1. **Instalar dependências:**
```bash
pip install -r requirements.txt

```


2. **Setup do Banco de Dados:**
O arquivo SQLite (`banco.db`) será criado automaticamente na primeira execução ou via script de migração.
3. **Executar:**
```bash
python app.py

```


