import { useEffect, useState } from "react";

interface Solicitacao {
  id: string;
  data: string;
  horario: string;
  analise: string; // contém JSON com campo "status"
}

function CentralControle() {
  const [solicitacoes, setSolicitacoes] = useState<Solicitacao[]>([]);
  const [pagina, setPagina] = useState<number>(1);
  const [totalPaginas, setTotalPaginas] = useState<number>(1);
  const [erro, setErro] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  // Carregar info inicial (total de páginas)
  useEffect(() => {
    const fetchInfo = async () => {
      try {
        const response = await fetch("/api/solicitacoes/info");
        if (response.ok) {
          const data = await response.json();
          setTotalPaginas(data.total_paginas);
        }
      } catch (error) {
        console.error(error);
        setErro("Falha ao carregar informações");
      }
    };
    fetchInfo();
  }, []);

  // Carregar solicitações da página atual
  useEffect(() => {
    const fetchSolicitacoes = async () => {
      setLoading(true);
      try {
        const response = await fetch(`/api/solicitacoes?pagina=${pagina}`);
        if (response.ok) {
          const data = await response.json();
          setSolicitacoes(data.solicitacoes);
        } else {
          setErro("Erro ao carregar solicitações");
        }
      } catch (error) {
        console.error(error);
        setErro("Falha na requisição");
      } finally {
        setLoading(false);
      }
    };
    fetchSolicitacoes();
  }, [pagina]);

  if (erro) {
    return <p className="text-red-600">{erro}</p>;
  }

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold text-blue-600 text-center">
        Central de Controle
      </h2>

      {loading ? (
        <p className="text-gray-500 text-center mt-4">
          Carregando solicitações...
        </p>
      ) : (
        <div className="overflow-x-auto mt-6">
          <table className="min-w-full border border-gray-300 bg-white rounded-md text-black">
            <thead>
              <tr className="bg-gray-100">
                <th className="px-4 py-2 border-b text-left">ID</th>
                <th className="px-4 py-2 border-b text-left">Data</th>
                <th className="px-4 py-2 border-b text-left">Horário</th>
                <th className="px-4 py-2 border-b text-left">Status</th>
              </tr>
            </thead>
            <tbody>
              {solicitacoes.map((s) => {
                let status = "";
                try {
                  const analiseJson = JSON.parse(s.analise);
                  status = analiseJson.resposta?.Status || "N/A";
                } catch {
                  status = "Inválido";
                }

                const badgeClasses =
                  status === "SIM"
                    ? "bg-green-200 text-green-800"
                    : "bg-red-200 text-red-800";

                return (
                  <tr key={s.id} className="hover:bg-gray-50">
                    <td className="px-4 py-2 border-b">{s.id}</td>
                    <td className="px-4 py-2 border-b">{s.data}</td>
                    <td className="px-4 py-2 border-b">{s.horario}</td>
                    <td className="px-4 py-2 border-b">
                      <span
                        className={`px-2 py-1 rounded-full text-sm font-semibold ${badgeClasses}`}
                      >
                        {status}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      {/* Paginação */}
      <div className="flex justify-center items-center gap-2 mt-4">
        <button
          disabled={pagina <= 1}
          onClick={() => setPagina(pagina - 1)}
          className="px-3 py-1 bg-gray-200 rounded disabled:opacity-50"
        >
          Anterior
        </button>
        <span>
          Página {pagina} de {totalPaginas}
        </span>
        <button
          disabled={pagina >= totalPaginas}
          onClick={() => setPagina(pagina + 1)}
          className="px-3 py-1 bg-gray-200 rounded disabled:opacity-50"
        >
          Próxima
        </button>
      </div>
    </div>
  );
}

export default CentralControle;
