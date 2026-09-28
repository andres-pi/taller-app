import {
    Bell,
    Search
} from 'lucide-react'
import './Header.css'

export const Header = () =>  {
    return (
        <header className="header">
            <div className="header__search">
                <Search size={18} />

                <input
                    type="text"
                    placeholder="Buscar..."
                />

                <span className="header__shortcut">
                    Ctrl K
                </span>
            </div>

            <div className="header__actions">
                <button
                    className="header__notification"
                    aria-label="Notificaciones"
                >
                    <Bell size={19} />
                    <span className="header__notification-dot" />
                </button>
            </div>
        </header>
    )
}
