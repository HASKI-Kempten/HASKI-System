import React, { useState, useEffect, useCallback, useMemo } from 'react';
import ReactFlow, { useReactFlow, addEdge, applyEdgeChanges, applyNodeChanges, Background, ReactFlowProvider } from 'react-flow-renderer';
import CustomControls from './CustomControls';
import BasicNode from './Nodes/CustomNode';
import Typography from '@mui/material/Typography';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import { default as MLink } from '@mui/material/Link';
import HomeIcon from '@mui/icons-material/Home';
import { Container } from '@mui/system';
import { Card, Grid } from '@mui/material';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import { Paper, Button } from '@mui/material';
import MenuAppBar from './MenuBar';

function Flow({ elements }) {

	const backendPath = process.env.REACT_APP_BACKENDHOST || 'http://localhost:5000';

	const nodeTypes = useMemo(() => ({ special: BasicNode }), []);
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

	const { setViewport, zoomIn, zoomOut } = useReactFlow();

	const handleTransform = useCallback(
		() => {
			setViewport({ x: 300, y: -400, zoom: 1.2 }, { duration: 800 });
		},
		[setViewport]
	);

	useEffect(() => {

		fetch(backendPath + '/elements').then(res => res.json()).then(data => {

			setNodes(data.elements.map((element, i, arr) => {
				const type = i === 0 ? 'special' : i === arr.length - 1 ? 'output' : 'special';
				return {
					id: (element.id).toString(),
					type: type,
					// sourcePosition: 'right',
					// targetPosition: 'left',
					data: {
						label: element.name,
						difficulty: element.difficulty,
						creationDate: element.creationDate,
						module: element.module,
						averageDuration: element.averageDuration,
						semester: element.semester,
						style: element.style,
						type: element.type,
						proLIST: element.proLIST,
						contraLIST: element.contraLIST,

					},
					// position: { x: element.id * 250, y: 100 },
					position: { x: 250, y: element.id * 400 },
				}
			}));

			setEdges(data.elements.map((element, i, arr) => {
				return {
					id: `e${element.id}-${element.id + 1}`,
					type: 'default',
					source: element.id.toString(),
					target: (element.id + 1).toString(),
					animated: true,
					markerEnd: { type: 'arrow' },
				}
			}));

			handleTransform();

		}
		);
	}, [handleTransform, backendPath]);



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
				{/* <Background /> */}
			</div>
		</ReactFlow>
	);
}
function noop() { }

const About = () => {


	return (
		<>
			<MenuAppBar />

			<Stack spacing={2} sx={{ height: '100%' }}>
				{/* Flow */}
				<ReactFlowProvider>
					<Flow />
				</ReactFlowProvider>
			</Stack>
		</>

	);
};

export default About;
export { Flow };