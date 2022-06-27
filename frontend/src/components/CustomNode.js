import { useCallback } from 'react';
import { Handle, Position } from 'react-flow-renderer';

// const handleStyle = { left: 10 };

// const node_style = {
//     height: '50px',
//     border: '1px solid #000',
//     padding: '5px',
//     'border-radius': '5px',
//     background: 'white',
//     overflow: 'hidden',
//     'box-shadow': 'rgb(0 0 0 / 10%) 0px 4px 6px -1px, rgb(0 0 0 / 6%) 0px 2px 4px -1px',
// }
const node_style = {
    display: 'flex',
    'flex-direction': 'column',
    height: '100 %',
    'border-width': '1px',
    'border-style': 'solid',
    'border-image': 'initial',
    'border-color': 'grey',
    'border-radius': '8px',
    'overflow': 'hidden',
    'box-shadow': 'rgb(0 0 0 / 10%) 0px 4px 6px -1px, rgb(0 0 0 / 6%) 0px 2px 4px -1px',
}

const footer_style = {
    'background-color': 'rgb(254, 254, 254)',
    'color': 'black',
    'font-weight': '400',
    'text-transform': 'uppercase',
    'font-family': 'monospace',
    'font-size': '10px',
    'padding-inline-start': '0.5rem',
    'padding-inline-end': '0.5rem',
    'padding-top': '0.2rem',
    'padding-bottom': '0.2rem',
    'border-top-width': '1px',
    'border-top-style': 'solid',
    'border-color': 'grey',
    flex: '1 1 0%'
}
const header_style = {
    'background-color': 'rgb(254, 254, 254)',
    'color': 'black',
    'font-weight': '400',
    'text-transform': 'uppercase',
    'font-family': 'monospace',
    'font-size': '10px',
    'padding-inline-start': '0.5rem',
    'padding-inline-end': '0.5rem',
    'padding-top': '0.2rem',
    'padding-bottom': '0.2rem',
    'border-bottom-width': '1px',
    'border-bottom-style': 'solid',
    'border-color': 'grey',
    flex: '1 1 0%'
}

const bottom_text = {
    'padding-top': '0.2rem',
    'padding-bottom': '0.2rem',
    'padding-left': '0.2rem',
}
const bottom_text_right = {
    'position': 'absolute',
    'padding-top': '0.2rem',
    'padding-bottom': '0.2rem',
    'padding-left': '0.2rem',
    right: '0.5rem',
}

function CustomNode({ data }) {


    return (
        <div style={node_style}>
            <Handle type="target" position={Position.Left} />
            <div>
                <div style={header_style}>
                    {data.topic}
                </div>
                <p style={{ 'padding': '0.5rem', 'font-weight': '400', 'font-family': 'monospace', }}>{data.label}</p>
            </div>
            <div style={footer_style}>
                <div style={{ display: 'flex' }}>
                    <div style={bottom_text}>
                        {data.difficulty}
                    </div>
                    <div style={bottom_text_right}>
                        ~{data.duration * 60} min.
                    </div>
                </div>

            </div>
            <Handle type="source" position={Position.Right} id="a" />
        </div>
    );
}

export default CustomNode;

