// src/documentacao/DocumentacaoArquitetura.tsx
import {
  CpuChipIcon,
  ArrowPathIcon,
  ServerStackIcon,
  GlobeAltIcon,
} from "@heroicons/react/24/outline";

function DocumentacaoArquitetura() {
  const cards = [
    {
      icon: CpuChipIcon,
      titulo: "Frontend com React + Vite",
      descricao:
        "Interface moderna e responsiva construída com React e empacotada com Vite para alto desempenho.",
    },
    {
      icon: ArrowPathIcon,
      titulo: "API REST Assíncrona",
      descricao:
        "Comunicação entre frontend e backend via chamadas HTTPS assíncronas, garantindo agilidade e escalabilidade.",
    },
    {
      icon: ServerStackIcon,
      titulo: "Backend em Python + FastAPI",
      descricao:
        "Camada lógica e de processamento construída com FastAPI, oferecendo alta performance e validação automática.",
    },
    {
      icon: GlobeAltIcon,
      titulo: "Estrutura Lógica Integrada",
      descricao:
        "Todos os componentes se conectam de forma fluida, formando uma arquitetura modular e escalável.",
    },
  ];

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Arquitetura do Sistema</h2>
      <p className="mb-6">
        A arquitetura do sistema foi projetada para ser leve, escalável e de
        fácil manutenção, conectando o frontend ao backend via API assíncrona.
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

export default DocumentacaoArquitetura;
