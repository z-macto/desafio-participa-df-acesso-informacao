// src/documentacao/DocumentacaoInstalacao.tsx

function DocumentacaoInstalacao() {
  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Guia de Instalação</h2>
      <p className="mb-6">
        Siga os passos abaixo para configurar o ambiente e instalar as
        dependências do projeto.
      </p>

      <ol className="space-y-4 list-decimal list-inside text-sm">
        <li>
          <strong>Clonar o Repositório:</strong>
          <pre className="bg-gray-100 p-2 rounded mt-1 text-xs">
            git clone
            https://github.com/z-macto/desafio-participa-df-acesso-informacao
            {"\n"}
            cd motor-pii
          </pre>
        </li>

        <li>
          <strong>Criar Ambiente Virtual:</strong>
          <pre className="bg-gray-100 p-2 rounded mt-1 text-xs">
            python -m venv venv
          </pre>
        </li>

        <li>
          <strong>Ativar Ambiente Virtual:</strong>
          <div className="mt-1">
            <p className="mb-1">Windows:</p>
            <pre className="bg-gray-100 p-2 rounded text-xs">
              venv\Scripts\activate
            </pre>
            <p className="mt-2 mb-1">Linux/macOS:</p>
            <pre className="bg-gray-100 p-2 rounded text-xs">
              source venv/bin/activate
            </pre>
          </div>
        </li>

        <li>
          <strong>Instalar Dependências:</strong>
          <pre className="bg-gray-100 p-2 rounded mt-1 text-xs">
            pip install -r requirements.txt
          </pre>
        </li>
      </ol>
    </div>
  );
}

export default DocumentacaoInstalacao;
