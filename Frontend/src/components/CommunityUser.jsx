import React from "react";
import Header from "./Header";
import Stack from "@mui/material/Stack";
import { Button } from "@mui/material";
import AssignmentTurnedInIcon from "@mui/icons-material/AssignmentTurnedIn";
import ContactSupportIcon from "@mui/icons-material/ContactSupport";
import CreateIcon from "@mui/icons-material/Create";
import { useNavigate } from "react-router-dom";

export default function User() {
  const navigate = useNavigate();

  const pastQuestHandleButtonClick = () => {
    navigate("/questHistory");
  };

  const addQuestHandleButtonClick = () => {
    navigate("/addQuest");
  };

  return (
    <React.Fragment>
      <Header />
      <section className="flex justify-center items-center h-screen mb-12 md:mb-48 py-16 md:py-24">
        <div className="container mx-auto text-center">
          <h2 className="font-bold leading-tight text-gray-900 text-4xl md:text-5xl lg:text-6xl mb-4 md:mb-8">
            Hello Mr. XYZ Singh
            {/* <span className="text-gradient"> SaaS Founders</span> */}
          </h2>

          <div className="max-w-3xl mx-auto">
            <p className="text-gray-800 text-lg md:text-xl mt-4 md:mt-6 mb-8">
              Comprehensive Solutions for Aspiring Opportunity Seekers
            </p>
          </div>
          <div
            className="flex items-center justify-center md:justify-start mt-6"
            style={{
              marginTop: "1.5rem",
              display: "flex",
              flexDirection: "row",
              justifyContent: "center", // Center horizontally
              alignItems: "center", // Center vertically
            }}
          >
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
                Link
                onClick={pastQuestHandleButtonClick}
              >
                Quest's History
              </Button>
              <Button
                variant="contained"
                size="large"
                startIcon={<ContactSupportIcon />}
                disableElevation
                onClick={addQuestHandleButtonClick}
              >
                Pending Request's
              </Button>
            </Stack>
          </div>
        </div>
      </section>
    </React.Fragment>
  );
}
