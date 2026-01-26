// src/documentacao/DocumentacaoVisaoGeral.tsx

function DocumentacaoSeguranca() {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4 text-red-700">
        Segurança e Configuração do Motor
      </h2>
      <p className="mb-6 text-sm leading-relaxed text-gray-700">
        O sistema foi projetado para analisar solicitações de forma segura e
        precisa, utilizando detectores de padrões, análise semântica e
        configuração flexível por meio de arquivos de parâmetros.
      </p>

      <section className="mb-6">
        <h3 className="text-xl font-semibold mb-2 text-red-600">
          Detectores de Padrões com REGEX
        </h3>
        <p className="text-sm text-gray-700 leading-relaxed">
          Expressões regulares (REGEX) são aplicadas para identificar documentos
          como CPF, RG, telefones, e-mails e processos SEI. Isso garante que
          dados pessoais sejam automaticamente reconhecidos e rastreados.
        </p>
      </section>

      <section className="mb-6">
        <h3 className="text-xl font-semibold mb-2 text-red-600">
          Parser Semântico
        </h3>
        <p className="text-sm text-gray-700 leading-relaxed">
          O motor realiza um parser das frases em português, obedecendo à
          semântica do idioma. Ele detecta verbos que indicam solicitações,
          frases interrogativas que pedem informações e termos sensíveis
          relacionados a dados pessoais.
        </p>
      </section>

      <section className="mb-6">
        <h3 className="text-xl font-semibold mb-2 text-red-600">
          Análise de Solicitações e Termos Sensíveis
        </h3>
        <p className="text-sm text-gray-700 leading-relaxed">
          São identificados verbos de solicitação (como "solicitar", "pedir") e
          substantivos relacionados, além de termos proibidos ou sensíveis. Essa
          análise permite classificar se uma linha é aceitável ou inválida.
        </p>
      </section>

      <section className="mb-6">
        <h3 className="text-xl font-semibold mb-2 text-red-600">
          Conjugador e Lista de Verbos
        </h3>
        <p className="text-sm text-gray-700 leading-relaxed">
          O sistema conta com um conjugador de verbos regulares e uma lista
          pré-definida de verbos irregulares. Isso assegura que diferentes
          formas verbais sejam corretamente reconhecidas durante a análise
          semântica.
        </p>
      </section>

      <section className="mb-6">
        <h3 className="text-xl font-semibold mb-2 text-red-600">
          Arquivos de Parâmetros
        </h3>
        <p className="text-sm text-gray-700 leading-relaxed">
          A aplicação utiliza diversos arquivos de parâmetros de entrada para
          configurar o motor de avaliação. Esses arquivos permitem definir:
        </p>
        <ul className="list-disc pl-6 space-y-1 text-sm text-gray-700">
          <li>Lista de termos sensíveis (ex.: CPF, RG, dados cadastrais).</li>
          <li>Verbos regulares e suas conjugações.</li>
          <li>Verbos irregulares já mapeados.</li>
          <li>Termos e substantivos de solicitação.</li>
          <li>Parâmetros jurídicos para detectar contexto legal.</li>
        </ul>
        <p className="text-sm text-gray-700 leading-relaxed mt-2">
          Essa configuração modular garante flexibilidade e permite adaptar o
          motor conforme novas regras ou necessidades de segurança.
        </p>
      </section>

      <p className="text-sm text-gray-700 leading-relaxed mt-4">
        Combinando detectores de padrões, parser semântico e arquivos de
        configuração, o sistema oferece uma camada robusta de segurança e
        validação automática das solicitações.
      </p>
    </div>
  );
}

export default DocumentacaoSeguranca;
