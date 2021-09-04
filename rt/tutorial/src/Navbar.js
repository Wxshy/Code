import './Navbar.css';
import {Link} from 'react-router-dom';
import about from './assets/about-icon.png';
import home from './assets/home-icon.png';
import code from './assets/code-icon.png';
import contact from './assets/contact-icon.png';
import gallery from './assets/gallery-icon.png';

function Navbar(){
    return (
        <nav onclick="nav_open()" onmouseover="nav_open()" onmouseleave="changesmopacity()">
            <ul>
                <li>
                    <Link to="/"><img src={home} alt='Home Icon'/>
                        <div className="navtext">Home</div>
                    </Link>
                </li>
                <li>
                    <Link to="/about"><img src={about} alt='About Icon'/>
                        <div className="navtext">About Me</div>
                    </Link>
                </li>
                <li>
                    <Link to="/gallery"><img src={gallery} alt='Gallery Icon'/>
                        <div className="navtext">Gallery</div>
                    </Link>
                </li>
                <li>
                    <Link to="/code"><img src={code} alt='Code Icon'/>
                        <div className="navtext">Code</div>
                    </Link>
                </li>
                <li>
                    <Link to="/contact"><img src={contact} alt='Contact Icon'/>
                        <div className="navtext">Contact Me</div>
                    </Link>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;