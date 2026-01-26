// src/documentacao/DocumentacaoVisaoGeral.tsx
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { vscDarkPlus } from "react-syntax-highlighter/dist/esm/styles/prism";

function DocumentacaoFormatos() {
  const mensagemEntrada = `Bom dia, prezados(as). Solicito, por gentileza, que me seja fornecida uma declaração em que conste meus dados cadastrais, tal como registrados no seu banco de dados, em que contenha meu nome, CPF, filiação, e características pessoais como Cor de pele e tipo de cabelo (caso façam parte do seu banco de dados). Nome: João Lopes Ribeiro CPF: 12345678908 RG: 0987654 Mãe:Gabriela Isabel Campos Lima Cruz CNH: 78945612378 Título de eleitor: 321654987321 (zona 01, seção 123) CTPS: 65421 - Série: 00123/DF At.te João Ribeiro`;

  const retornoJson = {
    Mensagem: "Bom dia, prezados(as)...",
    Indice: 24.0,
    Criticidade: 3,
    Questionamento: 1.0,
    Pessoalidade: 0.6,
    Impessoalidade: 0.4,
    Rastreabilidade: 2,
    Validacao: "Esse pedido solicita acesso a informacoes pessoais.",
    Status: "NAO",
    Linhas: [
      {
        linha: "Bom dia, prezados(as)...",
        status: "NAO",
        motivo: "Solicitação detectada com termos sensiveis: CPF, RG",
        contexto_juridico: false,
        tem_solicitacao: true,
        tem_termo_sensivel: true,
        termos_sensiveis: ["CPF", "RG"],
        solicitacao: ["solicito", "declaracao"],
      },
    ],
    Documentos: {
      CPF: ["12345678908"],
      RG: ["0987654"],
      PROCESSO_SEI: [],
      TELEFONE: [],
      "E-MAIL": [],
    },
    Motivo: "Solicitação detectada com termos sensiveis: CPF, RG",
    Motivo_bloqueou: [
      {
        expressao: ["solicito", "declaracao"],
        termo_invalido: ["CPF", "RG"],
        posicao: 35,
      },
    ],
  };

  return (
    <div className="p-6">
      {/* Mensagem original */}
      <div className="mb-8 p-4 border rounded bg-gray-50">
        <h3 className="text-xl font-semibold mb-2">Mensagem de Entrada</h3>
        <p className="text-sm whitespace-pre-line">{mensagemEntrada}</p>
      </div>

      {/* JSON com syntax highlight */}
      <h3 className="text-xl font-semibold mb-3">Exemplo de Retorno</h3>
      <div className="rounded overflow-hidden border">
        <SyntaxHighlighter
          language="json"
          style={vscDarkPlus}
          customStyle={{ margin: 0, padding: "1rem", fontSize: "0.85rem" }}
        >
          {JSON.stringify(retornoJson, null, 2)}
        </SyntaxHighlighter>
      </div>
    </div>
  );
}

export default DocumentacaoFormatos;
