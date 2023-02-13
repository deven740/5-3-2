import React from "react";
import "./App.css";
import Cards from "./Cards";

function Play() {
  return (
    <div className="play">
      <div className="table"></div>
      <div className="player-cards">
        <Cards />
      </div>
    </div>
  );
}

export default Play;
