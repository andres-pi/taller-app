import {
    Bell,
    Search
} from 'lucide-react'
import './Header.css'

export const Header = () =>  {
    return (
        <header className="header">
            <div className="header__search">
                <Search className='search-icon' size={18} />

                <input
                    type="text"
                    placeholder="Buscar..."
                />

                <div className="header__shortcut">
                    <span>Ctrl</span>
                    <span>K</span>
                </div>

            </div>

            <div className="header__actions">
                <button
                    className="header__notification"
                    aria-label="Notificaciones"
                >
                    <Bell size={20} strokeWidth={2} />
                    <span className="header__notification-dot" />
                </button>
                <div className="header__profile">
                    <div className="profile-avatar">AP</div>
                </div>
            </div>
        </header>
    )
}
