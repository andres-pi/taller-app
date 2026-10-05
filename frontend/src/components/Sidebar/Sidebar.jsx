import { NavLink } from "react-router-dom"
import {
    LayoutDashboard,
    Users,
    Monitor,
    Wrench,
    ClipboardList,
    Settings,
} from "lucide-react"
import "./Sidebar.css"

export const Sidebar = () => {

    const menuItems = [
        { path: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
        { path: '/clientes', label: 'Clientes', icon: Users },
        { path: '/equipos', label: 'Equipos', icon: Monitor },
        { path: '/ordenes', label: 'Órdenes', icon: Wrench },
        { path: '/actividades', label: 'Actividades', icon: ClipboardList },
        { path: '/configuracion', label: 'Configuración', icon: Settings }
    ]

    return (
        <aside className="sidebar">
            <div className="sidebar__brand">
                <div className="brand-logo">T</div>
                <div className="brand-text">
                    <h2>Taller APP</h2>
                </div>
            </div>

            <nav className="sidebar__menu">
                {menuItems.map((item) => {
                    const IconComponent = item.icon
                    return (
                        <NavLink
                            key={item.path}
                            to={item.path}
                            className={({ isActive }) => `menu-btn ${isActive ? "active" : ""}`}
                        >
                            <IconComponent className="menu-icon" size={20} strokeWidth={2} />
                            <span className="menu-label">{item.label}</span>
                        </NavLink>
                    )
                })}
            </nav>
        </aside>
    )
}
