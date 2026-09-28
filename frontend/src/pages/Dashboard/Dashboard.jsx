import {
    Users,
    Monitor,
    Wrench,
    ClipboardList,
    ArrowUpRight,
} from 'lucide-react'
import './Dashboard.css'

export const Dashboard = () => {
    return (
        <section className="dashboard">
            <div className="dashboard__header">
                <div>
                    <h1>Dashboard</h1>

                    <p>
                        Resumen general del taller.
                    </p>
                </div>

                <span className="dashboard__date">
                    Hoy, 27 de septiembre
                </span>
            </div>

            <div className="dashboard__stats">
                <article className="stat-card">
                    <div className="stat-card__top">
                        <span className="stat-card__label">
                            Clientes
                        </span>

                        <Users size={19} />
                    </div>

                    <strong className="stat-card__value">
                        128
                    </strong>

                    <span className="stat-card__detail">
                        Clientes registrados
                    </span>
                </article>

                <article className="stat-card">
                    <div className="stat-card__top">
                        <span className="stat-card__label">
                            Equipos
                        </span>

                        <Monitor size={19} />
                    </div>

                    <strong className="stat-card__value">
                        164
                    </strong>

                    <span className="stat-card__detail">
                        Equipos registrados
                    </span>
                </article>

                <article className="stat-card">
                    <div className="stat-card__top">
                        <span className="stat-card__label">
                            En reparación
                        </span>

                        <Wrench size={19} />
                    </div>

                    <strong className="stat-card__value">
                        12
                    </strong>

                    <span className="stat-card__detail">
                        Órdenes activas
                    </span>
                </article>

                <article className="stat-card">
                    <div className="stat-card__top">
                        <span className="stat-card__label">
                            Entregadas
                        </span>

                        <ClipboardList size={19} />
                    </div>

                    <strong className="stat-card__value">
                        37
                    </strong>

                    <span className="stat-card__detail">
                        Este mes
                    </span>
                </article>
            </div>

            <div className="dashboard__grid">
                <section className="dashboard-panel">
                    <div className="dashboard-panel__header">
                        <div>
                            <h2>Órdenes recientes</h2>
                            <p>
                                Últimas órdenes ingresadas al taller.
                            </p>
                        </div>

                        <button className="dashboard-panel__link">
                            Ver todas
                            <ArrowUpRight size={15} />
                        </button>
                    </div>

                    <div className="orders-table">
                        <div className="orders-table__row orders-table__row--header">
                            <span>Orden</span>
                            <span>Cliente</span>
                            <span>Equipo</span>
                            <span>Estado</span>
                        </div>

                        <div className="orders-table__row">
                            <span>#00124</span>
                            <span>María González</span>
                            <span>Notebook Lenovo</span>
                            <span className="status status--repair">
                                En reparación
                            </span>
                        </div>

                        <div className="orders-table__row">
                            <span>#00123</span>
                            <span>Juan Pérez</span>
                            <span>PC de escritorio</span>
                            <span className="status status--diagnosis">
                                Diagnóstico
                            </span>
                        </div>

                        <div className="orders-table__row">
                            <span>#00122</span>
                            <span>Laura Martínez</span>
                            <span>PlayStation 5</span>
                            <span className="status status--ready">
                                Reparada
                            </span>
                        </div>

                        <div className="orders-table__row">
                            <span>#00121</span>
                            <span>Carlos López</span>
                            <span>Monitor Samsung</span>
                            <span className="status status--pending">
                                Pendiente
                            </span>
                        </div>
                    </div>
                </section>

                <section className="dashboard-panel dashboard-panel--activity">
                    <div className="dashboard-panel__header">
                        <div>
                            <h2>Actividad reciente</h2>
                            <p>
                                Últimos movimientos.
                            </p>
                        </div>
                    </div>

                    <div className="activity-list">
                        <div className="activity">
                            <div className="activity__indicator" />

                            <div>
                                <strong>
                                    Orden #00124 actualizada
                                </strong>

                                <span>
                                    Hace 12 minutos
                                </span>
                            </div>
                        </div>

                        <div className="activity">
                            <div className="activity__indicator" />

                            <div>
                                <strong>
                                    Nuevo cliente registrado
                                </strong>

                                <span>
                                    Hace 35 minutos
                                </span>
                            </div>
                        </div>

                        <div className="activity">
                            <div className="activity__indicator" />

                            <div>
                                <strong>
                                    Orden #00122 reparada
                                </strong>

                                <span>
                                    Hace 1 hora
                                </span>
                            </div>
                        </div>

                        <div className="activity">
                            <div className="activity__indicator" />

                            <div>
                                <strong>
                                    Nuevo equipo registrado
                                </strong>

                                <span>
                                    Hace 2 horas
                                </span>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </section>
    )
}
