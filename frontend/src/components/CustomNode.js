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
    'flexDirection': 'column',
    height: '100 %',
    'borderWidth': '1px',
    'borderStyle': 'solid',
    'borderImage': 'initial',
    'borderColor': 'grey',
    'borderRadius': '8px',
    'overflow': 'hidden',
    'boxShadow': 'rgb(0 0 0 / 10%) 0px 4px 6px -1px, rgb(0 0 0 / 6%) 0px 2px 4px -1px',
}

const footer_style = {
    'backgroundColor': 'rgb(254, 254, 254)',
    'color': 'black',
    'fontWeight': '400',
    'textTransform': 'uppercase',
    'fontFamily': 'monospace',
    'fontSize': '10px',
    'paddingInlineStart': '0.5rem',
    'paddingInlineEnd': '0.5rem',
    'paddingTop': '0.2rem',
    'paddingBottom': '0.2rem',
    'borderTopWidth': '1px',
    'borderTopStyle': 'solid',
    'borderColor': 'grey',
    flex: '1 1 0%'
}
const header_style = {
    'backgroundColor': 'rgb(254, 254, 254)',
    'color': 'black',
    'fontWeight': '400',
    'textTransform': 'uppercase',
    'fontFamily': 'monospace',
    'fontSize': '10px',
    'paddingInlineStart': '0.5rem',
    'paddingInlineEnd': '0.5rem',
    'paddingTop': '0.2rem',
    'paddingBottom': '0.2rem',
    'borderBottomWidth': '1px',
    'borderBottomStyle': 'solid',
    'borderColor': 'grey',
    flex: '1 1 0%'
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

function CustomNode({ data }) {


    return (
        <div style={node_style}>
            <Handle type="target" position={Position.Left} />
            <div>
                <div style={header_style}>
                    {data.modul}
                </div>
                <p style={{ 'padding': '0.5rem', 'fontWeight': '400', 'fontFamily': 'monospace', }}>{data.label}</p>
            </div>
            <div style={footer_style}>
                <div style={{ display: 'flex' }}>
                    <div style={bottom_text}>
                        {data.difficulty}
                    </div>
                    <div style={bottom_text_right}>
                        ~{data.averageDuration} min.
                    </div>
                </div>

            </div>
            <Handle type="source" position={Position.Right} id="a" />
        </div>
    );
}

export default CustomNode;

