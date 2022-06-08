import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'

const About = () => {
	const [data, setLearningPath] = useState(0);

	useEffect(() => {
		fetch('/getLearningPath').then(res => res.json()).then(data => {
		setLearningPath(data);
		});
	}, []);

	return (
		<div>
			<h1>Dein Lernpfad</h1>
			<p>
				{data.name}, dein Lerntyp lässt sich nach Felder und Silverman als 
				<br /><br />
				{data.learnTyp}
				<br /><br /> 
				klassifizieren.
				Deshalb empfehlen wir dir den folgenden Lernpfad:
				<br /><br /> 
				<ul>
					<li>
						PDF zu Metriken zu Lines of Codes
					</li>
					<li>
						Video zu Metriken zu Lines of Codes
					</li>
					<li>
						Übung zu Metriken zu Lines of Codes
					</li>
				</ul>
			</p>
			<Link to={'/'}>
					<button > Zum Startbildschirm </button>
				</Link>
		</div>
	);
};

export default About;
