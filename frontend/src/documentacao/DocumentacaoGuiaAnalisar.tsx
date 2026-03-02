// src/documentacao/DocumentacaoGuiaAnalisar.tsx

import React from 'react';

const DocumentacaoGuiaAnalisar: React.FC = () => {
  return (
    <div className="space-y-8 text-gray-800">
      
      {/* Cabeçalho */}
      <div className="border-b border-gray-200 pb-4">
        <h2 className="text-3xl font-bold text-blue-700 flex items-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
          </svg>
          Guia de Uso: Tela de Análise
        </h2>
        <p className="mt-2 text-gray-600">
          Manual operacional para utilização da ferramenta de anonimização e interpretação dos resultados processados.
        </p>
      </div>

      {/* 1. Visão Geral */}
      <section className="bg-white p-6 rounded-lg shadow-sm border-l-4 border-blue-600">
        <h3 className="text-xl font-semibold mb-4 text-gray-900">Objetivo da Tela</h3>
        <p className="mb-4 leading-relaxed">
          A tela <strong>"Pedido de Informação"</strong> é a interface principal de interação com o motor de anonimização. 
          Ela permite que o operador insira textos brutos (contendo potenciais dados pessoais) e receba instantaneamente 
          uma versão tratada (anonimizada), pronta para publicação ou auditoria.
        </p>
      </section>

      {/* 2. Fluxo de Operação */}
      <section>
        <h3 className="text-xl font-semibold mb-6 text-gray-900">2. Passo a Passo da Operação</h3>
        
        <div className="space-y-6">
          {/* Passo 1 */}
          <div className="flex gap-4">
            <div className="flex-shrink-0 w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold">1</div>
            <div>
              <h4 className="font-bold text-gray-900">Entrada de Texto</h4>
              <p className="text-sm text-gray-600 mt-1">
                No campo <code>Digite aqui sua solicitação...</code>, insira o texto integral que deve ser analisado. O sistema aceita textos 
                com múltiplas quebras de linha e caracteres especiais.
              </p>
              <div className="mt-2 bg-yellow-50 p-3 rounded text-xs text-yellow-800 border border-yellow-200">
                <strong>Dica:</strong> Para melhores resultados, evite colar cabeçalhos ou rodapés de e-mails que não façam parte do conteúdo da solicitação.
              </div>
            </div>
          </div>

          {/* Passo 2 */}
          <div className="flex gap-4">
            <div className="flex-shrink-0 w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold">3</div>
            <div>
              <h4 className="font-bold text-gray-900">Processamento</h4>
              <p className="text-sm text-gray-600 mt-1">
                Ao clicar em <strong>"Solicitar"</strong>, o texto é enviado de forma segura para o backend. 
                O motor aplica as regras de Pré-processamento, Detecção de padrões, Classificação, Cálculo de métricas e Validação geral.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* 3. Interpretando os Resultados */}
      <section className="bg-gray-50 p-6 rounded-lg border border-gray-200 mt-8">
        <h3 className="text-xl font-semibold mb-6 text-gray-900">Interpretando os Resultados</h3>

        <div className="space-y-10">
          
          {/* Cenário A: Sem Dados Pessoais */}
          <div>
            <h4 className="font-bold text-gray-800 mb-3 flex items-center gap-2">
              <span className="w-6 h-6 rounded-full bg-green-100 text-green-700 flex items-center justify-center text-xs border border-green-200 font-bold">A</span>
              Cenário: Nenhum Dado Pessoal Detectado
            </h4>
            <div className="bg-white p-4 rounded shadow-sm border-l-4 border-green-500">
              <div className="flex justify-between items-center border-b pb-2 mb-2">
                <span className="font-bold text-green-700">Resultado Seguro</span>
                <span className="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full font-semibold">Liberado</span>
              </div>
              <p className="text-sm text-gray-600 mb-3">
                O sistema analisou o texto e não encontrou dados pessoais. O texto original é preservado.
              </p>
              <div className="bg-gray-50 p-3 rounded text-sm font-mono text-gray-700 leading-relaxed border border-gray-200">
                "Solicito cópia do contrato de licitação n.º 123/2024 para análise de conformidade financeira."
              </div>
            </div>
          </div>

          {/* Divisor */}
          <hr className="border-gray-200" />

          {/* Cenário B: Com Dados Pessoais */}
          <div>
            <h4 className="font-bold text-gray-800 mb-3 flex items-center gap-2">
              <span className="w-6 h-6 rounded-full bg-yellow-100 text-yellow-700 flex items-center justify-center text-xs border border-yellow-200 font-bold">B</span>
              Cenário: Dados Pessoais Detectados
            </h4>
            <div className="bg-white p-4 rounded shadow-sm border-l-4 border-yellow-500">
              <div className="flex justify-between items-center border-b pb-2 mb-2">
                <span className="font-bold text-yellow-700">Anonimização Realizada</span>
                <span className="bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded-full font-semibold">Atenção</span>
              </div>
              <p className="text-sm text-gray-600 mb-3">
                O sistema identifica os parâmetros. A interface destaca os termos para fácil identificação.
              </p>
              <div className="bg-gray-50 p-3 rounded text-sm font-mono text-gray-700 leading-relaxed border border-gray-200">
                "Solicito a ficha funcional do servidor <span className="bg-yellow-200 text-yellow-900 px-1 rounded mx-0.5 font-bold">***</span>, matrícula <span className="bg-yellow-200 text-yellow-900 px-1 rounded mx-0.5 font-bold">***</span>."
              </div>
            </div>
          </div>

        </div>
      </section>

    </div>
  );
};

export default DocumentacaoGuiaAnalisar;