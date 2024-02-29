// import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardActionArea from "@mui/material/CardActionArea";
import CardContent from "@mui/material/CardContent";
// import { useState } from "react";
import Header from "./Header";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
} from "@mui/material";
import CheckCircleIcon from "@mui/icons-material/CheckCircle"; // Material-UI check circle icon
import HourglassEmptyIcon from "@mui/icons-material/HourglassEmpty"; // Material-UI hourglass icon for pending tasks
import React, { useEffect, useState } from 'react';


function QuestHistory(props) {
  const { info } = props;
  const [open, setOpen] = useState(false);
  
  const handleOpen = () => {
    setOpen(true);
  };
  
  const handleClose = () => {
    setOpen(false);
  };
  return (
    <React.Fragment>
      <Header />
      <Grid item xs={12} md={6}>
        <CardActionArea onClick={handleOpen}>
          <Card sx={{ display: "flex" }}>
            <CardContent sx={{ flex: 1 }}>
              <Typography component="h2" variant="h5">
                Quest Name: {info.questName}
              </Typography>
              <Typography variant="subtitle1" color="text.secondary">
                Date Applied: {info.dateApplied}
              </Typography>
              <Typography variant="subtitle1" color="text.secondary">
                Date Assigned: 30 February
              </Typography>
              <Typography variant="subtitle1" color="text.secondary">
                Status: {info.status}
              </Typography>
              <Typography variant="subtitle1" color="text.secondary">
                Tasks Completed: {info.tasksCompleted}
              </Typography>
              <Typography variant="subtitle1" color="text.secondary">
                Tasks Remaining: {info.tasksRemaining}
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
                      Completed Tasks
                    </Typography>
                  }
                  />
              </ListItem>
              {info.completedTasks.map((task, index) => (
                <ListItem key={index}>
                  <ListItemIcon>
                    <CheckCircleIcon style={{ color: "green" }} />
                  </ListItemIcon>
                  <ListItemText primary={task} />
                </ListItem>
              ))}
              <ListItem>
                <ListItemText
                  primary={
                    <Typography variant="subtitle1" fontWeight="bold">
                      Pending Tasks
                    </Typography>
                  }
                  />
              </ListItem>
              {info.pendingTasks.map((task, index) => (
                <ListItem key={index}>
                  <ListItemIcon>
                    <HourglassEmptyIcon color="primary" />
                  </ListItemIcon>
                  <ListItemText primary={task} />
                </ListItem>
              ))}
            </List>
          </DialogContent>
        </Dialog>
      </Grid>
    </React.Fragment>
  );
}

const blogCards = [
  {
    questName: "Seeking the Lost Treasure",
    dateApplied: "January 15, 2024",
    status: "In Progress",
    tasksCompleted: 4,
    tasksRemaining: 6,
    completedTasks: [
      "Find map to treasure",
      "Cross the river",
      "Discover hidden cave",
    ],
    pendingTasks: [
      "Retrieve ancient artifact",
      "Defeat guardians",
      "Escape with treasure",
    ],
  },
  {
    questName: "Defeating the Dragon",
    dateApplied: "February 5, 2024",
    status: "Completed",
    tasksCompleted: 10,
    tasksRemaining: 0,
    completedTasks: [
      "Train for battle",
      "Gather supplies",
      "Forge legendary sword",
    ],
    pendingTasks: [],
  },
  {
    questName: "Rescuing the Princess",
    dateApplied: "March 20, 2024",
    status: "Pending",
    tasksCompleted: 2,
    tasksRemaining: 8,
    completedTasks: ["Scout enemy fortress", "Infiltrate castle"],
    pendingTasks: ["Locate princess", "Evade traps", "Confront villain"],
  },
  {
    questName: "Exploring the Forbidden Forest",
    dateApplied: "April 10, 2024",
    status: "In Progress",
    tasksCompleted: 6,
    tasksRemaining: 4,
    completedTasks: ["Navigate through dense foliage", "Discover hidden ruins"],
    pendingTasks: [
      "Bypass enchanted barrier",
      "Find ancient artifact",
      "Escape wild creatures",
    ],
  },
  {
    questName: "Conquering the Dark Tower",
    dateApplied: "May 5, 2024",
    status: "Pending",
    tasksCompleted: 1,
    tasksRemaining: 9,
    completedTasks: ["Gather allies"],
    pendingTasks: [
      "Ascend tower",
      "Defeat dark sorcerer",
      "Destroy source of evil",
    ],
  },
  {
    questName: "Uncovering the Ancient Ruins",
    dateApplied: "June 18, 2024",
    status: "In Progress",
    tasksCompleted: 3,
    tasksRemaining: 7,
    completedTasks: ["Decode ancient language", "Excavate ruins"],
    pendingTasks: [
      "Find hidden chamber",
      "Unlock secrets",
      "Guard against traps",
    ],
  },
];

function BlogList() {
  const [history, setHistory] = useState([]);
  
  useEffect(() => {
    setHistory([]);
    const cookies = localStorage.getItem('imp_cookie');
    const user_type = localStorage.getItem('user_type');
    console.log(cookies)
    
    fetch("http://127.0.0.1:8000/history/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ cookie: cookies, user_type: user_type})
    })
    .then((response) => response.json())
    .then((data) => {
      setHistory(data);
      })
      .catch((error) => {
        console.error("Error fetching history:", error);
      });
  }, []);

  return (
    <React.Fragment>
      <h2>Quest's History </h2>
      <Grid container spacing={3}>
        {blogCards.map((blog, index) => (
          <QuestHistory key={index} info={blog} />
        ))}
      </Grid>
    </React.Fragment>
  );
}

export default BlogList;
