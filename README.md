# 📖 Projeto: Desafio Participa DF – Acesso à Informação

## 📌 Descrição

Este projeto é uma aplicação **Flask** que analisa textos de solicitações de acesso à informação, verificando se são válidos ou inválidos com base em parâmetros pré-definidos.  
Ele identifica:

- **Solicitações** (verbos e expressões que indicam pedido).
- **Contexto jurídico** (expressões legais e formais).
- **Palavras proibidas** (informações pessoais ou termos sensíveis).

Além disso, possui uma rota de **testes em massa** para validar automaticamente diversos exemplos.

---

## 🚀 Funcionalidades

- Interface web simples para envio de solicitações.
- Análise automática de cada linha do texto:
  - Detecta verbos e substantivos de solicitação.
  - Identifica expressões jurídicas fixas e conjugáveis.
  - Bloqueia solicitações que contenham termos proibidos.
- Histórico dos últimos 5 pedidos armazenados em sessão.
- Página dedicada para execução de testes em lote.

---

## ⚙️ Instalação e Uso

### 1. Clonar o repositório

```bash
git clone https://github.com/z-macto/desafio-participa-df-acesso-informacao.git
cd desafio-participa-df-acesso-informacao
```

2. Instalar dependências

```bash
   pip install -r requirements.txt
```

3. Executar a aplicação

```bash
   python app.py
```

4. Acesse no navegador:

```bash
http://localhost:5000
```

## 📂 Rotas disponíveis

### Tabela de rotas

| Rota      | Descrição                                     |
| --------- | --------------------------------------------- |
| `/`       | Página principal para análise de solicitações |
| `/testes` | Página para execução de testes em massa       |

## ✅ Exemplo de uso

### Entrada

```text
Venho por meio desta solicitar acesso aos documentos do processo.
```

```bash
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
