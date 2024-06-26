import React, { useState, useEffect } from "react";
import Header from "./Header";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardActionArea from "@mui/material/CardActionArea";
import CardContent from "@mui/material/CardContent";
import { Fab } from "@mui/material";
import Stack from "@mui/material/Stack";
import Button from "@mui/material/Button";


function PendingRequests(props) {
  const { info } = props;
  return (
    <Grid item xs={12} md={6}>
      <Card sx={{ display: "flex", position: "relative" }}>
        <CardContent sx={{ flex: 1 }}>
          <Typography component="h2" variant="h5">
            Quest Name: {info.questName}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary">
            Date Applied: {info.dateApplied}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary">
            Status: {info.status}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary">
            Info: {info.info}
          </Typography>
        </CardContent>
        <Stack direction="row" spacing={2}>
          <Button variant="contained" color="primary">
            Approve
          </Button>
          <Button variant="contained" color="error">
            Reject
          </Button>
        </Stack>
      </Card>
    </Grid>
  );
}

const pendingRequests = [
  {
    questName: "Quest 1",
    dateApplied: "January 15, 2024",
    status: "Pending",
    info: "Additional information for Quest 1",
  },
  {
    questName: "Quest 2",
    dateApplied: "February 5, 2024",
    status: "Pending",
    info: "Additional information for Quest 2",
  },
  {
    questName: "Quest 3",
    dateApplied: "February 5, 2024",
    status: "Pending",
    info: "Additional information for Quest 2",
  },
  {
    questName: "Quest 4",
    dateApplied: "February 5, 2024",
    status: "Pending",
    info: "Additional information for Quest 2",
  },
  // Add more pending request objects here...
];

function PendingRequestsPage() {
  const [pendingRequests1, setPendingRequests] = useState([]);

  useEffect(() => {
    const cookies = localStorage.getItem('imp_cookie');

    fetch("http://127.0.0.1:8000/pending-requests/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ cookie: cookies })
    })
      .then((response) => response.json())
      .then((data) => {
        setPendingRequests(data);
      })
      .catch((error) => {
        console.error("Error fetching pending requests:", error);
      });
  }, []);

  return (
    <React.Fragment>
      <Header />
      <h1 style={{ marginBottom: "40px" }}>Pending Requests</h1>
      <Grid container spacing={3}>
        {pendingRequests.map((request, index) => (
          <PendingRequests key={index} info={request} />
        ))}
      </Grid>
    </React.Fragment>
  );
}



export default PendingRequestsPage;
