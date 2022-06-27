import { Controls, ControlButton } from 'react-flow-renderer';
import React from 'react';
import { ReactComponent as OpenInNewIcon } from '../media/icons/open_in_new_FILL0_wght400_GRAD200_opsz48.svg';

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
                <OpenInNewIcon />
            </ControlButton>
            <ControlButton onClick={() => console.log('another action')}>
            </ControlButton>
        </ Controls >
    );
}

export default CustomControls;