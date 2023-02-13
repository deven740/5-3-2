import React, { useState } from "react";
import "./App.css";

function InputBox() {
  const [playerName, setPlayerName] = useState("");
  const [roomName, setRoomName] = useState("");

  return (
    <div className="input-box">
      <div className="input-fields">
        <label>Player Name:</label>
        <input
          type="text"
          value={playerName}
          onChange={(e) => setPlayerName(e.target.value)}
        />
        <br />
        <br />
        <label>Join Room:</label>
        <input
          type="text"
          value={roomName}
          onChange={(e) => setRoomName(e.target.value)}
        />
      </div>
      <br />
      <div className="input-buttons">
        <button>Create Room</button>
        <button>Join Room</button>
      </div>
    </div>
  );
}

export default InputBox;
