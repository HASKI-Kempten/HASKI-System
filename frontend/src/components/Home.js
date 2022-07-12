import logo from '../haski.jpeg';
import '../App.css';
// import Swiper styles
import 'swiper/css';
import MenuAppBar from './MenuBar';
import ChangeUserDialog from './Dialogs/ChangeUserDialog';
import React from 'react';
import { Button, Card, Grid, Paper, Stack, Typography } from '@mui/material';
import DashElement from './DashElement';
import CustomBarChart from './Charts/CustomBarChart';
import { Box } from '@mui/system';
import CustomizedInput from './Dialogs/CustomInput';
import { Link } from 'react-router-dom';

const Home = () => {
  const [open, setOpen] = React.useState(false);
  const [user, setUser] = React.useState("David Fischer");

  const handleChangeUserDialogClick = (state) => {
    setOpen(state);
  };

  const handleChangeUser = (username) => {
    setUser(username);
  };



  return (
    <>
      <Stack spacing={1} container height={'98%'}>
        <MenuAppBar handler={handleChangeUserDialogClick} user={user} />
        <ChangeUserDialog handler={handleChangeUserDialogClick} open={open} hanlderUser={handleChangeUser} />
        <Grid container spacing={4} sx={{ height: '100%', width: '100%' }}>
          <Grid item xs={12} md={9}>
            <Stack container direction="column"
              justifyContent="flex-start"
              alignItems="center"
            >
              <Grid columnSpacing={{ xs: 1, sm: 2, md: 3 }} container>
                <Grid item xs={6}>
                  <DashElement link="/learningPath" heading="zuletzt" title="Halstaed C++ Übung" subtitle="Qualitätssicherung durch Metriken" buttonText="weiter" text="1/10 bearbeitet" />
                </Grid>
                <Grid item xs={6}>
                  <DashElement link="/learningPath" heading="vorgeschlagen" title="Metriken 1" subtitle="Qualitätssicherung durch Metriken" buttonText="weiter" text="4/10 bearbeitet" />
                </Grid>
              </Grid>
              <Card sx={{ height: '100%', width: '100%', marginTop: '2rem' }}>
                <Box sx={{ height: '100%', width: '100%', padding: '1rem' }}>
                  <Typography variant="h6" gutterBottom component="div">
                    Laut dem ILS Fragebogen sind die Dimensionen Deines Lernstils:
                  </Typography>
                  <Box sx={{ padding: '1rem' }}>
                    <CustomBarChart />
                  </Box>
                  <Typography variant="h6" gutterBottom component="div">
                    Dein Ergebnis des LIST Fragebogens:
                  </Typography>
                </Box>
              </Card>
              <Card sx={{ height: '100%', width: '100%', marginTop: '2rem' }}>
                <Box sx={{ padding: '1rem' }}>
                  <Typography variant="h6" gutterBottom component="div">
                    Einige UI Elemente wurden zusammengestellt, um einen Überblick über das Design zu bekommen. Das Design basiert auf Googles Material Design, und wurde für mehr individualität bezüglich Farbe und Form angepasst. Um die spielerische Optik zu bekommen, wurde sich an Educational Apps und Lernplattformen orientiert. Mehr dazu im Design Dokument.
                  </Typography>

                  <Link to="/theme" style={{ 'textDecoration': 'none' }}>
                    <Button variant="contained" size="small">
                      <Typography >
                        Demo
                      </Typography>
                    </Button>
                  </Link>
                </Box>
              </Card>
            </Stack>
          </Grid>
          <Grid item xs={12} md={3}>
            <Card sx={{ height: '100%' }}>
              <Stack
                direction="column"
                justifyContent="space-between"
                alignItems="center"
                spacing={2}
                sx={{ height: '100%' }}
              >
                <Stack sx={{ width: '100%' }}>
                  <img src={logo} width="100px" alt="logo" style={{ margin: '1rem', borderRadius: '20px' }} />

                </Stack>
                <Card sx={{ margin: '1rem', padding: '1rem', width: '80%', height: '14%' }}>
                  <Typography variant="h6" gutterBottom component="div">
                    Wuff wuff... Wo möchtest du weitermachen?
                  </Typography>
                </Card>
                <div></div>
                <div></div>
                <CustomizedInput />
              </Stack>
            </Card>
          </Grid>
        </Grid>
      </Stack>
    </>
  );
};

export default Home;