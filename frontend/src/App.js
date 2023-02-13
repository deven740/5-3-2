import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import "./App.css";
import InputBox from "./Room";
import Play from "./Play";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<InputBox />} />
          <Route path="/play" element={<Play />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
