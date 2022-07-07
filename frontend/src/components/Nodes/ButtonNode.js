import { Button } from "@mui/material";
import { Handle, Position } from "react-flow-renderer";
import { defaultBehavior, defaultColors, node_style } from "../CustomTheme";

const round_button = {
    width: "50%",
}

const round_button_a = {
    display: 'block',
    float: 'left',
    width: '100%',
    paddingTop: '50%',
    paddingBottom: '50%',
    'line-height': '1em',
    marginTop: '-0.5em',
    'text-align': 'center',
    color: '#e2eaf3',
    'font-family': 'Verdana',
    'font-weight': 'bold',
    'font-size': '2rem',
    'text-decoration': 'none',
}

const round_button_circle = {
    width: '100%',
    height: 0,
    paddingBottom: '100%',
    borderRadius: '50%',
    border: defaultBehavior.border.default + ' ' + defaultColors.lightgrey,
    overflow: 'hidden',

    background: '#4679BD',
    'box-shadow': defaultBehavior.boxShadowSize.default + defaultColors.lightgrey,
    ':hover': {
        background: '#30588e',
    }
}
function ButtonNode(props) {
    return (<>
        <Handle type="target" position={Position.Top} />
        <div style={round_button}>

            <div style={round_button_circle}>
                <a style={round_button_a} href="http://google.de">
                    {props.data.label}
                </a>
            </div>
        </div>
        <Handle type="source" position={Position.Bottom} id="a" />
    </>)
}

export default ButtonNode;