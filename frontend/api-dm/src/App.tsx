import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import CreateAnimal from "./pages/CreateAnimal";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/animal" element={<CreateAnimal />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;