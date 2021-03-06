import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { CardHeader, Grid, IconButton, Stack, Tooltip } from '@mui/material';
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
        <Card sx={{ height: '100%' }}>
            <CardHeader
                action={
                    <Tooltip title="Wieso wird mir das vorgeschlagen?">
                        <Button variant="text" sx={{ textTransform: 'lowercase' }}>
                            i
                        </Button>
                    </Tooltip>

                }
                subheader={heading}
            />
            <CardContent>
                <Grid columnSpacing={{ xs: 1, sm: 2, md: 3 }} container
                    direction="row"
                    justifyContent="space-between"
                    alignItems="center">
                    <Grid item xs={12} md={6}>
                        <Stack>
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
                    </Grid>
                    <Grid item xs={12} md={6} alignItems="center">

                        <Link to={link} style={{ 'textDecoration': 'none', width: '100%' }}>
                            <Button variant="contained">
                                <Typography >
                                    {buttonText}
                                </Typography>
                            </Button>
                        </Link>
                    </Grid>
                </Grid>
            </CardContent>


        </Card>
    );
}
