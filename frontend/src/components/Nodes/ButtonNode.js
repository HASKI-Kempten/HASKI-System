import { useState } from "react";
import { Button, Stack, Typography } from "@mui/material";
import { Box } from "@mui/system";
import { Handle, Position } from "react-flow-renderer";
import { defaultBehavior, defaultColors, node_style, defaultFonts } from "../CustomTheme";
import LearningElementDialog from "../Dialogs/LearningElementDialog";

const round_button = {
    width: "10rem",
    ':hover': {
        background: '#30588e',
    }
}

const round_button_a = {
    display: 'inline-block',
    float: 'left',
    width: '100%',
    // paddingTop: '50%',
    // paddingBottom: '50%',
    'lineHeight': '1em',
    // marginTop: '-0.5em',
    'textAlign': 'center',
    'fontFamily': defaultFonts.default,
    'fontWeight': 'bold',
    'fontSize': '1.3rem',
    color: 'white',
    'textDecoration': 'none',
}

const stack = {
    height: '10rem',
}

const round_button_circle = {
    width: '100%',
    height: 0,
    paddingBottom: '100%',
    borderRadius: '50%',
    border: defaultBehavior.border.default + defaultColors.primary[800],
    background: defaultColors.primary[900],
    boxShadow: defaultBehavior.boxShadowSize.large + defaultColors.primary[800],
    ':hover': {
        filter: 'var(--web-ui_button-filter-hover,brightness(1.1))',
    },
    ':active': {
        transform: 'translateY(0.7rem) translateZ(0)',
        boxShadow: 'unset'
    }
}
function ButtonNode({ data }) {
    const [open, setOpen] = useState(false);
    const handleDialogClick = (state) => {
        setOpen(state);
    };
    return (<>
        <Stack direction="column" justifyContent="center" alignItems="center">
            <div onClick={() => handleDialogClick(true)} style={round_button}>
                <Stack sx={round_button_circle} direction="row" justifyContent="center">
                    <Stack sx={stack} justifyContent="center" alignItems="center">
                        <p style={round_button_a}>
                            {data.label}
                        </p>
                    </Stack>

                </Stack>
            </div>
            {/* <Typography sx={{ color: 'black' }} variant="h4" component="div" gutterBottom>
                {props.data.label}
            </Typography> */}
        </Stack>
        <LearningElementDialog handler={handleDialogClick} data={data} open={open} />
    </>)
}

export default ButtonNode;