import logo from '../haski.jpeg';
import '../App.css';
import { Link } from "react-router-dom";
// import Swiper styles
import 'swiper/css';
import MenuAppBar from './MenuBar';
import ChangeUserDialog from './Dialogs/ChangeUserDialog';
import React from 'react';
import { Card, Grid, Paper, Stack } from '@mui/material';
import DashElement from './DashElement';

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
      <MenuAppBar handler={handleChangeUserDialogClick} user={user} />
      <ChangeUserDialog handler={handleChangeUserDialogClick} open={open} hanlderUser={handleChangeUser} />
      <Grid container spacing={2} marginTop="1rem" sx={{ height: '100%' }}>
        <Grid item xs={10} md={8}>
          <Stack container direction="column"
            justifyContent="flex-start"
            alignItems="center"
            spacing={2}>
            <Grid container spacing={2}>
              <Grid item xs={6}>
                <DashElement link="/learningPath" heading="zuletzt" title="Halstaed C++ Übung" subtitle="Qualitätssicherung durch Metriken" buttonText="weiter" text="1/10 bearbeitet" />
              </Grid>
              <Grid item xs={6}>
                <DashElement link="/learningPath" heading="vorgeschlagen" title="Metriken 1" subtitle="Qualitätssicherung durch Metriken" buttonText="weiter" text="4/10 bearbeitet" />
              </Grid>
            </Grid>
            <Card>
              lol
            </Card>
          </Stack>
        </Grid>
        <Grid item xs={2} md={4}>
          <Paper sx={{ height: '100%' }}>
            <img src={logo} className="App-logo" alt="logo" />
          </Paper>
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
    </>
  );
};

export default Home;