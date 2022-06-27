import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { Link } from 'react-router-dom'
import ReactFlow, { applyEdgeChanges, applyNodeChanges, Background } from 'react-flow-renderer';
import CustomControls from './CustomControls';
import CustomNode from './CustomNode';
//import initialEdges from '../data/edges.js';


function Flow() {

	const nodeTypes = useMemo(() => ({ special: CustomNode }), []);
	// https://reactflow.dev/docs/api/nodes/node-options/
	// https://reactflow.dev/docs/api/edges/edge-options/

	const [nodes, setNodes] = useState();
	const [edges, setEdges] = useState();

	const onNodesChange = useCallback(
		(changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
		[setNodes]
	);
	const onEdgesChange = useCallback(
		(changes) => setEdges((eds) => applyEdgeChanges(changes, eds)),
		[setEdges]
	);

	useEffect(() => {
		fetch('/elements').then(res => res.json()).then(data => {

			setNodes(data.elements.map((element, i, arr) => {
				const type = i === 0 ? 'input' : i === arr.length - 1 ? 'output' : 'special';
				return {
					id: (element.id).toString(),
					type: type,
					sourcePosition: 'right',
					targetPosition: 'left',
					data: {
						label: element.name,
						duration: element.duration,
						topic: element.topic,
						difficulty: element.difficulty,
					},
					position: { x: element.id * 250, y: 100 },
				}
			}));

			setEdges(data.elements.map((element, i, arr) => {
				return {
					id: `e${element.id}-${element.id + 1}`,
					type: 'default',
					source: (element.id).toString(),
					target: (element.id + 1).toString(),
					animated: true,
					markerEnd: { type: 'arrow' },
				}
			}))

		}
		);
	}, []);


	return (

		<ReactFlow
			nodes={nodes}
			edges={edges}
			onNodesChange={onNodesChange}
			onEdgesChange={onEdgesChange}

			nodeTypes={nodeTypes}

			fitView>
			<div>
				<CustomControls />
				<Background />
			</div>
		</ReactFlow>
	);
}

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

export default Flow;
export { About };