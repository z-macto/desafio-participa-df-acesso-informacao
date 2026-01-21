// src/documentacao/DocumentacaoVisaoGeral.tsx

function DocumentacaoExecucao() {
  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Guia de Execução</h2>
      <p className="mb-6">
        Siga os passos abaixo para iniciar a execução da aplicação.
      </p>

      <ol className="space-y-4 list-decimal list-inside text-sm">
        <li>
          <strong>Iniciar Aplicação</strong>
          <pre className="bg-gray-100 p-2 rounded mt-1 text-xs">
            python app.py
          </pre>
        </li>
      </ol>
    </div>
  );
}

export default DocumentacaoExecucao;
