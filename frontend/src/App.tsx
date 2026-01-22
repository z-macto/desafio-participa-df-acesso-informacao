import { useEffect } from "react";
import "./App.css";
import Cabecalho from "./componentes/Cabecalho";
import Rodape from "./componentes/Rodape";
import TelaPrincipal from "./componentes/TelaPrincipal";

function App() {
  useEffect(() => {
    document.title = "1º Hackathon em Controle Social: Desafio Participa DF";
  }, []);

  return (
    <div className="bg-white min-h-screen">
      <Cabecalho />
      <TelaPrincipal />
      <Rodape />
    </div>
  );
}

export default App;
