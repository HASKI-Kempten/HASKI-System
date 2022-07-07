import { Button, Card, Divider, Grid, Stack, Typography } from '@mui/material';
import { Handle, Position } from 'react-flow-renderer';
import { node_style, middle_style, bottom_text, bottom_text_right, footer_style, header_style } from './CustomTheme';
import ButtonNode from './Nodes/ButtonNode';
import { OverviewNode } from './Nodes/OverviewNode';

const color_3 = '#FF924C'


function UMLNode(props) {
    return (<>
        <div style={node_style}>
            <Handle type="target" position={Position.Top} />
            <div>
                <div style={{ ...header_style, backgroundColor: props.options['color'] }}>
                    {props.data.type}
                </div>
                <div style={{ ...middle_style, backgroundColor: props.options['color'] }}>
                    <p style={{ 'padding': '0.3rem 0.3rem 0.0rem 0.3rem', 'fontWeight': '400', 'fontFamily': 'monospace', }}>
                        {props.data.label}</p>
                    <p style={{ 'padding': '0.3rem', 'paddingTop': '0px', 'fontSize': '10%', 'fontFamily': 'monospace', }}>
                        {props.data.module}</p>
                </div>
            </div>
            <div style={{ ...footer_style, backgroundColor: props.options['color'] }}>
                <div style={{ display: 'flex' }}>
                    <div style={bottom_text}>
                        {props.options['difficulty']}
                    </div>
                    <div style={bottom_text_right}>
                        ~{props.data.averageDuration} min.
                    </div>
                </div>

            </div>
            <Handle type="source" position={Position.Bottom} id="a" />
        </div >
    </>)
}

function BasicNode({ data }) {
    const color = data.type === 'h5p' ? color_3 : data.type === 'youtube' ? '#FF595E' : data.type === 'ppt' ? '#FFCA3A' : data.type === 'exercise' ? '#1982C4' : data.type === 'upload' ? '#4267AC' : '#FFF'
    const difficulty = data.difficulty === "1" ? 'easy' : data.difficulty === "2" ? 'medium' : data.difficulty === "3" ? 'hard' : 'NONE'
    const options = {
        color: color,
        difficulty: difficulty,
    }
    switch (data.type) {
        case 'overview':
            return <OverviewNode data={data} options={options} />
        case 'h5p':
            return <ButtonNode data={data} options={options} />
        default:
            return <UMLNode data={data} options={options} />

    }
}


export default BasicNode;
