import { node_style, middle_style, bottom_text, bottom_text_right, footer_style, header_style } from '../CustomTheme';

export function UMLNode(props) {
    return (<>
        <div style={node_style}>
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
        </div>
    </>);
}
