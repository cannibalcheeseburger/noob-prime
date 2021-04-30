import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { AppWrapper } from "../context/AppContext";

import "../libs/tailwind.min.css";
import "./App.scss";
import Home from "./Home/Home";

function App() {
  return (
    <AppWrapper>
      <div className="bg-black min-h-screen text-white">
        <Router>
          <Switch>
            <Route exact path="/" component={Home} />
          </Switch>
        </Router>
      </div>
    </AppWrapper>
  );
}

export default App;
