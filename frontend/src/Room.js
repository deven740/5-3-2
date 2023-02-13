import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./App.css";
import axios from "axios";

function InputBox() {
  let navigate = useNavigate();
  const [playerName, setPlayerName] = useState("");
  const [roomId, setRoomId] = useState("");

  const joinRoom = (e) => {
    console.log(roomId);
  };

  const createRoom = async (e) => {
    try {
      const { data } = await axios.get("http://localhost:8000/create_room");
      const roomID = data.room_id;
      window.alert(`Your Room ID is ${roomID}`);
      return navigate("/play");
    } catch (err) {
      console.log(err);
    }
  };

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
          value={roomId}
          onChange={(e) => setRoomId(e.target.value)}
        />
      </div>
      <br />
      <div className="input-buttons">
        <button onClick={createRoom}>Create Room</button>
        <button onClick={joinRoom}>Join Room</button>
      </div>
    </div>
  );
}

export default InputBox;
