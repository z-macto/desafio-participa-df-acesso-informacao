import { useState } from "react";
import {
  HomeIcon,
  BookOpenIcon,
  CubeTransparentIcon,
  CogIcon,
  //PlayIcon,
  DocumentTextIcon,
  BeakerIcon,
  ShieldCheckIcon,
  CodeBracketIcon,
} from "@heroicons/react/24/outline";

// Importando os componentes com prefixo Documentacao
import DocumentacaoVisaoGeral from "../documentacao/DocumentacaoVisaoGeral";
import DocumentacaoGuiaAnalisar from "../documentacao/DocumentacaoGuiaAnalisar";
import DocumentacaoArquitetura from "../documentacao/DocumentacaoArquitetura";
import DocumentacaoInstalacao from "../documentacao/DocumentacaoInstalacao";
import DocumentacaoExecucao from "../documentacao/DocumentacaoExecucao";
import DocumentacaoFormatos from "../documentacao/DocumentacaoFormatos";
import DocumentacaoMetodologia from "../documentacao/DocumentacaoMetodologia";
import DocumentacaoSeguranca from "../documentacao/DocumentacaoSeguranca";
import DocumentacaoApi from "../documentacao/DocumentacaoApi";

const abas = [
  { id: "visao", label: "Visão Geral", icon: HomeIcon },
  { id: "guia de uso", label: "Guia de uso", icon: BookOpenIcon },
  { id: "arquitetura", label: "Arquitetura", icon: CubeTransparentIcon },
  { id: "instalacao", label: "Instalação", icon: CogIcon },
  { id: "formatos", label: "Formatos", icon: DocumentTextIcon },
  { id: "metodologia", label: "Metodologia", icon: BeakerIcon },
  { id: "seguranca", label: "Segurança", icon: ShieldCheckIcon },
  { id: "api", label: "API", icon: CodeBracketIcon },
];

function Documentacao() {
  const [abaAtiva, setAbaAtiva] = useState("visao");

  return (
    <div className="p-6 text-black">
      <h1 className="text-5xl font-bold text-center mb-6 text-black">
        Documentação
      </h1>

      {/* Menu de abas */}
      <div className="flex flex-wrap justify-center gap-4 border-b pb-2">
        {abas.map(({ id, label, icon: Icon }) => (
          <button
            key={id}
            onClick={() => setAbaAtiva(id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-md transition-colors duration-200
              ${
                abaAtiva === id
                  ? "bg-blue-600 text-white"
                  : "bg-gray-100 text-black hover:bg-blue-100"
              }`}
          >
            <Icon className="h-5 w-5" />
            <span className="text-sm font-medium">{label}</span>
          </button>
        ))}
      </div>

      {/* Conteúdo da aba */}
      <div className="mt-6 text-left max-w-3xl mx-auto">
        {abaAtiva === "visao" && <DocumentacaoVisaoGeral />}
        {abaAtiva === "guia de uso" && <DocumentacaoGuiaAnalisar />}
        {abaAtiva === "arquitetura" && <DocumentacaoArquitetura />}
        {abaAtiva === "instalacao" && <DocumentacaoInstalacao />}
        {abaAtiva === "execucao" && <DocumentacaoExecucao />}
        {abaAtiva === "formatos" && <DocumentacaoFormatos />}
        {abaAtiva === "metodologia" && <DocumentacaoMetodologia />}
        {abaAtiva === "seguranca" && <DocumentacaoSeguranca />}
        {abaAtiva === "api" && <DocumentacaoApi />}
      </div>
    </div>
  );
}

export default Documentacao;
