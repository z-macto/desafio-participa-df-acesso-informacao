
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
```text
Venho solicitar junto a Caesb o histórico de consumo da inscrição:157028-1, 
sob o CPF: 129.180.122-6, Júlio Cesar Alves da Rosa, no período de 12/2002 a
01/2007. E o histórico de consumo da Inscrição: 00569848-9, sob o 
CPF: 210.201.140-24, Maria Martins Mota Silva. Tal solicitação se deve, 
a fim de fazer o comparativo de consumo destes imóveis no período em que 
residi com minha família. Preciso solicitar justificativas para um consumo 
atual muito alto para as características do imóvel, quantidade de pessoas. 
No primeiro imóvel residiam 10 pessoas o terreno de 2.000 metros quadrados ,
tinha pomar, grama, piscina (10X6), sauna, instalações antigas com 
15 banheiros. Atualmente a casa tem 800 metros quadrados, somente 02 adultos
e 04 criança. Pequeno jardim e a casa tem a estrutura toda nova. 
Foram feitos várias solicitações junto à Caesb e a empresa de caça-vazamentos 
para que pudéssemos identificar vazamentos e demais anormalidades que causassem 
esse consumo absurdo. juntamente com os históricos de consumo citados, desejo 
receber também as cartas respostas referentes a todas minha solicitações.
```

**Resposta:**
```json
{
   "resposta":{
      "Criticidade":4,
      "Documentos":{
         "CHN":[
            
         ],
         "CPF":[
            
         ],
         "E-MAIL":[
            
         ],
         "OAB":[
            
         ],
         "PROCESSO_SEI":[
            
         ],
         "RG":[
            "00569848-9"
         ],
         "SUS":[
            
         ],
         "TELEFONE":[
            
         ]
      },
      "Impessoalidade":0.86,
      "Indice":6.86,
      "Linhas":[
         {
            "contexto_juridico":false,
            "linha":"Venho solicitar junto a Caesb o histórico de consumo da inscrição:157028-1, sob o CPF: 129",
            "motivo":"Solicitação detectada com termos sensiveis: cpf",
            "solicitacao":[
               "solicitar"
            ],
            "status":"NAO",
            "tem_solicitacao":true,
            "tem_termo_sensivel":true,
            "termos_sensiveis":[
               "cpf"
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"180",
            "motivo":"None",
            "solicitacao":[
               
            ],
            "status":"SIM",
            "tem_solicitacao":false,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"122-6, Júlio Cesar Alves da Rosa, no período de 12/2002 a 01/2007",
            "motivo":"None",
            "solicitacao":[
               
            ],
            "status":"SIM",
            "tem_solicitacao":false,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"E o histórico de consumo da Inscrição: 00569848-9, sob o CPF: 210",
            "motivo":"None",
            "solicitacao":[
               
            ],
            "status":"SIM",
            "tem_solicitacao":false,
            "tem_termo_sensivel":true,
            "termos_sensiveis":[
               "cpf"
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"201",
            "motivo":"None",
            "solicitacao":[
               
            ],
            "status":"SIM",
            "tem_solicitacao":false,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"140-24, Maria Martins Mota Silva",
            "motivo":"None",
            "solicitacao":[
               
            ],
            "status":"SIM",
            "tem_solicitacao":false,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"Tal solicitação se deve, a fim de fazer o comparativo de consumo destes imóveis no período em que residi com minha família",
            "motivo":"None",
            "solicitacao":[
               "solicitacao"
            ],
            "status":"SIM",
            "tem_solicitacao":true,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"Preciso solicitar justificativas para um consumo atual muito alto para as características do imóvel, quantidade de pessoas",
            "motivo":"None",
            "solicitacao":[
               "solicitar",
               "preciso",
               "preciso"
            ],
            "status":"SIM",
            "tem_solicitacao":true,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"No primeiro imóvel residiam 10 pessoas o terreno de 2",
            "motivo":"None",
            "solicitacao":[
               
            ],
            "status":"SIM",
            "tem_solicitacao":false,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"000 metros quadrados , tinha pomar, grama, piscina (10X6), sauna, instalações antigas com 15 banheiros",
            "motivo":"None",
            "solicitacao":[
               
            ],
            "status":"SIM",
            "tem_solicitacao":false,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"Atualmente a casa tem 800 metros quadrados, somente 02 adultos e 04 criança",
            "motivo":"None",
            "solicitacao":[
               "tem",
               "tem"
            ],
            "status":"SIM",
            "tem_solicitacao":true,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"Pequeno jardim e a casa tem a estrutura toda nova",
            "motivo":"None",
            "solicitacao":[
               "tem",
               "tem",
               "que"
            ],
            "status":"SIM",
            "tem_solicitacao":true,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"Foram feitos várias solicitações junto à Caesb e a empresa de caça-vazamentos para que pudéssemos identificar vazamentos e demais anormalidades que causassem esse consumo absurdo",
            "motivo":"None",
            "solicitacao":[
               "que"
            ],
            "status":"SIM",
            "tem_solicitacao":true,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         },
         {
            "contexto_juridico":false,
            "linha":"juntamente com os históricos de consumo citados, desejo receber também as cartas respostas referentes a todas minha solicitações",
            "motivo":"None",
            "solicitacao":[
               "desejo",
               "receber"
            ],
            "status":"SIM",
            "tem_solicitacao":true,
            "tem_termo_sensivel":false,
            "termos_sensiveis":[
               
            ]
         }
      ],
      "Mensagem":"Venho solicitar junto a Caesb o histórico de consumo da inscrição:157028-1, sob o CPF: 129.180.122-6, Júlio Cesar Alves da Rosa, no período de 12/2002 a 01/2007. E o histórico de consumo da Inscrição: 00569848-9, sob o CPF: 210.201.140-24, Maria Martins Mota Silva. Tal solicitação se deve, a fim de fazer o comparativo de consumo destes imóveis no período em que residi com minha família. Preciso solicitar justificativas para um consumo atual muito alto para as características do imóvel, quantidade de pessoas. No primeiro imóvel residiam 10 pessoas o terreno de 2.000 metros quadrados , tinha pomar, grama, piscina (10X6), sauna, instalações antigas com 15 banheiros. Atualmente a casa tem 800 metros quadrados, somente 02 adultos e 04 criança. Pequeno jardim e a casa tem a estrutura toda nova. Foram feitos várias solicitações junto à Caesb e a empresa de caça-vazamentos para que pudéssemos identificar vazamentos e demais anormalidades que causassem esse consumo absurdo. juntamente com os históricos de consumo citados, desejo receber também as cartas respostas referentes a todas minha solicitações.",
      "Motivo":"Solicitação detectada com termos sensiveis: cpf",
      "Motivo_bloqueou":[
         {
            "expressao":[
               "solicitar"
            ],
            "posicao":6,
            "termo_invalido":[
               "cpf"
            ]
         }
      ],
      "Pessoalidade":0.14,
      "Questionamento":0.5,
      "Rastreabilidade":1,
      "Retorno":"Venho solicitar junto a Caesb o histórico de consumo da inscrição:157028-1, sob o CPF: 129.180.122-6, Júlio Cesar Alves da Rosa, no período de 12/2002 a 01/2007. E o histórico de consumo da Inscrição: 00569848-9, sob o CPF: 210.201.140-24, Maria Martins Mota Silva. Tal solicitação se deve, a fim de fazer o comparativo de consumo destes imóveis no período em que residi com minha família. Preciso solicitar justificativas para um consumo atual muito alto para as características do imóvel, quantidade de pessoas. No primeiro imóvel residiam 10 pessoas o terreno de 2.000 metros quadrados , tinha pomar, grama, piscina (10X6), sauna, instalações antigas com 15 banheiros. Atualmente a casa tem 800 metros quadrados, somente 02 adultos e 04 criança. Pequeno jardim e a casa tem a estrutura toda nova. Foram feitos várias solicitações junto à Caesb e a empresa de caça-vazamentos para que pudéssemos identificar vazamentos e demais anormalidades que causassem esse consumo absurdo. juntamente com os históricos de consumo citados, desejo receber também as cartas respostas referentes a todas minha solicitações.",
      "Status":"NAO",
      "Validacao":"Esse pedido solicita acesso a informacoes pessoais."
   }
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


