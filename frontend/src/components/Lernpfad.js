import React, { useState, useEffect, useCallback, useMemo } from 'react';
import ReactFlow, { addEdge, applyEdgeChanges, applyNodeChanges, Background } from 'react-flow-renderer';
import CustomControls from './CustomControls';
import CustomNode from './CustomNode';
import Typography from '@mui/material/Typography';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import { default as MLink } from '@mui/material/Link';
import HomeIcon from '@mui/icons-material/Home';
import { Container } from '@mui/system';
import { Grid } from '@mui/material';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import { Paper, Button } from '@mui/material';
import MenuAppBar from './MenuBar';

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
					position: { x: 250, y: element.id * 250 },
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
				{/* <Background /> */}
			</div>
		</ReactFlow>
	);
}
function noop() { }

const About = () => {
	const [data, setData] = useState();
	useEffect(() => {
		fetch('/elements').then(res => res.json()).then(data => {
			setData(data);
		}
		);
	}, []);

	return (
		<>
			<MenuAppBar />
			
			<Stack spacing={2} sx={{ height: '100%' }}>
				<Container maxWidth="md" sx={{ marginTop: 2 }}>
					{/* kurzübersicht stack */}
					<Paper elevation={2} sx={{ padding: 2 }}>
						<Stack spacing={2}>
							<h3>Kurzüberblick</h3>
							<Stack
								direction="row"
								justifyContent="flex-start"
								alignItems="center"
								spacing={2}
							>
								<h4>Metriken 1</h4>
								<Divider orientation="vertical" variant="middle" flexItem />
								<h4>1h 22 min</h4>
							</Stack>
							<Grid container
								justifyContent="center"
								alignItems="center"
							>
								<Grid item xs={8}>
									Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
								</Grid>
								<Grid container item xs={4} justifyContent="center">
									<Grid item
										justifyContent="center"
										alignItems="center">
										<Button variant="contained" size="large">
											Continue
										</Button>
									</Grid>
								</Grid>
							</Grid>
						</Stack>
					</Paper>
				</Container>
				{/* Flow */}
				<Flow />
			</Stack>
		</>

	);
};

export default About;
export { Flow };