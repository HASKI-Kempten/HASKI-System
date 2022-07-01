import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { Link } from 'react-router-dom'
import ReactFlow, { addEdge, applyEdgeChanges, applyNodeChanges, Background } from 'react-flow-renderer';
import CustomControls from './CustomControls';
import CustomNode from './CustomNode';
import Typography from '@mui/material/Typography';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import { default as MLink } from '@mui/material/Link';
import HomeIcon from '@mui/icons-material/Home';
const axios = require('axios').default;

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

	const onConnect = useCallback(
		(connection) => setEdges((eds) => addEdge({ ...connection, animated: true }, eds)),
		[setEdges]
	);

	useEffect(() => {
		fetch('/elements').then(res => res.json()).then(data => {

			setNodes(data.elements.map((element, i, arr) => {
				const type = i === 0 ? 'input' : i === arr.length - 1 ? 'output' : 'special';
				return {
					id: element.id,
					type: type,
					sourcePosition: 'right',
					targetPosition: 'left',
					data: {
						label: element.name,
						difficulty: element.difficulty,
						creationDate: element.creationDate,
						modul: element.modul,
						averageDuration: element.averageDuration,
						semester: element.semester,
						style: element.style,
						type: element.type,
						proLIST: element.proLIST,
						contraLIST: element.contraLIST,

					},
					position: { x: element.id * 250, y: 100 },
				}
			}));

			setEdges(data.elements.map((element, i, arr) => {
				return {
					id: `e${element.id}-${element.id + 1}`,
					type: 'default',
					source: element.id,
					target: (parseInt(element.id) + 1).toString(),
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
			onConnect={onConnect}
			nodeTypes={nodeTypes}

			fitView>
			<div>
				<CustomControls />
				<Background />
			</div>
		</ReactFlow>
	);
}
function noop() { }

const About = () => {


	return (
		<>
			<div role="presentation" onClick={noop()}>
				<Breadcrumbs aria-label="breadcrumb">
					<MLink
						underline="hover"
						sx={{ display: 'flex', alignItems: 'center' }}
						color="inherit"
						href="/"
					>
						<HomeIcon sx={{ mr: 0.5 }} fontSize="inherit" />
						Dashboard
					</MLink>
					<MLink
						underline="hover"
						sx={{ display: 'flex', alignItems: 'center' }}
						color="inherit"
					>
						Wirtschaftsinformatik I
					</MLink>
					<Typography
						sx={{ display: 'flex', alignItems: 'center' }}
						color="text.primary"
					>

						Lernpfad
					</Typography>
				</Breadcrumbs>
			</div>
			<Flow />
		</>
	);
};

export default About;
export { Flow };