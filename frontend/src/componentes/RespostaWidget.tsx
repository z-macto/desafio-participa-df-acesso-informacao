import { useState } from "react";

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
      className={`w-full max-w-3xl mt-6 mx-auto rounded-md shadow border-[3px] ${borderStatus} sem_cursor`}
    >
      {/* Menu de abas */}
      <div className="flex justify-center space-x-6 border-b bg-gray-100 rounded-t-md">
        {["Criticidade", "Linhas", "Motivação"].map((aba) => (
          <button
            key={aba}
            onClick={() => setAbaAtiva(aba)}
            className={`relative py-3 px-6 font-medium transition-colors duration-200 
              focus:outline-none border-none
              ${
                abaAtiva === aba
                  ? `${corTexto} after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[3px] ${corMarcador}`
                  : `text-black hover:${corTexto}`
              }`}
          >
            {aba}
          </button>
        ))}
      </div>

      {/* Conteúdo da aba */}
      <div className="p-4 bg-gray-100 rounded-b-md text-black">
        {abaAtiva === "Criticidade" && (
          <div className="p-4 border rounded-lg bg-gray-50 shadow-md space-y-2 text-sm text-black">
            {/* Status com destaque */}

            {/* Validação */}
            <div className="flex gap-2">
              <strong className="text-black">Validação:</strong>
              <span>{resposta.Validacao}</span>
            </div>

            {/* Índice */}
            <div className="flex gap-2">
              <strong className="text-black">Índice:</strong>
              <span>{resposta.Indice}</span>
            </div>

            {/* Criticidade */}
            <div className="flex gap-2">
              <strong className="text-black">Criticidade:</strong>
              <span>{resposta.Criticidade}</span>
            </div>

            {/* Questionamento */}
            <div className="flex gap-2">
              <strong className="text-black">Questionamento:</strong>
              <span>{resposta.Questionamento}</span>
            </div>

            {/* Pessoalidade */}
            <div className="flex gap-2">
              <strong className="text-black">Pessoalidade:</strong>
              <span>{resposta.Pessoalidade}</span>
            </div>

            {/* Impessoalidade */}
            <div className="flex gap-2">
              <strong className="text-black">Impessoalidade:</strong>
              <span>{resposta.Impessoalidade}</span>
            </div>

            {/* Linha do tempo horizontal */}
            <div className="mt-6 flex items-center justify-between">
              {[
                { label: "Criticidade", value: resposta.Criticidade },
                { label: "Pessoalidade", value: resposta.Pessoalidade },
              ].map((item, idx) => (
                <div key={idx} className="flex flex-col items-center flex-1">
                  {/* Círculo */}
                  <div
                    className={`w-6 h-6 rounded-full border-2 ${
                      item.value > 0
                        ? "bg-red-500 border-red-600"
                        : "bg-green-500 border-green-600"
                    }`}
                  ></div>
                  {/* Label */}
                  <span className="mt-2 text-xs text-black">{item.label}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {abaAtiva === "Linhas" && (
          <div className="space-y-2">
            {resposta.Linhas?.map((linha, idx) => (
              <div
                key={idx}
                className="p-2 border rounded bg-white text-black space-y-1"
              >
                {/* Linha */}
                <div className="flex gap-2">
                  <strong>Linha:</strong>
                  <span>{linha.linha}</span>
                </div>

                {/* Status */}
                <div className="flex gap-2">
                  <strong>Status:</strong>
                  <span>{linha.status}</span>
                </div>

                {/* Motivo (se existir) */}
                {linha.motivo && (
                  <div className="flex gap-2">
                    <strong>Motivo:</strong>
                    <span>{linha.motivo}</span>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}

        {abaAtiva === "Motivação" && (
          <div>
            <p>
              <strong>Motivo geral:</strong> {resposta.Motivo || "Nenhum"}
            </p>
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
