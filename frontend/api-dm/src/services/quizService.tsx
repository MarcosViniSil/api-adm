import type { QuizRequest } from '../models/question';

const API_URL = import.meta.env.VITE_API_URL;

export async function createQuiz(quiz:QuizRequest) {
    try {
        const response = await fetch(`${API_URL}/quiz`, {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(quiz),
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData?.detail || "Erro ao realizar criação de questão");
        }

        return response.json();
    } catch (error) {
        throw error;
    }
}

