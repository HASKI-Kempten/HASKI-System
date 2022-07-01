import { Handle, Position } from 'react-flow-renderer';

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

function CustomNode({ data }) {
    const color = data.type === 'h5p' ? color_3 : data.type === 'youtube' ? '#FF595E' : data.type === 'ppt' ? '#FFCA3A' : data.type === 'exercise' ? '#1982C4' : data.type === 'upload' ? '#4267AC' : '#FFF'
    const difficulty = data.difficulty === "1" ? 'easy' : data.difficulty === "2" ? 'medium' : data.difficulty === "3" ? 'hard' : 'NONE'
    return (
        <div style={node_style}>
            <Handle type="target" position={Position.Left} />
            <div>
                <div style={{ ...header_style, backgroundColor: color }}>
                    {data.type}
                </div>
                <div style={{ ...middle_style, backgroundColor: color }}>
                    <p style={{ 'padding': '0.3rem 0.3rem 0.0rem 0.3rem', 'fontWeight': '400', 'fontFamily': 'monospace', }}>
                        {data.label}</p>
                    <p style={{ 'padding': '0.3rem', 'paddingTop': '0px', 'fontSize': '10%', 'fontFamily': 'monospace', }}>
                        {data.modul}</p>
                </div>
            </div>
            <div style={{ ...footer_style, backgroundColor: color }}>
                <div style={{ display: 'flex' }}>
                    <div style={bottom_text}>
                        {difficulty}
                    </div>
                    <div style={bottom_text_right}>
                        ~{data.averageDuration} min.
                    </div>
                </div>

            </div>
            <Handle type="source" position={Position.Right} id="a" />
        </div >
    );
}

export default CustomNode;

