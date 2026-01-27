import { useEffect, useState } from "react";
import RespostaWidget from "../componentes/RespostaWidget";

function Modal({ aberto, onClose, children }: any) {
  if (!aberto) return null;
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div
        className="bg-white p-6 rounded-md shadow-lg relative"
        style={{
          width: "800px", // largura fixa
          height: "500px", // altura fixa
          maxWidth: "90%", // responsivo
          maxHeight: "90%", // responsivo
          overflowY: "auto", // scroll se passar da altura
        }}
      >
        <button
          className="absolute top-2 right-2 text-gray-600 hover:text-black"
          onClick={onClose}
        >
          ✕
        </button>
        {children}
      </div>
    </div>
  );
}

function Testes() {
  const [dados, setDados] = useState<any>(null);
  const [erro, setErro] = useState<string | null>(null);
  const [modalAberto, setModalAberto] = useState(false);
  const [itemSelecionado, setItemSelecionado] = useState<any>(null);

  useEffect(() => {
    const fetchDados = async () => {
      try {
        const response = await fetch("/api/testes");
        if (response.ok) {
          const data = await response.json();
          setDados(data.resposta);
        } else {
          setErro("Erro ao carregar dados de /api/testes");
        }
      } catch (error) {
        console.error(error);
        setErro("Falha na requisição");
      }
    };

    fetchDados();
  }, []);

  if (erro) {
    return <p className="text-red-600">{erro}</p>;
  }

  if (!dados) {
    return <p className="text-black">Carregando dados...</p>;
  }

  return (
    <div className="p-6 text-black">
      <h2 className="text-xl font-bold text-center">Testes</h2>

      {/* Resumo */}
      <div className="mt-4 text-center">
        <p>Total de entradas: {dados.TotalEntradas}</p>
        <p>Válidos: {dados.Validos}</p>
        <p>Inválidos: {dados.Invalidos}</p>
      </div>

      {/* Tabela de resultados */}
      <div className="overflow-x-auto mt-6 sem_cursor">
        <table className="min-w-full border border-gray-300 bg-white rounded-md">
          <thead>
            <tr className="bg-gray-100">
              <th className="px-4 py-2 border-b text-left">Solicitação</th>
              <th className="px-4 py-2 border-b text-left">Validação</th>
              <th className="px-4 py-2 border-b text-left">Índice</th>
              <th className="px-4 py-2 border-b text-left">Criticidade</th>
              <th className="px-4 py-2 border-b text-left">Status</th>
            </tr>
          </thead>
          <tbody>
            {dados.Resultados.map((res: any, idx: number) => {
              const badgeClasses =
                res.Status === "SIM"
                  ? "bg-green-200 text-green-800"
                  : "bg-red-200 text-red-800";

              return (
                <tr
                  key={idx}
                  className="hover:opacity-80 cursor-pointer"
                  onClick={() => {
                    setItemSelecionado(res);
                    setModalAberto(true);
                  }}
                >
                  <td className="px-4 py-2 border-b">{res.Retorno}</td>
                  <td className="px-4 py-2 border-b">{res.Validacao}</td>
                  <td className="px-4 py-2 border-b">{res.Indice}</td>
                  <td className="px-4 py-2 border-b">{res.Criticidade}</td>
                  <td className="px-4 py-2 border-b font-bold">
                    <span
                      className={`px-2 py-1 rounded-full text-sm font-semibold ${badgeClasses}`}
                    >
                      {res.Status}
                    </span>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {/* Modal com mensagem + RespostaWidget */}
      <Modal aberto={modalAberto} onClose={() => setModalAberto(false)}>
        {itemSelecionado && (
          <div className="space-y-4">
            {/* Mensagem do teste */}
            <div className="p-4 bg-gray-50 border rounded-md shadow-sm">
              <h3 className="text-lg font-bold mb-2 text-center">
                Mensagem do Teste
              </h3>
              <p className="text-black">{itemSelecionado.Mensagem}</p>
            </div>

            {/* Widget de resposta detalhada */}
            <RespostaWidget resposta={itemSelecionado} />
          </div>
        )}
      </Modal>
    </div>
  );
}

export default Testes;
