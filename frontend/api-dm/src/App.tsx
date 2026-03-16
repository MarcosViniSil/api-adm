import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import CreateAnimal from "./pages/CreateAnimal";
import { Link } from "react-router-dom";
import CreateQuiz from "./pages/createQuiz";

function App() {
  return (
    <BrowserRouter>
    <nav>
      <Link className="linkTo" to={"/animal"}>Home</Link>
      <Link className="linkTo" to={"/login"}>Login</Link>
      <Link className="linkTo" to={"/register"}>Register</Link>
      <Link className="linkTo" to={"/question"}>Question</Link>
    </nav>
    
      <Routes>
        <Route path="/" element={<CreateAnimal />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/animal" element={<CreateAnimal />} />
        <Route path="/question" element={<CreateQuiz />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;