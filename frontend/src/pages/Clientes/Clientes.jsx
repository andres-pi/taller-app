import { NavLink } from "react-router-dom"
import { MoreHorizontal, Plus, Search } from "lucide-react"
import { useClientes } from "../../hooks/Clientes/useClientes"
import "./Clientes.css"

export const Clientes = () => {
    
    const {
        clientes,
        cargando,
        error
    } = useClientes()

    return (
        <section className="clientes">
            <div className="clientes__header">
                <div>
                    <h1>Clientes</h1>

                    <p>
                        Gestioná los clientes registrados en el taller.
                    </p>
                </div>

                <button className="clientes__create">
                    <Plus size={17} />
                    Nuevo cliente
                </button>
            </div>

            <div className="clientes__panel">
                <div className="clientes__toolbar">
                    <div className="clientes__search">
                        <Search size={17} />

                        <input
                            type="text"
                            placeholder="Buscar cliente..."
                        />
                    </div>
                </div>

                {cargando && (
                    <div className="clientes__message">
                        Cargando clientes...
                    </div>
                )}

                {error && (
                    <div className="clientes__message clientes__message--error">
                        {error}
                    </div>
                )}

                {!cargando && !error && (
                    <div className="clientes__table">
                        <div className="clientes__row clientes__row--header">
                            <span>Cliente</span>
                            <span>Teléfono</span>
                            <span>Email</span>
                            <span>Registro</span>
                            <span></span>
                        </div>

                        {clientes.map((cliente) => (
                            <div
                                className="clientes__row"
                                key={cliente.id}
                            >
                                <div className="clientes__name">
                                    <div className="clientes__avatar">
                                        {cliente.nombre[0]}
                                        {cliente.apellido[0]}
                                    </div>

                                    <div>
                                        <strong>
                                            {cliente.nombre}{" "}
                                            {cliente.apellido}
                                        </strong>

                                        <span>
                                            ID #{cliente.id}
                                        </span>
                                    </div>
                                </div>

                                <span>
                                    {cliente.telefono}
                                </span>

                                <span>
                                    {cliente.email || "—"}
                                </span>

                                <span>
                                    —
                                </span>

                                <button className="clientes__action">
                                    <MoreHorizontal size={18} />
                                </button>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </section>
    )
}
