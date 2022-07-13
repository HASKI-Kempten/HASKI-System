import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Dialog, { DialogProps } from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import FormControl from '@mui/material/FormControl';
import FormControlLabel from '@mui/material/FormControlLabel';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Switch from '@mui/material/Switch';

function LearningElementDialog({ open, handler, data }) {
    const [fullWidth, setFullWidth] = React.useState(true);
    const [maxWidth, setMaxWidth] = React.useState('sm');

    const handleMaxWidthChange = (event) => {
        setMaxWidth(
            // @ts-expect-error autofill of arbitrary value is not handled.
            event.target.value,
        );
    };

    const handleFullWidthChange = (event) => {
        setFullWidth(event.target.checked);
    };

    return (
        <Dialog
            fullWidth={fullWidth}
            maxWidth={maxWidth}
            open={open}
            onClose={() => handler(false)}
        >
            <DialogTitle>{data.label}</DialogTitle>
            <DialogContent>
                <DialogContentText>
                    {(data.type === 'url') && (
                        <iframe width="560" height="315"
                            src={data.content}
                            title="Georg Video"
                            frameBorder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowFullScreen>

                        </iframe>)}
                    {(data.type === 'Picture') && (
                        <img src={process.env.PUBLIC_URL + '/' + data.content} alt="logo" />)}
                </DialogContentText>
                <Box
                    noValidate
                    component="form"
                    sx={{
                        display: 'flex',
                        flexDirection: 'column',
                        m: 'auto',
                        width: 'fit-content',
                    }}
                >
                    {/* <FormControlLabel
                        sx={{ mt: 1 }}
                        control={
                            <Switch checked={fullWidth} onChange={handleFullWidthChange} />
                        }
                        label="Full width"
                    /> */}
                </Box>
            </DialogContent>
            <DialogActions>
                <Button onClick={() => handler(false)}>Schließen</Button>
            </DialogActions>
        </Dialog >
    )
}

export default LearningElementDialog;