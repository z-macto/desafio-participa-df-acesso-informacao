import { useState } from "react";
import RespostaWidget from "../componentes/RespostaWidget";
import API from "../API";

function AbaPedidoInformacao() {
  const [texto, setTexto] = useState("");
  const [resposta, setResposta] = useState<any>(null);

  const api = new API();
  const handleSolicitar = async () => {
    try {
      const apiUrl = await api.getApiUrl(); // pega a URL do config.json
      const response = await fetch(`${apiUrl}/api/solicitar_analise`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ solicitacao: texto }),
      });
      if (response.ok) {
        const data = await response.json();
        setResposta(data.resposta);
        setTexto("");
      } else {
        setResposta({
          Status: "Erro",
          Validacao: "Erro ao enviar solicitação",
        });
      }
    } catch (error) {
      console.error(error);
      setResposta({ Status: "Erro", Validacao: "Falha na requisição" });
    }
  };

  return (
    <div className="flex flex-col items-start gap-6">
      {/* Caixa de texto */}
      <div className="w-full max-w-3xl mt-6 mx-auto sem_cursor">
        <textarea
          rows={6}
          placeholder="Digite aqui sua solicitação..."
          value={texto}
          onChange={(e) => setTexto(e.target.value)}
          className="com_cursor w-full bg-white border border-gray-300 rounded-md p-4 text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-600 resize-none"
        />
      </div>

      {/* Botão Solicitar */}
      <div className="w-full max-w-3xl mt-4 mx-auto flex justify-center">
        <button
          className="bg-blue-600 text-white px-6 py-2 rounded-md hover:bg-blue-700 transition-colors sem_cursor"
          onClick={handleSolicitar}
        >
          Solicitar
        </button>
      </div>

      {/* Componente de resposta */}
      <RespostaWidget resposta={resposta} />
    </div>
  );
}

export default AbaPedidoInformacao;
