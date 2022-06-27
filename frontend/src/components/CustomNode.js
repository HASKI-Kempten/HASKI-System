import { useCallback } from 'react';
import { Handle, Position } from 'react-flow-renderer';

const handleStyle = { left: 10 };

const node_style = {
    height: '50px',
    border: '1px solid #eee',
    padding: '5px',
    'border-radius': '5px',
    background: 'white',
}

function TextUpdaterNode({ data }) {
    const onChange = useCallback((evt) => {
        console.log(evt.target.value);
    }, []);

    return (
        <div style={node_style}>
            <Handle type="target" position={Position.Top} />
            <div>
                <label htmlFor="text">Text:</label>
                <input id="text" name="text" onChange={onChange} />
            </div>
            <Handle type="source" position={Position.Bottom} id="a" style={handleStyle} />
            <Handle type="source" position={Position.Bottom} id="b" />
        </div>
    );
}

export default TextUpdaterNode;

