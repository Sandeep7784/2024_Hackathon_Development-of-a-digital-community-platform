import React, { useState } from "react";
import SignIn from "./components/Signin";
import SignUp from "./components/Signup";
// import Header from "./components/Header";
import "./App.css";

function App() {
  return (
    <React.Fragment>
      {/* <Header /> */}
      {/* <SignIn /> */}
      <SignUp />
    </React.Fragment>
  );
}

export default App;
