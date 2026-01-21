import { ShieldCheckIcon } from "@heroicons/react/24/solid";

function Cabecalho() {
  return (
    <header className="w-full bg-blue-600 text-white shadow-md">
      <div className="w-full px-4 py-3 flex justify-between items-center">
        
        {/* Logo com ícone de escudo */}
        <div className="flex items-center space-x-2">
          <ShieldCheckIcon className="h-8 w-8 text-white" />
          <span className="text-lg font-bold">
            1º Hackathon em Controle Social: Desafio Participa DF
          </span>
        </div>

        {/* Ícone do GitHub com link */}
        <a
          href="https://github.com/z-macto/desafio-participa-df-acesso-informacao"
          target="_blank"
          rel="noopener noreferrer"
          className="hover:text-gray-200"
        >
          {/* SVG do GitHub */}
          <svg
            className="h-8 w-8 fill-current"
            viewBox="0 0 24 24"
            aria-hidden="true"
          >
            <path
              fillRule="evenodd"
              d="M12 .5C5.65.5.5 5.65.5 12c0 5.1 3.3 9.4 7.9 10.9.6.1.8-.3.8-.6v-2.1c-3.2.7-3.9-1.5-3.9-1.5-.5-1.2-1.2-1.5-1.2-1.5-1-.7.1-.7.1-.7 1.1.1 1.7 1.1 1.7 1.1 1 .1.7 1.9 2.7 1.4.1-.8.4-1.3.7-1.6-2.6-.3-5.3-1.3-5.3-5.9 0-1.3.5-2.4 1.2-3.3-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.3 1.2a11.6 11.6 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.8.1 3.1.8.9 1.2 2 1.2 3.3 0 4.6-2.7 5.6-5.3 5.9.4.3.8 1 .8 2v3c0 .3.2.7.8.6A10.9 10.9 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5z"
            />
          </svg>
        </a>
      </div>
    </header>
  );
}

export default Cabecalho;
