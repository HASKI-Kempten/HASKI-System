import "./App.css";
import {
	BrowserRouter as Router,
	Routes,
	Route,
} from "react-router-dom";

import Home from "./components/Home";
import Lernpfad from "./components/Lernpfad";
import Quiz from "./components/Quiz";

function App() {
	return (
		<>
			<Router>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/learningPath" element={<Lernpfad />} />
					<Route path="/quiz" element={<Quiz />} />
				</Routes>
			</Router>
		</>
	);
}

export default App;
