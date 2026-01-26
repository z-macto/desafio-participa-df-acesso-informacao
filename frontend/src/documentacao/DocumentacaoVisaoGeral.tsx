// src/documentacao/DocumentacaoVisaoGeral.tsx
import {
  ShieldCheckIcon,
  DocumentTextIcon,
  GlobeAltIcon,
} from "@heroicons/react/24/outline";

function DocumentacaoVisaoGeral() {
  const cards = [
    {
      icon: ShieldCheckIcon,
      titulo: "LGPD - Lei Geral de Proteção de Dados (Lei n° 13.709/2018)",
      descricao:
        "Estabelece regras para coleta, uso e armazenamento de dados pessoais, garantindo privacidade e segurança.",
    },
    {
      icon: DocumentTextIcon,
      titulo: "LAI - Lei de Acesso à Informação (Lei n° 12.527/2011)",
      descricao:
        "Garante o direito de acesso às informações públicas, promovendo transparência e controle social.",
    },
    {
      icon: GlobeAltIcon,
      titulo: "Governança e Transparência Digital (Lei n° 14.129/2021)",
      descricao:
        "Promove boas práticas de gestão de dados e uso responsável das informações em ambientes digitais.",
    },
  ];

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Visão Geral</h2>
      <p className="mb-6">
        Esta seção apresenta leis e iniciativas fundamentais para a proteção de
        dados pessoais e a transparência pública.
      </p>

      <div className="space-y-4">
        {cards.map(({ icon: Icon, titulo, descricao }, idx) => (
          <div
            key={idx}
            className="flex items-start gap-3 p-4 rounded-lg bg-white/30 backdrop-blur-md shadow-md"
          >
            <Icon className="h-6 w-6 text-blue-600 flex-shrink-0" />
            <div>
              <h3 className="text-lg font-semibold">{titulo}</h3>
              <p className="text-sm">{descricao}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DocumentacaoVisaoGeral;
