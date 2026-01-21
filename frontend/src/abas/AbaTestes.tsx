import  { useEffect, useState } from "react";

function Testes() {
  const [dados, setDados] = useState<any>(null);
  const [erro, setErro] = useState<string | null>(null);

  useEffect(() => {
    const fetchDados = async () => {
      try {
        const response = await fetch("/api/testes");
        if (response.ok) {
          const data = await response.json();
          setDados(data.resposta);
          console.log(data.resposta);
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
      <div className="overflow-x-auto mt-6">
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
              const corFundo =
                res.Status === "SIM" ? "bg-green-100" : "bg-red-100";
              return (
                <tr key={idx} className={`${corFundo} hover:opacity-80`}>
                  <td className="px-4 py-2 border-b">{res.Retorno}</td>
                  <td className="px-4 py-2 border-b">{res.Validacao}</td>
                  <td className="px-4 py-2 border-b">{res.Indice}</td>
                  <td className="px-4 py-2 border-b">{res.Criticidade}</td>
                  <td className="px-4 py-2 border-b font-bold">{res.Status}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Testes;
