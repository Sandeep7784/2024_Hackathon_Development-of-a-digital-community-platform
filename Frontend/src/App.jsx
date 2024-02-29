import React, { useState } from "react";
import SignIn from "./components/Signin";
import SignUp from "./components/Signup";
import Header from "./components/Header";
import User from "./components/User";
import QuestHistory from "./components/QuestHistory";
import PendingRequests from "./components/PendingRequests";
import CommunityUser from "./components/CommunityUser";
import AddQuest from "./components/AddQuest";
import SearchResults from "./components/SearchResults";
import TransferList from "./components/TransferList";
import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signin" element={<SignIn />} /> 
        <Route path="/signup" element={<SignUp />} />
        <Route path="/user" element={<User />} />
        <Route path="/questHistory" element={<QuestHistory />} />
        <Route path="/community-manager" element={<CommunityUser />} />
        <Route path="/addQuest" element={<AddQuest />} />
        <Route path="/pendingRequests" element={<PendingRequests />} />
        <Route path="/searchResults" element={<SearchResults />} />
        <Route path="/transferList" element={<TransferList />} />
      </Routes>
    </Router>
  );
}

export default App;
