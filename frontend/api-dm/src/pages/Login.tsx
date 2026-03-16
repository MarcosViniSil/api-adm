import React, { useState } from "react";
import "../styles/auth.css";
import { Link } from 'react-router-dom';
import { Toaster, toast } from "sonner";
import { loginUser } from "../services/login.service";
import type { UserLogin } from "../models/user";

const Login: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isFetching, setIsFetching] = useState(false);

  const sendSuccess = (message: string, toastId: number) => {
    toast.success(`${message}`, {
      style: {
        background: "#346E62",
        color: "#fff",
      },
      id: toastId,
    });
  };

  const sendError = (message: string, toastId: number) => {
    toast.error(`${message}`, {
      style: {
        background: "#8B0000",
        color: "#fff",
      },
      id: toastId,
    });
  };

  const handleSubmit = async (e: React.SubmitEvent) => {
    e.preventDefault();

    try {
      if (isFetching) {
        return;
      }
      setIsFetching(true);
      await loginUser(createUserModel());
      sendSuccess("Login realizado com sucesso",-1)
    } catch (err) {
      console.log(err);
      sendError(String(err),-1)
    }finally{
      setIsFetching(false)
    }
  };

  const createUserModel = () => {
    const user: UserLogin = {
      email,
      password,
    };

    return user;
  };

  return (
    <div className="auth-container">
      <Toaster position="top-right" />
      <form className="auth-card" onSubmit={handleSubmit}>
        <h2>Login</h2>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Senha"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">Entrar</button>

        <p>
          Não possui conta? <Link to="/register">Registrar</Link>
        </p>
      </form>
    </div>
  );
};

export default Login;