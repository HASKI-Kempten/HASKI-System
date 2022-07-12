import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import AccountCircle from '@mui/icons-material/AccountCircle';
import Switch from '@mui/material/Switch';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormGroup from '@mui/material/FormGroup';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import { Breadcrumbs, Grid } from '@mui/material';
import MLink from '@mui/material/Link';
import HomeIcon from '@mui/icons-material/Home';
import ChangeUserDialog from './Dialogs/ChangeUserDialog';

export default function MenuAppBar({ handler, user }) {
  const [auth, setAuth] = React.useState(true);
  const [anchorEl, setAnchorEl] = React.useState(null);


  const handleChange = (event) => {
    setAuth(event.target.checked);
  };

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <>
      <Box sx={{ flexGrow: 1 }}>
        {/* <FormGroup>
        <FormControlLabel
          control={
            <Switch
              checked={auth}
              onChange={handleChange}
              aria-label="login switch"
            />
          }
          label={auth ? 'Logout' : 'Login'}
        />
      </FormGroup> */}
        <AppBar position="static" color='secondary'>
          <Toolbar>
            <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 2 }}
            >
              <MenuIcon />
            </IconButton>
            <Grid
              container
              direction="row"
              justifyContent="space-between"
              alignItems="center"
            >
              <Grid item>
                <Typography variant="h4" component="div" sx={{ flexGrow: 1 }}>
                  <div role="presentation" >
                    <Breadcrumbs aria-label="breadcrumb" color="inherit">
                      <MLink
                        underline="hover"
                        sx={{ display: 'flex', alignItems: 'center' }}
                        color="inherit"
                        href="/"
                      >
                        <HomeIcon sx={{ mr: 0.5 }} fontSize="inherit" />
                        Dashboard
                      </MLink>
                      <MLink
                        underline="hover"
                        sx={{ display: 'flex', alignItems: 'center' }}
                        color="inherit"
                      >
                        Wirtschaftsinformatik I
                      </MLink>
                      <MLink
                        underline="hover"
                        sx={{ display: 'flex', alignItems: 'center' }}
                        color="inherit"
                      >
                        Qualitätssicherung durch Metriken
                      </MLink>
                      <Typography
                        sx={{ display: 'flex', alignItems: 'center' }}
                        color="grey"
                      >

                        Metriken
                      </Typography>
                    </Breadcrumbs>

                  </div>
                </Typography>
              </Grid>
              <Grid item>
                {auth && (
                  <Grid container spacing={2}
                    direction="row"
                    justifyContent="flex-end"
                    alignItems="center">
                    <Grid item>
                      <Typography >{user}</Typography>
                    </Grid>
                    <Grid item>
                      <IconButton
                        size="large"
                        aria-label="account of current user"
                        aria-controls="menu-appbar"
                        aria-haspopup="true"
                        onClick={handleMenu}
                        color="inherit"
                      >
                        <AccountCircle />
                      </IconButton>
                    </Grid>
                    <Menu
                      id="menu-appbar"
                      anchorEl={anchorEl}
                      anchorOrigin={{
                        vertical: 'top',
                        horizontal: 'right',
                      }}
                      keepMounted
                      transformOrigin={{
                        vertical: 'top',
                        horizontal: 'right',
                      }}
                      open={Boolean(anchorEl)}
                      onClose={handleClose}
                    >
                      <MenuItem onClick={handleClose}>Profil</MenuItem>
                      <MenuItem onClick={handleClose}>Mein Account</MenuItem>
                      <MenuItem onClick={() => handler(true)}>Nutzer wechseln</MenuItem>
                      <MenuItem onClick={handleClose}><FormGroup>
                        <FormControlLabel
                          control={
                            <Switch
                              checked={auth}
                              onChange={handleChange}
                              aria-label="login switch"
                            />
                          }
                          label={auth ? 'Ausloggen' : 'Einloggen'}
                        />
                      </FormGroup></MenuItem>
                    </Menu>

                  </Grid>
                )}
              </Grid>
            </Grid>
          </Toolbar>
        </AppBar>
      </Box>
    </>
  );
}
