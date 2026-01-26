# 🎨 Frontend – Desafio Participa DF: Acesso à Informação

## 📌 Descrição

Este é o frontend da aplicação **Desafio Participa DF – Acesso à Informação**, desenvolvido em **React + TypeScript**.  
Ele fornece uma interface web para interação com o motor de análise de solicitações, exibindo resultados, estatísticas e documentação de forma clara e acessível.

---

## 🚀 Funcionalidades

- Interface para envio de solicitações de acesso à informação.
- Exibição dos resultados da análise (status, motivos, métricas e documentos encontrados).
- Páginas de documentação explicando:
  - **Visão Geral** das APIs.
  - **Metodologia** do motor de análise.
  - **Segurança** e configuração do sistema.
- Visualização de estatísticas e histórico de solicitações.
- Integração com o backend via rotas REST.

---

## ⚙️ Instalação e Uso

### 1. Clonar o repositório

```bash
git clone https://github.com/z-macto/desafio-participa-df-acesso-informacao.git
cd desafio-participa-df-acesso-informacao/frontend
```

### 2. Instalar dependências

```bash
npm install
```

### 3. Executar a aplicação

```bash
npm run dev
```

### 4. Acesse no navegador

```bash
http://localhost:5173
```

---

## 📂 Estrutura de Pastas

```
frontend/
├── src/
│   ├── abas/               # Abas principais da interface (Central, Testes, Documentação)
│   ├── assets/             # Imagens e ícones
│   ├── componentes/        # Componentes reutilizáveis (Cabeçalho, Rodapé, Widget de resposta)
│   ├── documentacao/       # Páginas explicativas sobre o sistema
│   ├── App.tsx             # Componente raiz
│   └── App.css             # Estilos globais
├── public/                 # Arquivos públicos
├── package.json            # Dependências e scripts
└── vite.config.ts          # Configuração do Vite
```

---

## 📄 Principais Páginas

- `DocumentacaoVisaoGeral.tsx` – Explica as APIs disponíveis.
- `DocumentacaoMetodologia.tsx` – Detalha o funcionamento do motor de análise.
- `DocumentacaoSeguranca.tsx` – Mostra como o sistema garante segurança e configuração.
- `DocumentacaoInstalacao.tsx` – Guia de instalação e uso.
- `AbaPedidoInformacao.tsx` – Interface principal para envio de solicitações.
- `AbaTestes.tsx` – Execução de testes em lote.
- `AbaDocumentacao.tsx` – Navegação entre páginas explicativas.

---

## ✅ Exemplos de Uso

### Exemplo 1 – Solicitação aceitável

**Entrada:**

```text
Venho por meio desta solicitar acesso aos documentos do processo.
```

**Saída exibida:**

```json
{
  "Validacao": "Pedido aceitavel !",
  "Status": "SIM",
  "Indice": 12.5,
  "Criticidade": 2,
  "Questionamento": 0.5,
  "Pessoalidade": 0,
  "Impessoalidade": 1,
  "Rastreabilidade": 0
}
```

---

### Exemplo 2 – Solicitação inválida

**Entrada:**

```text
Solicito acesso ao CPF dos servidores.
```

**Saída exibida:**

```json
{
  "Validacao": "Esse pedido solicita acesso a informacoes pessoais.",
  "Status": "NAO",
  "Motivo": "Solicitação detectada com termo inválido (\"cpf\")",
  "Rastreabilidade": 1
}
```

---

### Exemplo 3 – Solicitação com contexto jurídico

**Entrada:**

```text
Com fundamento no artigo 5º da Constituição, venho requerer acesso aos documentos.
```

**Saída exibida:**

```json
{
  "Validacao": "Pedido aceitavel !",
  "Status": "SIM",
  "Contexto_juridico": true
}
```

---

### Exemplo 4 – Solicitação com múltiplos dados pessoais

**Entrada:**

```text
Solicito acesso ao banco de dados contendo nome, CPF, RG e endereço dos servidores.
```

**Saída exibida:**

```json
{
  "Validacao": "Esse pedido solicita acesso a informacoes pessoais.",
  "Status": "NAO",
  "Motivo": "Solicitação detectada com termos inválidos (\"cpf\", \"rg\", \"endereço\")",
  "Rastreabilidade": 3
}
```

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

## 🛠️ Tecnologias Utilizadas

- **React** + **TypeScript**
- **Vite** (build tool)
- **TailwindCSS** (estilização)
- **Heroicons** (ícones)
- **Axios / Fetch API** (requisições ao backend)

---
