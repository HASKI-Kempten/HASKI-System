import { Controls, ControlButton, useReactFlow } from 'react-flow-renderer';
import React, { useCallback } from 'react';
import { ReactComponent as OpenInNewIcon } from '../media/icons/open_in_new_FILL0_wght400_GRAD200_opsz48.svg';
import HomeIcon from '@mui/icons-material/Home';
function CustomControls({ handleTransform }) {

    const { setViewport, zoomIn, zoomOut } = useReactFlow();

    return (
        <Controls
            showZoom={false}
            showInteractive={false}
            style={{
                top: '20px',
                bottom: 'unset',
            }}
        >
            <ControlButton onClick={() => handleTransform()}>
                <HomeIcon />
            </ControlButton>
            <ControlButton onClick={() => console.log('Hier passiert was')}>
            </ControlButton>
        </ Controls >
    );
}

export default CustomControls;