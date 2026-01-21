import  { useState } from "react";

type Linha = {
  linha: string;
  status: string;
  motivo?: string;
};

type Resposta = {
  Status: string;
  Validacao: string;
  Indice: number;
  Criticidade: number;
  Questionamento: number;
  Pessoalidade: number;
  Impessoalidade: number;
  Linhas: Linha[];
  Motivo?: string;
  Motivo_bloqueou?: any;
};

interface Props {
  resposta: Resposta | null;
}

function RespostaWidget({ resposta }: Props) {
  const [abaAtiva, setAbaAtiva] = useState("Criticidade");

  if (!resposta) return null;

  // Define cor da borda conforme Status
  const borderStatus =
    resposta.Status === "SIM" ? "border-green-600" : "border-red-600";
const corMarcador =
    resposta.Status === "SIM" ? "after:bg-green-600" : "after:bg-red-600";
const corTexto =
    resposta.Status === "SIM" ? "text-green-600" : "text-red-600";

  return (
    <div
      className={`w-full max-w-3xl mt-6 mx-auto rounded-md shadow border-[3px] ${borderStatus}`}
    >
      {/* Menu de abas */}
      <div className="flex justify-center space-x-6 border-b bg-gray-100 rounded-t-md">
        {["Criticidade", "Linhas", "Motivação"].map((aba) => (
          <button
            key={aba}
            onClick={() => setAbaAtiva(aba)}
            className={`relative py-3 px-6 font-medium transition-colors duration-200 
              focus:outline-none border-none
              ${abaAtiva === aba
                ? `${corTexto} after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[3px] ${corMarcador}`
                : `text-black hover:${corTexto}`}`}
          >
            {aba}
          </button>
        ))}
      </div>

      {/* Conteúdo da aba */}
      <div className="p-4 bg-gray-100 rounded-b-md text-black">
        {abaAtiva === "Criticidade" && (
          <div>
            <p><strong>Status:</strong> {resposta.Status}</p>
            <p><strong>Validação:</strong> {resposta.Validacao}</p>
            <p><strong>Índice:</strong> {resposta.Indice}</p>
            <p><strong>Criticidade:</strong> {resposta.Criticidade}</p>
            <p><strong>Questionamento:</strong> {resposta.Questionamento}</p>
            <p><strong>Pessoalidade:</strong> {resposta.Pessoalidade}</p>
            <p><strong>Impessoalidade:</strong> {resposta.Impessoalidade}</p>
          </div>
        )}

        {abaAtiva === "Linhas" && (
          <div className="space-y-2">
            {resposta.Linhas?.map((linha, idx) => (
              <div key={idx} className="p-2 border rounded bg-white text-black">
                <p><strong>Linha:</strong> {linha.linha}</p>
                <p><strong>Status:</strong> {linha.status}</p>
                {linha.motivo && <p><strong>Motivo:</strong> {linha.motivo}</p>}
              </div>
            ))}
          </div>
        )}

        {abaAtiva === "Motivação" && (
          <div>
            <p><strong>Motivo geral:</strong> {resposta.Motivo || "Nenhum"}</p>
            <pre className="text-sm whitespace-pre-wrap text-black">
              {JSON.stringify(resposta.Motivo_bloqueou, null, 2)}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default RespostaWidget;
