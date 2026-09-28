import { api } from '../api/axios.js'

export const clienteService = {

    obtenerTodos: async () => {
        const respuesta = await api.get('/clientes')
        return respuesta.data
    },
    obtenerPorId: async (id) => {
        const respuesta = await api.get(`/clientes/${id}`)
        return respuesta.data
    },
    crear: async (payload) => {
        const respuesta = await api.post('/clientes', payload)
        return respuesta.data
    },
    actualizar: async (id, payload) => {
        const respuesta = await api.put(`/clientes/${id}/actualizar`, payload)
        return respuesta.data
    },
    editar: async (id, payload) => {
        const respuesta = await api.patch(`/clientes/${id}/editar`, payload)
    }

}