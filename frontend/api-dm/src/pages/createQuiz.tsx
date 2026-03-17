import React, { useState } from "react";
import "../styles/quiz.style.css";
import { Toaster, toast } from "sonner";
import { getAnimalNameAndId } from "../services/animal.service";
import type { AnimalNameAndId } from "../models/animal";
import { useEffect } from "react";
import type { Question, QuizRequest } from "../models/question";
import { createQuiz } from "../services/quizService";

const CreateQuiz: React.FC = () => {

  const [statement, setStatement] = useState("");
  const [possibilities, setPossibilities] = useState("");
  const [options, setOptions] = useState<Question[]>([]);
  const [animalOptions, setAnimalOptions] = useState<AnimalNameAndId[]>([]);
  const [responseDetails, setResponseDetails] = useState("");
  const [isFetching, setIsFetching] = useState(false);
  const [questionCount, setQuestionCount] = useState(1);
  const [animalId, setAnimalId] = useState(-1);
  const [answer, setAnswer] = useState(-1);

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

    let quiz:QuizRequest = {
        questionStatement:statement,
        questionPossibilities: JSON.stringify(options),
        answerId:answer,
        answerDetails:responseDetails,
        animalId:animalId
    }
    console.log(quiz)
    await createQuiz(quiz)
    sendSuccess("Questão criada com sucesso",-1)
    setTimeout(() => {
        window.location.reload()

    },1500)
    } catch (err:any) {
      if(err.Error){
        console.log(err.Error)
      }else{
        console.log(err);
      }
      
      sendError(String(err), -1);
    } finally {
      setIsFetching(false);
    }
  };

  useEffect(() => {
    getAnimalDetails();
  }, []);

  const addAlternative = (question: string) => {
    let questionModel: Question = {
      id: questionCount,
      value: question,
    };

    options.forEach(e => {
       if (e.value == question){
        sendError("Esta alternativa já existe",-1)
        throw Error("Opção inválida")
       }
    })

    console.log("aaaaa")

    

    setQuestionCount(questionCount + 1);
    setOptions([...options, questionModel]);
    setPossibilities("");
  };

  const getAnimalDetails = async () => {
    try {
      if (isFetching) {
        return;
      }
      setIsFetching(true);
      let animalDetails = await getAnimalNameAndId();
      setAnimalOptions(animalDetails);
    } catch (err) {
      console.log(err);
    } finally {
      setIsFetching(false);
    }
  };

  const handleAnswerChange = (event:any) => {
    setAnswer(event.target.value);
  }

const handleAnimalIdChange = (event:any) => {
    setAnimalId(event.target.value);
  }

  return (
    <div className="auth-container1">
      <Toaster position="top-right" />
      <form className="auth-card1" onSubmit={handleSubmit}>
        <h2>Cadastro de questão</h2>

        <input
          type="text"
          placeholder="Enunciado da questão"
          value={statement}
          onChange={(e) => setStatement(e.target.value)}
          required
        />

        <p className="section-title1">Alternativas</p>

        <div className="alternatives-container">
         <div className="inputAndButtonQuestion">

         
          <input
            type="text"
            placeholder="Digite uma alternativa"
            value={possibilities}
            onChange={(e) => setPossibilities(e.target.value)}
          />

          <button
            type="button"
            className="add-btn1"
            onClick={() => addAlternative(possibilities)}
          >
            Adicionar alternativa
          </button>
          </div>

          {options.map((option) => (
            <div key={option.id} className="alternative-item1">
              <p>{option.value}</p>
              <button
                type="button"
                className="remove-btn1"
                onClick={() =>
                  setOptions(options.filter((q) => q.id !== option.id))
                }
              >
                Remover
              </button>
            </div>
          ))}
        </div>


        {(() => {
          return (
            <select name="response" id="response" onChange={handleAnswerChange}>
              <option value="" disabled selected>
                Selecione a resposta correta
              </option>
              {options.map((option) => (
                <option key={option.id} value={option.id}>
                  {option.value}
                </option>
              ))}
            </select>
          );
        })()}
        <input
          type="text"
          placeholder="Detalhes da resposta"
          value={responseDetails}
          onChange={(e) => setResponseDetails(e.target.value)}
          required
        />
        {(() => {
          return (
            <select name="animalId" id="animalId"  onChange={handleAnimalIdChange}>
              <option value="" disabled selected>
                Selecione o animal relacioando à pergunta
              </option>
              {animalOptions.map((option) => (
                <option key={option.id} value={option.id}>
                  {option.name}
                </option>
              ))}
            </select>
          );
        })()}
        <button className="add-btn1" type="submit">Entrar</button>
      </form>
    </div>
  );
};

export default CreateQuiz;
