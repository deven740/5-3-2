import React, { useState, useCallback, useEffect } from "react";
import Cards from "./Cards";
import Players from "./Players";
import Self from "./Self";
import { useLocation } from "react-router-dom";
import useWebSocket, { ReadyState } from "react-use-websocket";

function Play() {
  const { state } = useLocation();
  const { roomId, playerName } = state;
  const [socketUrl, setSocketUrl] = useState(
    `ws://localhost:8000/ws?player_name=${playerName}&room_id=${roomId}`
  );
  console.log(state);
  const { sendMessage, lastMessage, readyState } = useWebSocket(socketUrl);

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
// import React, { useState, useCallback, useEffect } from 'react';
// import useWebSocket, { ReadyState } from 'react-use-websocket';

// export const WebSocketDemo = () => {
//   //Public API that will echo messages sent to it back to the client
//   const [socketUrl, setSocketUrl] = useState('wss://echo.websocket.org');
//   const [messageHistory, setMessageHistory] = useState([]);

//   const { sendMessage, lastMessage, readyState } = useWebSocket(socketUrl);

//   useEffect(() => {
//     if (lastMessage !== null) {
//       setMessageHistory((prev) => prev.concat(lastMessage));
//     }
//   }, [lastMessage, setMessageHistory]);

//   const handleClickChangeSocketUrl = useCallback(
//     () => setSocketUrl('wss://demos.kaazing.com/echo'),
//     []
//   );

//   const handleClickSendMessage = useCallback(() => sendMessage('Hello'), []);

//   const connectionStatus = {
//     [ReadyState.CONNECTING]: 'Connecting',
//     [ReadyState.OPEN]: 'Open',
//     [ReadyState.CLOSING]: 'Closing',
//     [ReadyState.CLOSED]: 'Closed',
//     [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
//   }[readyState];

//   return (
//     <div>
//       <button onClick={handleClickChangeSocketUrl}>
//         Click Me to change Socket Url
//       </button>
//       <button
//         onClick={handleClickSendMessage}
//         disabled={readyState !== ReadyState.OPEN}
//       >
//         Click Me to send 'Hello'
//       </button>
//       <span>The WebSocket is currently {connectionStatus}</span>
//       {lastMessage ? <span>Last message: {lastMessage.data}</span> : null}
//       <ul>
//         {messageHistory.map((message, idx) => (
//           <span key={idx}>{message ? message.data : null}</span>
//         ))}
//       </ul>
//     </div>
//   );
