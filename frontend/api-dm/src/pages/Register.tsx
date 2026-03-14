import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../styles/auth.css";
import { Toaster, toast } from "sonner";
import { createUser } from "../services/register.service";
import type { User } from "../models/user";

const Register: React.FC = () => {
  const [name, setName] = useState("");
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
      await createUser(createUserModel());

      sendSuccess("Cadastro realizado com sucesso",-1)
    } catch (err) {
      console.log(err);
      sendError(String(err),-1)
    }finally{
      setIsFetching(false)
    }
  };

  const createUserModel = () => {
    const user: User = {
      name,
      email,
      password,
    };

    return user;
  };

  return (
    <div className="auth-container">
    <Toaster position="top-right" />
      <form className="auth-card" onSubmit={handleSubmit}>
        <h2>Registrar</h2>

        <input
          type="text"
          placeholder="Nome"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

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

        <button type="submit">Criar conta</button>

        <p>
          Já possui conta? <Link to="/login">Login</Link>
        </p>
      </form>
    </div>
  );
};

export default Register;
