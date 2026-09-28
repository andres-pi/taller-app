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
            <div className="sidebar-brand">
                <h2>Taller APP</h2>
            </div>

            <nav className="sidebar-menu">
                {menuItems.map((item) => {
                    const IconComponent = item.icon

                    return (
                        <NavLink
                            key={item.path}
                            to={item.path}
                            className={({ isActive }) =>
                                `menu-btn ${
                                    isActive ? "active" : ""
                                }`
                            }
                        >
                            <IconComponent
                                className="menu-icon"
                                size={20}
                            />

                            {item.label}
                        </NavLink>
                    )
                })}
            </nav>
        </aside>
    )
}
