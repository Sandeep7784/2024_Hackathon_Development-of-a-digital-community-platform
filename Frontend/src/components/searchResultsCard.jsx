import React from "react";
import Header from "./Header";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";

const SearchResultCard = ({ title, tasks, town, onSendRequest }) => {
  return (
    <React.Fragment>
      <Header />
      <Grid item xs={12} md={6}>
        <Card variant="outlined" style={{ marginBottom: "1rem" }}>
          <CardContent>
            <Typography variant="h5" component="div">
              {title}
            </Typography>
            <Typography variant="body1" color="text.secondary">
              Tasks: {tasks}
            </Typography>
            <Typography variant="body1" color="text.secondary">
              Town: {town}
            </Typography>
            <Button
              onClick={onSendRequest}
              variant="contained"
              color="primary"
              sx={{ mt: 1 }}
            >
              Send Request
            </Button>
          </CardContent>
        </Card>
      </Grid>
    </React.Fragment>
  );
};

export default SearchResultCard;
