import "./App.css";
import {
	BrowserRouter as Router,
	Routes,
	Route,
} from "react-router-dom";

import Home from "./components/Home";
import Lernpfad from "./components/Lernpfad";
import Quiz from "./components/Quiz";
import CourseDashboard from "./components/CourseDashboard";

function App() {
	return (
		<>
			<meta name="viewport" content="initial-scale=1, width=device-width" />
			<Router>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/courseDashboard" element={<CourseDashboard />} />
					<Route path="/learningPath" element={<Lernpfad />} />
					<Route path="/quiz" element={<Quiz />} />
				</Routes>
			</Router>
		</>
	);
}

export default App;
