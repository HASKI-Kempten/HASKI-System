import logo from '../haski.jpeg';
import '../App.css';
// import Swiper styles
import 'swiper/css';
import MenuAppBar from './MenuBar';
import ChangeUserDialog from './Dialogs/ChangeUserDialog';
import React from 'react';
import { Card, Grid, Paper, Stack, Typography } from '@mui/material';
import DashElement from './DashElement';
import CustomBarChart from './Charts/CustomBarChart';
import { Box } from '@mui/system';
import CustomizedInput from './Dialogs/CustomInput';

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
          <Grid item xs={10} md={8}>
            <Stack container direction="column"
              justifyContent="flex-start"
              alignItems="center">
              <Grid spacing={2} container>
                <Grid item xs={6}>
                  <DashElement link="/learningPath" heading="zuletzt" title="Halstaed C++ Übung" subtitle="Qualitätssicherung durch Metriken" buttonText="weiter" text="1/10 bearbeitet" />
                </Grid>
                <Grid item xs={6}>
                  <DashElement link="/learningPath" heading="vorgeschlagen" title="Metriken 1" subtitle="Qualitätssicherung durch Metriken" buttonText="weiter" text="4/10 bearbeitet" />
                </Grid>
              </Grid>
              <Card sx={{ height: '100%', width: '100%', marginTop: '2rem' }}>
                <Box sx={{ height: '100%', width: '100%', padding: '1rem 6rem 1rem 1rem' }}>
                  <Typography variant="h6" gutterBottom component="div">
                    Laut dem ILS Fragebogen sind die Dimensionen Deines Lernstils:
                  </Typography>
                  <CustomBarChart />
                </Box>
              </Card>
            </Stack>
          </Grid>
          <Grid item xs={2} md={4}>
            <Card sx={{ height: '100%' }}>
              <img src={logo} width="100px" alt="logo" style={{ margin: '1rem', position: 'absolute' }} />
              <Stack
                direction="column"
                justifyContent="space-between"
                alignItems="center"
                spacing={2}
                sx={{ height: '100%' }}
              >
                <div></div>
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
        {/* <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Welcome to the HASKI project!
          </p>
          <br />
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/courseDashboard">Course Dashboard</Link>
            </li>
            <li>
              <Link to="/quiz">Finde deinen Lerntypen heraus</Link>
            </li>
            <li>
              <Link to="/learningPath">Lernpfad ansehen</Link>
            </li>
            <li>
              <Link to="/theme">Theme presentation</Link>
            </li>
          </ul>
        </header>
      </div> */}
      </Stack>
    </>
  );
};

export default Home;