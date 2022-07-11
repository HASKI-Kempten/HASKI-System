import { Button, Card, Divider, Grid, Stack, Typography } from '@mui/material';
import { useCallback } from 'react';
import { Handle, Position, useReactFlow } from 'react-flow-renderer';


const color_3 = '#FF924C'

const node_style = {
    display: 'flex',
    'flexDirection': 'column',
    height: '100 %',
    'borderWidth': '2px',
    'borderStyle': 'solid',
    'borderImage': 'initial',
    'borderColor': 'black',
    'borderRadius': '8px',
    'overflow': 'hidden',
    'boxShadow': 'rgb(0 0 0 / 10%) 0px 4px 6px -1px, rgb(0 0 0 / 6%) 0px 2px 4px -1px',
}

const footer_style = {
    'backgroundColor': '#FFCA3A',
    'color': 'black',
    'fontWeight': '400',
    'textTransform': 'uppercase',
    'fontFamily': 'monospace',
    'fontSize': '10px',
    'paddingInlineStart': '0.5rem',
    'paddingInlineEnd': '0.5rem',
    'paddingTop': '0.2rem',
    'paddingBottom': '0.2rem',
    'borderTopWidth': '2px',
    'borderTopStyle': 'solid',
    'borderColor': 'black',
    flex: '1 1 0%'
}
const header_style = {
    'backgroundColor': '#FFCA3A',
    'color': 'black',
    'fontWeight': '400',
    'textTransform': 'uppercase',
    'fontFamily': 'monospace',
    'fontSize': '10px',
    'paddingInlineStart': '0.5rem',
    'paddingInlineEnd': '0.5rem',
    'paddingTop': '0.2rem',
    'paddingBottom': '0.2rem',
    'borderBottomWidth': '2px',
    'borderBottomStyle': 'solid',
    'borderColor': 'black',
    flex: '1 1 0%'
}

const middle_style = {
    backgroundColor: '#FFCA3A',
    margin: '0rem',
    paddingTop: '0.1rem',
    paddingBottom: '0.1rem',
}


const bottom_text = {
    'paddingTop': '0.2rem',
    'paddingBottom': '0.2rem',
    'paddingLeft': '0.2rem',
}
const bottom_text_right = {
    'position': 'absolute',
    'paddingTop': '0.2rem',
    'paddingBottom': '0.2rem',
    'paddingLeft': '0.2rem',
    right: '0.5rem',
}


function OverviewNode(props) {

    const { setViewport, zoomIn, zoomOut } = useReactFlow();

    const handleTransform = useCallback(
        () => {
            setViewport({ x: 150, y: -1000, zoom: 1.2 }, { duration: 800 });
        },
        [setViewport]
    );

    return (
        <Card sx={{ padding: 2, maxWidth: '400px' }}>
            <Stack spacing={2}>
                {/* <Typography variant="h4" component="div" gutterBottom>
                        Lernraum Metriken
                    </Typography> */}
                <Stack
                    direction="row"
                    justifyContent="flex-start"
                    alignItems="center"
                    spacing={2}
                >
                    <h4>{props.data.label}</h4>
                    <Divider orientation="vertical" variant="middle" flexItem />
                    <h4>1h 22 min</h4>
                </Stack>
                <Grid container
                    justifyContent="center"
                    alignItems="center"
                >
                    <Grid item xs={8}>
                        <Typography variant="body" component="div" gutterBottom>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                        </Typography>
                    </Grid>
                    <Grid container item xs={4} justifyContent="center">
                        <Grid item
                            justifyContent="center"
                            alignItems="center">
                            <Button onClick={handleTransform} variant="contained" size="large">
                                Continue
                            </Button>
                        </Grid>
                    </Grid>
                </Grid>
            </Stack>
        </Card>
    );
}

export { OverviewNode };