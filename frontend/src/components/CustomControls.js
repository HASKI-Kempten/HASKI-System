import { Controls, ControlButton } from 'react-flow-renderer';

function CustomControls() {
    return (
        <Controls
            showZoom={false}
            showInteractive={false}
            style={{
                top: '20px',
                bottom: 'unset',
            }}
        >
            <ControlButton onClick={() => console.log('action')}>
                {/* <FancyIcon /> */}
            </ControlButton>
            <ControlButton onClick={() => console.log('another action')}>
                {/* <AnotherFancyIcon /> */}
            </ControlButton>
        </ Controls >
    );
}

export default CustomControls;