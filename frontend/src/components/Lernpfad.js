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
import ChangeUserDialog from './Dialogs/ChangeUserDialog';


function getWindowDimensions() {
	const { innerWidth: width, innerHeight: height } = window;
	return {
		width,
		height
	};
}

function Flow({ user }) {

	const backendPath = process.env.REACT_APP_BACKENDHOST || 'http://localhost:5000';

	const nodeTypes = useMemo(() => ({ special: BasicNode }), []);
	// https://reactflow.dev/docs/api/nodes/node-options/
	// https://reactflow.dev/docs/api/edges/edge-options/

	const [nodes, setNodes] = useState();
	const [edges, setEdges] = useState();
	const [windowDimensions, setWindowDimensions] = useState(getWindowDimensions());

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
			setViewport({ x: getWindowDimensions().width / 3, y: getWindowDimensions().height / 10, zoom: 1.2 }, { duration: 800 });
		},
		[setViewport]
	);

	useEffect(() => {
		let userId = '3';
		// dirty nach user switchen
		switch (user) {
			case "Jim Haug":
				userId = '1';
				break;

			case "Marc Normann":
				userId = '2';
				break;

			case "David Fischer":
				userId = '3';
				break;
			default:
				break;
		}
		fetch(backendPath + '/learningWay/' + userId + '/' + '1' + '/' + userId).then(res => res.json()).then(data => {
			// fetch element from learningway
			// for each in data.elements do that
			Promise.all(data.elements.map((learningWayElement, i, arr) => {
				return fetch(backendPath + '/elements/' + learningWayElement.elementId).then(res => res.json())
			})).then(
				(elements) => {
					setNodes(elements.map((element, i, arr) => {
						const type = i === 0 ? 'special' : 'special';
						return {
							id: (i).toString(),
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
								content: element.content,
								id: i.toString(),

							},
							// position: { x: element.id * 250, y: 100 },
							position: { x: 10, y: i * 400 },
						}
					}));

					setEdges(elements.map((element, i, arr) => {
						return {
							id: `e${element.id}-${element.id + 1}`,
							type: 'default',
							source: i.toString(),
							target: (i + 1).toString(),
							animated: true,
							markerEnd: { type: 'arrow' },
						}
					}));

					handleTransform();
				}
			)


		}
		);
	}, [handleTransform, backendPath, user]);



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
				<CustomControls handleTransform={handleTransform} />
				{/* <Background /> */}
			</div>
		</ReactFlow>
	);
}
function noop() { }

const About = () => {

	const [open, setOpen] = React.useState(false);
	const [user, setUser] = React.useState("David Fischer");

	const handleChangeUserDialogClick = (state) => {
		setOpen(state);
	};

	const handleChangeUser = (username) => {
		setUser(username);
	};
	return (

		<Stack sx={{ height: '100%' }}>
			<MenuAppBar handler={handleChangeUserDialogClick} user={user} />
			<ChangeUserDialog handler={handleChangeUserDialogClick} open={open} hanlderUser={handleChangeUser} />
			{/* Flow */}
			<ReactFlowProvider>
				<Flow user={user} />
			</ReactFlowProvider>
		</Stack>

	);
};

export default About;
export { Flow };