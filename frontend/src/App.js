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
import { ThemeProvider } from '@mui/material/styles';
import { Theme } from "./components/CustomTheme";
import ThemePresentation from "./components/ThemePresentation";


function App() {
	return (
		<>
			<meta property="og:title" content="__OG_TITLE__" />
			<meta property="og:description" content="__OG_DESCRIPTION__" />
			<ThemeProvider theme={Theme}>
				<Router>
					<Routes>
						<Route path="/" element={<Home />} />
						<Route path="/courseDashboard" element={<CourseDashboard />} />
						<Route path="/learningPath" element={<Lernpfad />} />
						<Route path="/theme" element={<ThemePresentation />} />
						<Route path="/quiz" element={<Quiz />} />
					</Routes>
				</Router>
			</ThemeProvider>
		</>

	);
}

export default App;
