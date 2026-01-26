
# 📖 Projeto: Desafio Participa DF – Acesso à Informação

## 📌 Descrição

Este projeto é uma aplicação **Flask** que analisa textos de solicitações de acesso à informação, verificando se são válidos ou inválidos com base em parâmetros pré-definidos.  
Ele identifica:

- **Solicitações** (verbos e expressões que indicam pedido).
- **Contexto jurídico** (expressões legais e formais).
- **Termos sensíveis** (informações pessoais ou termos sensíveis).
- **Documentos rastreáveis** (CPF, RG, telefone, e-mail, processo SEI).

Além disso, possui rotas para **testes em massa**, **estatísticas de uso** e **consulta de solicitações armazenadas**.

---

## 🚀 Funcionalidades

- Interface web simples para envio de solicitações.
- Análise automática de cada linha do texto:
  - Detecta verbos e substantivos de solicitação.
  - Identifica expressões jurídicas fixas e conjugáveis.
  - Bloqueia solicitações que contenham termos sensíveis.
- Histórico dos últimos pedidos armazenados em banco de dados.
- Página dedicada para execução de testes em lote.
- Estatísticas de solicitações realizadas nos últimos 30 dias.
- Consulta paginada de solicitações já registradas.

---

## ⚙️ Instalação e Uso

### 1. Clonar o repositório

```bash
git clone https://github.com/z-macto/desafio-participa-df-acesso-informacao.git
cd desafio-participa-df-acesso-informacao
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar a aplicação

```bash
python3 app.py
```

### 4. Acesse no navegador

```bash
http://localhost:5000
```

---

## 📂 Rotas disponíveis

| Rota                        | Método | Descrição                                                                 |
| --------------------------- | ------ | ------------------------------------------------------------------------- |
| `/`                         | GET    | Página principal para análise de solicitações                             |
| `/testes`                   | GET    | Página para execução de testes em massa                                   |
| `/api/solicitar_analise`    | POST   | Recebe um texto e retorna análise completa em JSON                        |
| `/api/testes`               | GET    | Executa testes em lote e retorna resumo                                   |
| `/api/estatisticas_30dias`  | GET    | Retorna estatísticas de solicitações dos últimos 30 dias                  |
| `/api/solicitacoes/info`    | GET    | Retorna total de solicitações e número de páginas                         |
| `/api/solicitacoes`         | GET    | Lista solicitações registradas, com suporte a paginação (`?pagina=N`)     |

---

## ✅ Exemplos de uso

### Exemplo 1 – Solicitação aceitável

**Entrada:**

```text
Venho por meio desta solicitar acesso aos documentos do processo.
```

**Saída:**

```json
{
  "Validacao": "Pedido aceitavel !",
  "Status": "SIM",
  "Linhas": [
    {
      "linha": "Venho por meio desta solicitar acesso aos documentos do processo.",
      "status": "SIM",
      "motivo": null,
      "contexto_juridico": false
    }
  ]
}
```

---

### Exemplo 2 – Solicitação inválida (dados pessoais)

**Entrada:**

```text
Venho por meio desta solicitar acesso ao CPF dos servidores.
```

**Saída:**

```json
{
  "Validacao": "Esse pedido solicita acesso a informacoes pessoais.",
  "Status": "NAO",
  "Linhas": [
    {
      "linha": "Venho por meio desta solicitar acesso ao CPF dos servidores.",
      "status": "NAO",
      "motivo": "Solicitação detectada (\"solicitar\") com termo inválido (\"cpf\")",
      "contexto_juridico": false
    }
  ],
  "Motivo": "Solicitação detectada (\"solicitar\") com termo inválido (\"cpf\")",
  "Motivo_bloqueou": [
    {
      "expressao": "solicitar",
      "termo_invalido": "cpf",
      "posicao": 27
    }
  ]
}
```

---

### Exemplo 3 – Solicitação aceitável com contexto jurídico

**Entrada:**

```text
Com fundamento no artigo 5º da Constituição, venho requerer acesso aos documentos.
```

**Saída:**

```json
{
  "Validacao": "Pedido aceitavel !",
  "Status": "SIM",
  "Linhas": [
    {
      "linha": "Com fundamento no artigo 5º da Constituição, venho requerer acesso aos documentos.",
      "status": "SIM",
      "motivo": null,
      "contexto_juridico": true
    }
  ]
}
```

---

### Exemplo 4 – Solicitação inválida com múltiplos dados pessoais

**Entrada:**

```text
Solicito acesso ao banco de dados contendo nome, CPF, RG e endereço dos servidores.
```

**Saída:**

```json
{
  "Validacao": "Esse pedido solicita acesso a informacoes pessoais.",
  "Status": "NAO",
  "Linhas": [
    {
      "linha": "Solicito acesso ao banco de dados contendo nome, CPF, RG e endereço dos servidores.",
      "status": "NAO",
      "motivo": "Solicitação detectada (\"solicito\") com termos inválidos (\"cpf\", \"rg\", \"endereço\")",
      "contexto_juridico": false
    }
  ],
  "Motivo": "Solicitação detectada (\"solicito\") com termos inválidos (\"cpf\", \"rg\", \"endereço\")",
  "Motivo_bloqueou": [
    {
      "expressao": "solicito",
      "termo_invalido": ["cpf", "rg", "endereço"],
      "posicao": 0
    }
  ]
}
```

---

## 📊 Estatísticas e Rastreabilidade

- O motor calcula métricas como **Criticidade**, **Questionamento**, **Pessoalidade**, **Impessoalidade** e um **Índice Final** consolidado.
- O **Índice de Rastreabilidade** indica quantos documentos pessoais foram encontrados no texto (CPF, RG, telefone, e-mail, processo SEI).

---

## 🛡️ Segurança e Configuração

- Detectores de padrões com **REGEX** para documentos.
- Parser semântico para frases em português.
- Conjugador de verbos regulares e lista de verbos irregulares.
- Arquivos de parâmetros configuráveis para:
  - Termos sensíveis
  - Verbos regulares e irregulares
  - Termos de solicitação
  - Parâmetros jurídicos

---
