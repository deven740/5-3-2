import React from "react";
import "./App.css";
import Cards from "./Cards";
import Players from "./Players";
import Self from "./Self";

function Play() {
  return (
    <div className="play">
      <div className="table">
        <Players />
        <Self />
      </div>
      <div className="player-cards">
        <Cards />
      </div>
    </div>
  );
}

export default Play;
