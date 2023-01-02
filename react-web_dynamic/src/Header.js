import './images/xlease-logo4.png';

const Header = () => {
    return ( 
        <header>
            <a href="#">
                <img src="./logo.png" alt="" className="logo" />
            </a>
            <div className="search">
                <button className="search-button">
                    <div className="search-logo"></div>
                    search
                </button>
                <input type="text" className="search-field" />
            </div>
            <div className="links">
                <a href="#" className="lease-button">Lease your device</a>
                <button className="profile"></button>
            </div>
        </header>
     );
}
 
export default Header;