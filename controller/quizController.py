from fastapi import APIRouter, Cookie, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer

from models.animal import RegisterAnimal
from models.dependencies import getQuizService
from models.quiz import QuizRequest, UserQuestion
from service.animalService import AnimalService
from service.quizService import QuizService
from service.userService import UserService

quizRouter = APIRouter()

security = HTTPBearer()

@quizRouter.post("/quiz")
async def create_quiz(quizRequest:QuizRequest,credentials: HTTPAuthorizationCredentials = Depends(security),quizService: QuizService = Depends(getQuizService)):
    return quizService.createQuiz(credentials.credentials,quizRequest)

@quizRouter.get("/quiz")
async def get_questions(quizService: QuizService = Depends(getQuizService)):
    return quizService.listQuestions()

@quizRouter.delete("/quiz")
async def delete_question(quizId:int,credentials: HTTPAuthorizationCredentials = Depends(security),quizService: QuizService = Depends(getQuizService)):
    return quizService.deleteQuestionById(credentials.credentials,quizId)

@quizRouter.get("/quiz/list")
async def get_user_questions(animalId:int,credentials: HTTPAuthorizationCredentials = Depends(security),quizService: QuizService = Depends(getQuizService)):
    return quizService.getUserQuestions(credentials.credentials,animalId)

@quizRouter.post("/quiz/answer")
async def create_quiz(userAnswer:UserQuestion,credentials: HTTPAuthorizationCredentials = Depends(security),quizService: QuizService = Depends(getQuizService)):
    return quizService.registerUserAnswer(credentials.credentials,userAnswer)

