import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Stack } from '@mui/material';
import { Link } from "react-router-dom";

const bull = (
    <Box
        component="span"
        sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
    >
        •
    </Box>
);

export default function DashElement({ heading, title, subtitle, text, buttonText, link }) {
    return (
        <Card sx={{ minWidth: 275, minHeight: 150 }}>
            <CardContent>
                <Stack
                    direction="row"
                    justifyContent="space-between"
                    alignItems="center"
                    spacing={2}
                >
                    <Stack>
                        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                            {heading}
                        </Typography>
                        <Typography variant="h5" component="div">
                            {title}
                        </Typography>
                        <Typography sx={{ mb: 1.5 }} color="text.secondary">
                            {subtitle}
                        </Typography>
                        <Typography variant="body2">
                            {text}
                        </Typography>
                    </Stack>


                    <CardActions>
                        <Link to={link} style={{ 'textDecoration': 'none' }}>
                            <Button variant="contained" size="small">
                                <Typography >
                                    {buttonText}
                                </Typography>
                            </Button>
                        </Link>
                    </CardActions>
                </Stack>
            </CardContent>


        </Card>
    );
}
