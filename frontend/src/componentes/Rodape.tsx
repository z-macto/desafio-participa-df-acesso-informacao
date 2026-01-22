import { useEffect, useState } from "react";

function Rodape() {
  const [totalSolicitacoes, setTotalSolicitacoes] = useState<number>(0);

  useEffect(() => {
    const fetchInfo = async () => {
      try {
        const response = await fetch("/api/solicitacoes/info");
        if (response.ok) {
          const data = await response.json();
          setTotalSolicitacoes(data.total_solicitacoes);
        }
      } catch (error) {
        console.error("Erro ao carregar total de solicitações:", error);
      }
    };
    fetchInfo();
  }, []);

  return (
    <footer className="w-full bg-blue-600 py-4 px-6 flex items-center text-white">
      {/* Texto à esquerda */}
      <div className="flex-1 text-sm">
        <a
          href="https://github.com/z-macto/desafio-participa-df-acesso-informacao"
          className="text-white no-underline hover:text-white focus:text-white"
        >
          Desenvolvido por Equipe z-macto
        </a>
      </div>

      {/* Texto ao centro */}
      <div className="flex-1 text-center text-sm font-semibold">
        {totalSolicitacoes} solicitações processadas
      </div>

      {/* Texto à direita */}
      <div className="flex-1 text-sm text-right">
        <a
          href="https://www.economia.df.gov.br/w/1-hackathon-em-controle-social-desafio-participa-df"
          className="text-white no-underline hover:text-white focus:text-white"
        >
          Desafio Participa DF - Controladoria-Geral do Distrito Federal
        </a>
      </div>
    </footer>
  );
}

export default Rodape;
