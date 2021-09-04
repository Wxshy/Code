import './App.css';

import Home from './Home';
import Navbar from './Navbar';
import About from './About';
import Contact from './Contact';
import Gallery from './Gallery';

import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path='/' exact component={Home}/>
        <Route path='/about' exact component={About}/>
        <Route path='/contact' exact component={Contact}/>
        <Route path='/gallery' exact component={Gallery}/>
        <Route path='/code' component={() => {window.location.href = "https://www.github.com/Wxshy"}}/>
      </Switch>
    </Router>
  );
}

export default App;
