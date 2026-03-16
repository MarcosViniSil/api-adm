import type { CreateAnimalModel } from "../models/characteristics";

const API_URL = import.meta.env.VITE_API_URL;

export async function createAnimal(animal:CreateAnimalModel) {
    console.log(animal)
    try {
        const response = await fetch(`${API_URL}/animal`, {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(animal),
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

export async function getAnimalNameAndId() {
    try {
        const response = await fetch(`${API_URL}/animal/details`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            },
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData?.detail || "Erro ao buscar dados dos animais");
        }

        return response.json();
    } catch (error) {
        throw error;
    }
}