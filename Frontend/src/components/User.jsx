import React from "react";
import Header from "./Header";
import Stack from "@mui/material/Stack";
import { Button, TextField } from "@mui/material";
import AssignmentTurnedInIcon from "@mui/icons-material/AssignmentTurnedIn";
import ContactSupportIcon from "@mui/icons-material/ContactSupport";
import Paper from "@mui/material/Paper";
import InputBase from "@mui/material/InputBase";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";

export default function User() {
  return (
    <React.Fragment>
      <Header />
      <section className="template6Hero mb-12 md:mb-48 bg-gray-100 py-16 md:py-24">
        <div className="container mx-auto text-center">
          <h1 className="font-bold leading-tight text-gray-900 text-6xl md:text-7xl lg:text-8xl mb-4 md:mb-8">
            Comprehensive Solutions for Aspiring Opportunity Seekers
            {/* <span className="text-gradient"> SaaS Founders</span> */}
          </h1>
          <div className="max-w-3xl mx-auto">
            <p className="text-gray-800 text-lg md:text-xl mt-4 md:mt-6 mb-8">
              Enter your preferred domain in the search button below to explore
              a wealth of opportunities perfectly suited to your skills and
              interests.
            </p>
          </div>
          <div className="flex flex-col items-center md:flex-row md:justify-center gap-4">
            <div className="flex items-center">
              <Paper
                component="form"
                sx={{
                  p: "2px 4px",
                  display: "flex",
                  alignItems: "center",
                }}
              >
                <InputBase
                  sx={{ ml: 1, flex: 1 }}
                  placeholder="Search for the Quests"
                  inputProps={{ "aria-label": "search google maps" }}
                />
                <Divider sx={{ height: 28, m: 0.5 }} orientation="vertical" />
                <IconButton
                  color="primary"
                  sx={{ p: "10px" }}
                  aria-label="directions"
                >
                  <SearchIcon />
                </IconButton>
              </Paper>
            </div>
            <div className="mt-6" style={{ marginTop: "1.5rem" }}>
              <Stack
                direction="row"
                spacing={2}
                alignItems="center"
                justifyContent="center"
              >
                <Button
                  variant="contained"
                  size="large"
                  startIcon={<AssignmentTurnedInIcon />}
                  disableElevation
                >
                  Quest's History
                </Button>
                <Button
                  variant="contained"
                  size="large"
                  startIcon={<ContactSupportIcon />}
                  disableElevation
                >
                  Pending Request's
                </Button>
              </Stack>
            </div>
          </div>
        </div>
      </section>
    </React.Fragment>
  );
}
