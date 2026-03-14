import {UserLogin} from '../models/user'

const API_URL = import.meta.env.VITE_API_URL;

export async function loginUser(user:UserLogin) {
    try {
        const response = await fetch(`${API_URL}/user/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(user),
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData?.detail || "Erro ao realizar login de usuário");
        }

        return response.json();
    } catch (error) {
        throw error;
    }
}

