import  { useState } from "react";
import PedidoInformacao from "../abas/AbaPedidoInformacao";
import Testes from "../abas/AbaTestes";
import CentralControle from "../abas/AbaCentralControle";
import Documentacao from "../abas/AbaDocumentacao";

function TelaPrincipal() {
  const tabs = [
    { id: "aba1", label: "Pedido de Informação" },
    { id: "aba2", label: "Testes" },
    { id: "aba3", label: "Central de Controle" },
    { id: "aba4", label: "Documentação" },
  ];

  const [activeTab, setActiveTab] = useState(tabs[0].id);

  return (
    <div className="w-full min-h-screen bg-white">
      {/* Tabs */}
      <div className="flex justify-center space-x-6 border-b bg-gray-100">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`relative py-3 px-6 font-medium transition-colors duration-200 
              focus:outline-none border-none
              ${activeTab === tab.id
                ? "text-blue-600 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[3px] after:bg-blue-600"
                : "text-gray-600 hover:text-blue-600"}`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Conteúdo */}
      <div>
        {activeTab === "aba1" && <PedidoInformacao />}
        {activeTab === "aba2" && <Testes />}
        {activeTab === "aba3" && <CentralControle />}
        {activeTab === "aba4" && <Documentacao />}
      </div>
    </div>
  );
}

export default TelaPrincipal;
