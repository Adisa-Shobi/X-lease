import { Link } from 'react-router-dom';
import './images/xlease-logo4.png';

const Header = () => {
    return ( 
        <header>
            <Link to="/">
                <img src="./logo.png" alt="" className="logo" />
            </Link>
            <div className="search">
                <button className="search-button">
                    <div className="search-logo"></div>
                    search
                </button>
                <input type="text" className="search-field" />
            </div>
            <div className="links">
                <Link to="lease-my-device/" className="lease-button">Lease your device</Link>
                <Link to="lease-my-device/" className="lease-button">Signin</Link>
                <Link to="lease-my-device/" className="lease-button">Signup</Link>
                {/* <button className="profile"></button> */}
            </div>
        </header>
     );
}
 
export default Header;