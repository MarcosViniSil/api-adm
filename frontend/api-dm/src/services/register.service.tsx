import {User} from '../models/user'

const API_URL = import.meta.env.VITE_API_URL;

export async function createUser(user:User) {
    try {
        const response = await fetch(`${API_URL}/user`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(user),
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData?.detail || "Erro ao criar usuário");
        }

        return response.json();
    } catch (error) {
        throw error;
    }
}

