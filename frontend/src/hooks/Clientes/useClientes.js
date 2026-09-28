import { useState, useEffect } from 'react'
import { clienteService } from '../../services/cliente.services'

export const useClientes = () => {

    const [clientes, setClientes] = useState([])
    const [cargando, setCargando] = useState(false)
    const [error, setError] = useState(null)

    useEffect(() => {
        const obtenerClientes = async () => {
            try {
                setCargando(true)
                const data = await clienteService.obtenerTodos()
                setClientes(data)
            } catch (error) {
                console.error(error)
                setError("No se pudieron cargar los clientes")
            } finally {
                setCargando(false)
            }
        }
        obtenerClientes()
    }, [])

    return {
        clientes,
        cargando,
        error
    }

}