import logo from '../haski.jpeg';
import '../App.css';
import { Link } from "react-router-dom";
// import Swiper styles
import 'swiper/css';

const Home = () => {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to the HASKI project!
        </p>
        <br />
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/courseDashboard">Course Dashboard</Link>
          </li>
          <li>
            <Link to="/quiz">Finde deinen Lerntypen heraus</Link>
          </li>
          <li>
            <Link to="/learningPath">Lernpfad ansehen</Link>
          </li>
          <li>
            <Link to="/theme">Theme presentation</Link>
          </li>
        </ul>
      </header>
    </div>
  );
};

export default Home;