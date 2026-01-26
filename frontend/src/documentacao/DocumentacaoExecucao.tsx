// src/documentacao/DocumentacaoVisaoGeral.tsx

function DocumentacaoVisaoGeral() {
  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Guia de Execução da Aplicação</h1>
      <p className="mb-6 text-sm leading-relaxed">
        Este guia descreve como realizar o build do frontend e iniciar o backend
        da aplicação em diferentes sistemas operacionais.
      </p>

      {/* Execução no Windows */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Execução no Windows</h2>
        <p className="text-sm mb-4">
          No Windows, utilize o script em batch fornecido para automatizar o
          processo.
        </p>
        <pre className="bg-gray-100 p-3 rounded text-xs mb-4">
          {`@echo off
REM Script para build do frontend e disponibilizar em 'distribuicao'

setlocal enabledelayedexpansion

cd /d "%~dp0frontend"

echo 📦 Instalando dependências...
call npm install

echo ⚙️ Executando build do frontend...
call npm run build

cd ..

if not exist distribuicao (
    mkdir distribuicao
)

if not exist armazenamento_de_dados (
    mkdir armazenamento_de_dados
)

echo 📂 Copiando arquivos gerados para 'distribuicao'...
xcopy /E /Y frontend\\dist\\* distribuicao\\

echo ✅ Build concluído e arquivos disponíveis em 'distribuicao'.

echo ⚙️ Executando aplicação...
py backend\\app.py`}
        </pre>
        <p className="text-sm">
          Salve este conteúdo em um arquivo <code>build.bat</code> e execute-o
          clicando duas vezes ou via terminal.
        </p>
      </section>

      {/* Execução no Linux */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Execução no Linux</h2>
        <p className="text-sm mb-4">
          No Linux, utilize o script em Bash para realizar o mesmo processo.
        </p>
        <pre className="bg-gray-100 p-3 rounded text-xs mb-4">
          {`#!/bin/bash
# Script para build do frontend e disponibilizar em 'distribuicao'

set -e

cd "$(dirname "$0")/frontend"

echo "📦 Instalando dependências..."
npm install

echo "⚙️ Executando build do frontend..."
npm run build

cd ..

mkdir -p distribuicao
mkdir -p armazenamento_de_dados

echo "📂 Copiando arquivos gerados para 'distribuicao'..."
cp -r frontend/dist/* distribuicao/

echo "✅ Build concluído e arquivos disponíveis em 'distribuicao'."

echo "⚙️ Executando aplicação..."
python3 backend/app.py`}
        </pre>
        <p className="text-sm">
          Salve este conteúdo em um arquivo <code>build.sh</code>, dê permissão
          de execução com <code>chmod +x build.sh</code> e rode com
          <code> ./build.sh</code>.
        </p>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-4">Observações</h2>
        <ul className="list-disc list-inside text-sm space-y-2">
          <li>
            Certifique-se de ter <strong>Node.js</strong> e <strong>npm</strong>{" "}
            instalados para o build do frontend.
          </li>
          <li>
            Verifique se possui <strong>Python 3</strong> instalado para
            executar o backend.
          </li>
          <li>
            As pastas <code>distribuicao</code> e{" "}
            <code>armazenamento_de_dados</code> serão criadas automaticamente.
          </li>
        </ul>
      </section>
    </div>
  );
}

export default DocumentacaoVisaoGeral;
