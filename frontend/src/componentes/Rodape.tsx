
function Rodape() {
  return (
    <footer className="w-full bg-blue-600 py-4 px-6 flex justify-between items-center">
      {/* Texto à esquerda */}
      <span className="text-sm text-white">
         <a
          href="https://github.com/z-macto/desafio-participa-df-acesso-informacao"
          className="text-white no-underline hover:text-white focus:text-white"
        >
        Desenvolvido por Equipe z-macto
        </a>
      </span>

      {/* Texto à direita */}
      <span className="text-sm text-right">
        <a
          href="https://www.economia.df.gov.br/w/1-hackathon-em-controle-social-desafio-participa-df"
          className="text-white no-underline hover:text-white focus:text-white"
        >
          Desafio Participa DF - Controladoria-Geral do Distrito Federal
        </a>
      </span>
    </footer>
  );
}

export default Rodape;
