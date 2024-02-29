import React, { useState } from "react";
import Header from "./Header";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import CardActionArea from "@mui/material/CardActionArea";
import Dialog from "@mui/material/Dialog";
import DialogContent from "@mui/material/DialogContent";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import DescriptionIcon from "@mui/icons-material/Description"; // Generic task icon

const SearchResultCard = ({ key, title, tasks,}) => {
  const [open, setOpen] = useState(false);

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleMakeRequest = async () => {
    // Call the API to make a request
    const cookies = localStorage.getItem('imp_cookies');
    await fetch('http://127.0.0.1:8000/request/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        questId: key,
        cookie: cookies
      })
    })
    .then(response => {
      if (response.ok) {
        console.log("Request sent successfully");
      } else {
        console.error("Failed to send request");
      }
    })
    .catch(error => {
      console.error("Error:", error);
    });
  };

  // Split the tasks string into an array of individual tasks
  const taskList = tasks.split(',');

  return (
    <React.Fragment>
      <Header />
      <Grid item xs={12} md={6}>
        <CardActionArea onClick={handleOpen}>
          <Card sx={{ display: "flex" }}>
            <CardContent sx={{ flex: 1 }}>
              <Typography component="h2" variant="h5">
                Quest Name: {title}
              </Typography>
              <Typography variant="subtitle1" color="text.secondary">
                Tasks: {tasks}
              </Typography>
            </CardContent>
          </Card>
        </CardActionArea>
        <Dialog open={open} onClose={handleClose}>
          <DialogContent>
            <List>
              <ListItem>
                <ListItemText
                  primary={
                    <Typography variant="subtitle1" fontWeight="bold">
                      Tasks
                    </Typography>
                  }
                />
              </ListItem>
              {/* Display each task sequentially */}
              {taskList.map((task, index) => (
                <ListItem key={index}>
                  <ListItemIcon>
                    <DescriptionIcon color="primary" /> {/* Generic task icon */}
                  </ListItemIcon>
                  <ListItemText primary={task.trim()} />
                </ListItem>
              ))}
            </List>
            <Button onClick={handleMakeRequest} variant="contained" color="primary">
              Make Request
            </Button>
          </DialogContent>
        </Dialog>
      </Grid>
    </React.Fragment>
  );
};

export default SearchResultCard;
