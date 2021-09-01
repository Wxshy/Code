import './Navbar';
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
                    <a href="/"><img src={home}/>
                        <div className="navtext">Home</div>
                    </a>
                </li>
                <li>
                    <a href="about.html"><img src={about}/>
                        <div className="navtext">About Me</div>
                    </a>
                </li>
                <li>
                    <a href="uc.html"><img src={gallery}/>
                        <div className="navtext">Galleryy</div>
                    </a>
                </li>
                <li>
                    <a href="https://github.com/Wxshy"><img src={code}/>
                        <div className="navtext">Code</div>
                    </a>
                </li>
                <li>
                    <a href="uc.html"><img src={contact}/>
                        <div className="navtext">Contact Me</div>
                    </a>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;