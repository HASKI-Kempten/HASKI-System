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
import { Accordion, AccordionDetails, AccordionSummary, Stack, Typography } from '@mui/material';

function ChangeUserDialog({ open, handler, hanlderUser }) {
    const [fullWidth, setFullWidth] = React.useState(true);
    const [maxWidth, setMaxWidth] = React.useState('sm');
    const [expanded, setExpanded] = React.useState('panel1');


    const handleChange = (panel) => (event, newExpanded) => {
        setExpanded(newExpanded ? panel : false);
    };

    return (
        <Dialog
            fullWidth={fullWidth}
            maxWidth={maxWidth}
            open={open}
            onClose={() => handler(false)}
        >
            <DialogTitle>Nutzerauswahl</DialogTitle>
            <DialogContent>
                <Accordion expanded={expanded === 'panel1'} onChange={handleChange('panel1')}>
                    <AccordionSummary aria-controls="panel1d-content" id="panel1d-header">
                        <Typography>Jim Haug</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Stack spacing={2}>
                            <Typography>
                                Balanciert (Bal) – Intuitiv (Int) – Visuell (Vis) – Bal (JH):
                            </Typography>
                            <Typography>
                                Ein intuitiver Lernstil resultiert in einer höheren Priorität von ÜB und ZL. Ein visueller Lernstil resultiert nur in einer niedrigeren Priorität von ZL. Damit ist ZL in der Priorität niedriger als ÜB. Positive Aspekte sind schwerer gewichtet. Im Hinblick auf SE und ZF gibt es bei beiden Lernstilen keine Vorlieben. ZF wird standardmäßig am Ende des Lernraums vorgeschlagen.  Daraus folgt die Reihenfolge ÜB (+), ZL (+ & /), SE, ZF. Eine Adaption hinsichtlich der Reihenfolge von BE kann nicht erfolgen, da dies mit LK verknüpft ist und nicht herausgelöst werden kann. Wäre es separat würde es sich nach der ZF einordnen, da ein intuitiver Lernstil hier in einer niedrigeren Priorität resultiert.
                            </Typography>
                            <Button variant="contained" color="primary" onClick={() => { handler(false); hanlderUser("Jim Haug") }}>
                                auswählen
                            </Button>
                        </Stack>
                    </AccordionDetails>
                </Accordion>
                <Accordion expanded={expanded === 'panel2'} onChange={handleChange('panel2')}>
                    <AccordionSummary aria-controls="panel2d-content" id="panel2d-header">
                        <Typography>Marc Normann</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Stack spacing={2}>
                            <Typography>
                                Bal – Bal – Vis – Global (Glo):
                            </Typography>
                            <Typography>
                                Ein globaler Lernstil resultiert in einer höheren Priorität von BE und ZF. Ein visueller Lernstil resultiert nur in einer niedrigeren Priorität von ZL. Im Hinblick auf SE und ÜB gibt es bei beiden Lernstilen keine Vorlieben.  Daraus folgt die Reihenfolge ZF (+), SE, ÜB, ZL (/). Eine Adaption hinsichtlich der Reihenfolge von BE kann nicht erfolgen, da dies mit LK verknüpft ist und nicht herausgelöst werden kann. Wäre es separat würde es sich nach ZF einordnen, da ein globaler Lernstil diese direkt nach LK haben möchte und dann BE (+) folgen würde.
                            </Typography>
                            <Button variant="contained" color="primary" onClick={() => { handler(false); hanlderUser("Marc Normann") }}>
                                auswählen
                            </Button>
                        </Stack>
                    </AccordionDetails>
                </Accordion>
                <Accordion expanded={expanded === 'panel3'} onChange={handleChange('panel3')}>
                    <AccordionSummary aria-controls="panel3d-content" id="panel3d-header">
                        <Typography>David Fischer</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Stack spacing={2}>
                            <Typography>
                                Aktiv (Akt) – Int – Vis – Bal:
                            </Typography>
                            <Typography>
                                Ein aktiver und intuitiver Lernstil resultiert in einer viel höheren Priorität von ÜB (++) und einer höheren Priorität von SE (+).Sowohl der aktive als auch der visuelle Lernstil sprechen für eine niedrigere Priorität von ZL, während der intuitive Lernstil dafür spricht.Positive Aspekte sind schwerer gewichtet.Im Hinblick auf ZF gibt es bei beiden Lernstilen keine Vorlieben.ZF wird standardmäßig am Ende des Lernraums vorgeschlagen.Daraus folgt die Reihenfolge ÜB (++), SE (+), ZL (/ / & +), ZF.Eine Adaption hinsichtlich der Reihenfolge von BE kann nicht erfolgen, da dies mit LK verknüpft ist und nicht herausgelöst werden kann.Wäre es separat würde es sich nach der ZF einordnen, da sowohl der aktive als auch der intuitiver Lernstil hier in eine niedrigere Priorität bewirken.                            </Typography>
                            <Button variant="contained" color="primary" onClick={() => { handler(false); hanlderUser("David Fischer") }}>
                                auswählen
                            </Button>
                        </Stack>
                    </AccordionDetails>
                </Accordion>
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

export default ChangeUserDialog;