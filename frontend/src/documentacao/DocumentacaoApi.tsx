// src/documentacao/DocumentacaoVisaoGeral.tsx

function DocumentacaoApi() {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Visão Geral das APIs</h2>
      <p className="mb-6 text-sm leading-relaxed">
        O sistema disponibiliza um conjunto de APIs REST que permitem analisar
        textos, executar testes, consultar estatísticas e gerenciar solicitações
        armazenadas. Abaixo estão descritas as principais rotas.
      </p>

      {/* API de Análise */}
      <section className="mb-8">
        <h3 className="text-xl font-semibold mb-3">1. Solicitar Análise</h3>
        <p className="text-sm mb-2">
          Rota: <code>POST /api/solicitar_analise</code>
        </p>
        <p className="text-sm mb-2">
          Entrada: JSON com o campo <code>solicitacao</code> (texto a ser
          analisado).
        </p>
        <p className="text-sm mb-2">
          Saída: Objeto JSON com resultado da análise, incluindo documentos,
          métricas e status.
        </p>
      </section>

      {/* API de Testes */}
      <section className="mb-8">
        <h3 className="text-xl font-semibold mb-3">2. Executar Testes</h3>
        <p className="text-sm mb-2">
          Rota: <code>GET /api/testes</code>
        </p>
        <p className="text-sm mb-2">
          Executa testes em massa sobre textos pré-definidos e retorna um resumo
          em JSON.
        </p>
      </section>

      {/* API de Estatísticas */}
      <section className="mb-8">
        <h3 className="text-xl font-semibold mb-3">
          3. Estatísticas de 30 dias
        </h3>
        <p className="text-sm mb-2">
          Rota: <code>GET /api/estatisticas_30dias</code>
        </p>
        <p className="text-sm mb-2">
          Retorna estatísticas de solicitações registradas nos últimos 30 dias,
          agrupadas por dia.
        </p>
      </section>

      {/* API de Informações de Solicitações */}
      <section className="mb-8">
        <h3 className="text-xl font-semibold mb-3">
          4. Informações de Solicitações
        </h3>
        <p className="text-sm mb-2">
          Rota: <code>GET /api/solicitacoes/info</code>
        </p>
        <p className="text-sm mb-2">
          Retorna o total de solicitações armazenadas e o número de páginas
          disponíveis.
        </p>
      </section>

      {/* API de Listagem de Solicitações */}
      <section>
        <h3 className="text-xl font-semibold mb-3">5. Listar Solicitações</h3>
        <p className="text-sm mb-2">
          Rota: <code>GET /api/solicitacoes</code>
        </p>
        <p className="text-sm mb-2">
          Parâmetro opcional: <code>pagina</code> (default = 1).
        </p>
        <p className="text-sm mb-2">
          Retorna uma lista de solicitações referentes à página informada.
        </p>
      </section>
    </div>
  );
}

export default DocumentacaoApi;
