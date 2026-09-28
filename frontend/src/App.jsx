import { Routes, Route, Navigate } from 'react-router-dom'
import { Sidebar } from './components/Sidebar/Sidebar.jsx'
import { Header } from './components/Header/Header.jsx'
import { Dashboard } from './pages/Dashboard/Dashboard.jsx'
import { Clientes } from './pages/Clientes/Clientes.jsx'
import './App.css'

export const App = () => {
  return (
    <div className='app'>

      <Sidebar />

      <div className="app__main">
        <Header />

        <main className="app__content">
          <Routes>

            {/* Ruta Principal: Dashbaord / Inicio */}
            <Route path='/' element={<Navigate to='/dashboard' replace />} />
            <Route path='/dashboard' element={<Dashboard />} />

            {/* Rutas del módulo Clientes */}
            <Route path='/clientes' element={<Clientes />} />

          </Routes>
        </main>
      </div>

    </div>
  )
}

