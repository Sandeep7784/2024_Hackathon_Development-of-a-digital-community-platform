import React from "react";
import Header from "./Header";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardActionArea from "@mui/material/CardActionArea";
import CardContent from "@mui/material/CardContent";

function PendingRequests(props) {
  const { info } = props;
  return (
    <React.Fragment>
      <Header />
      <Grid item xs={12} md={6}>
        <CardActionArea>
          <Card sx={{ display: "flex" }}>
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
          </Card>
        </CardActionArea>
      </Grid>
    </React.Fragment>
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
  return (
    <React.Fragment>
      <h1 style={{ marginBottom: "40px" }}>Pending Request's</h1>
      <Grid container spacing={3}>
        {pendingRequests.map((request, index) => (
          <PendingRequests key={index} info={request} />
        ))}
      </Grid>
    </React.Fragment>
  );
}

export default PendingRequestsPage;
