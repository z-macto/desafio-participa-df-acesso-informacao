// src/documentacao/DocumentacaoVisaoGeral.tsx
import { CalculatorIcon } from "@heroicons/react/16/solid";

function DocumentacaoMetodologia() {
  const cards = [
    {
      titulo: "Criticidade",
      cor: "red",
      descricao:
        "A criticidade mede a gravidade da solicitação, combinando a presença de termos sensíveis, verbos de solicitação e contexto pessoal. Quanto maior o valor, mais arriscada é a linha analisada.",
    },
    {
      titulo: "Questionamento",
      cor: "red",
      descricao:
        "O questionamento avalia a proporção de linhas que contêm solicitações. Indica o quanto o texto está orientado a pedir informações ou ações.",
    },
    {
      titulo: "Pessoalidade",
      cor: "red",
      descricao:
        "A pessoalidade calcula a relação entre termos sensíveis e o total de linhas. Mostra o quanto o pedido envolve dados pessoais diretamente.",
    },
    {
      titulo: "Impessoalidade",
      cor: "red",
      descricao:
        "A impessoalidade é o complemento da pessoalidade (1 - pessoalidade). Indica o quanto o pedido se mantém distante de dados pessoais.",
    },
    {
      titulo: "Índice Final",
      cor: "red",
      descricao:
        "O índice final consolida criticidade, questionamento e pessoalidade em um único valor. Ele representa a avaliação global do pedido, ponderando risco e contexto.",
    },
  ];

  return (
    <div>
      {/* Card principal explicando o motor */}
      <div className="max-w-2xl mx-auto mt-8 p-6 bg-white rounded-lg shadow-md border-l-4 border-green-600">
        {/* Cabeçalho */}
        <div className="flex items-center gap-3 mb-4">
          <div className="bg-green-100 p-2 rounded-full">
            <CalculatorIcon className="h-6 w-6 text-green-600" />
          </div>
          <div>
            <h2 className="text-lg font-semibold text-green-700">
              Algoritmo de validação de solicitação de informações
            </h2>
            <span className="text-xs font-bold text-white bg-green-600 px-2 py-1 rounded">
              MOTOR
            </span>
          </div>
        </div>

        {/* Explicação do Motor */}
        <h3 className="text-green-700 font-semibold mb-2">
          Como funciona o algoritmo do Motor de Análise
        </h3>
        <p className="text-sm text-gray-700 leading-relaxed text-justify mb-2">
          O motor foi desenvolvido para avaliar solicitações de forma
          automática, identificando se um texto contém elementos que
          caracterizam dados pessoais ou pedidos inválidos. O processo segue
          estas etapas principais:
        </p>
        <ul className="list-disc pl-6 space-y-1 text-sm text-gray-700 text-justify">
          <li>
            <strong>Pré-processamento:</strong> o conteúdo é dividido em linhas
            e normalizado (remoção de espaços, acentos e padronização).
          </li>
          <li>
            <strong>Detecção de padrões:</strong> identifica verbos e
            substantivos de solicitação, contexto jurídico e termos sensíveis.
          </li>
          <li>
            <strong>Classificação:</strong> se uma linha contém solicitação
            junto com termo sensível, ela é marcada como inválida; caso
            contrário, é aceitável.
          </li>
          <li>
            <strong>Cálculo de métricas:</strong> gera valores de criticidade,
            questionamento, pessoalidade e impessoalidade, além de um índice
            final.
          </li>
          <li>
            <strong>Validação geral:</strong> se qualquer linha for inválida, o
            pedido é classificado como não aceitável; caso contrário, é válido.
          </li>
        </ul>
        <p className="text-sm text-gray-700 leading-relaxed text-justify mt-2">
          O resultado é um relatório completo com métricas, status e motivos,
          permitindo uma análise clara e objetiva das solicitações.
        </p>
      </div>

      {/* Cards dos índices */}
      <div className="max-w-4xl mx-auto mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
        {cards.map((card, idx) => (
          <div
            key={idx}
            className={`w-full p-6 bg-white rounded-lg shadow-md border-l-4 border-${card.cor}-600`}
          >
            {/* Cabeçalho */}
            <div className="flex items-center gap-3 mb-4">
              <div className={`bg-${card.cor}-100 p-2 rounded-full`}>
                <CalculatorIcon className={`h-6 w-6 text-${card.cor}-600`} />
              </div>
              <div>
                <h2 className={`text-lg font-semibold text-${card.cor}-700`}>
                  {card.titulo}
                </h2>
                <span
                  className={`text-xs font-bold text-white bg-${card.cor}-600 px-2 py-1 rounded`}
                >
                  MOTOR
                </span>
              </div>
            </div>

            {/* Conteúdo */}
            <p className="text-sm text-gray-700 leading-relaxed text-justify">
              {card.descricao}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DocumentacaoMetodologia;
