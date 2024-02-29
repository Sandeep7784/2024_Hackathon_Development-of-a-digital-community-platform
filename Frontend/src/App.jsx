import React, { useState } from "react";
import SignIn from "./components/Signin";
import SignUp from "./components/Signup";
import Header from "./components/Header";
import User from "./components/User";
import QuestHistory from "./components/QuestHistory";
import PendingRequests from "./components/PendingRequests";
import "./App.css";

function App() {
  return (
    <React.Fragment>
      <Header />
      <SignIn />
      <SignUp />
      {/* <User /> */}
      {/* <QuestHistory /> */}
      <PendingRequests />
    </React.Fragment>
  );
}

export default App;
