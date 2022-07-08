import { Button, Card, Divider, Grid, Stack, Typography } from '@mui/material';
import { Handle, Position } from 'react-flow-renderer';
import ButtonNode from './ButtonNode';
import { OverviewNode } from './OverviewNode';
import { UMLNode } from './UMLNode';

const color_3 = '#FF924C'


function BasicNode({ data }) {
    const color = data.type === 'h5p' ? color_3 : data.type === 'youtube' ? '#FF595E' : data.type === 'ppt' ? '#FFCA3A' : data.type === 'exercise' ? '#1982C4' : data.type === 'upload' ? '#4267AC' : '#FFF'
    const difficulty = data.difficulty === "1" ? 'easy' : data.difficulty === "2" ? 'medium' : data.difficulty === "3" ? 'hard' : 'NONE'
    const options = {
        color: color,
        difficulty: difficulty,
    }
    switch (data.type) {
        case 'overview':
            return (<>
                <Handle type="target" position={Position.Top} />
                <OverviewNode data={data} options={options} />
                <Handle type="source" position={Position.Bottom} id="a" />
            </>)
        case 'h5p':
            return (<>
                <Handle type="target" position={Position.Top} />
                <ButtonNode data={data} options={options} />
                <Handle type="source" position={Position.Bottom} id="a" />
            </>)
        default:
            return (<>
                <Handle type="target" position={Position.Top} />
                <UMLNode data={data} options={options} />
                <Handle type="source" position={Position.Bottom} id="a" />
            </>)

    }
}


export default BasicNode;
