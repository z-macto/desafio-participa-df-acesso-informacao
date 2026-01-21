import './App.css'
import Cabecalho from './componentes/Cabecalho' 
import Rodape from './componentes/Rodape'
import TelaPrincipal from './componentes/TelaPrincipal' 

function App() {
  return (
     <div className="bg-white min-h-screen">
      <Cabecalho /> 
      <TelaPrincipal /> 
      <Rodape/>
     </div>
  )
}

export default App
