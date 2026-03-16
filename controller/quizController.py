from fastapi import APIRouter, Cookie, Depends
from fastapi.security import OAuth2PasswordBearer

from models.animal import RegisterAnimal
from models.dependencies import getQuizService
from models.quiz import QuizRequest, UserQuestion
from service.animalService import AnimalService
from service.quizService import QuizService
from service.userService import UserService

quizRouter = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@quizRouter.post("/quiz")
async def create_quiz(quizRequest:QuizRequest,access_token: str = Cookie(...),quizService: QuizService = Depends(getQuizService)):
    return quizService.createQuiz(access_token,quizRequest)

@quizRouter.get("/quiz")
async def get_questions(quizService: QuizService = Depends(getQuizService)):
    return quizService.listQuestions()

@quizRouter.delete("/quiz")
async def delete_question(quizId:int,access_token: str = Cookie(...),quizService: QuizService = Depends(getQuizService)):
    return quizService.deleteQuestionById(access_token,quizId)

@quizRouter.get("/quiz/list")
async def get_user_questions(animalId:int,access_token: str = Cookie(...),quizService: QuizService = Depends(getQuizService)):
    return quizService.getUserQuestions(access_token,animalId)

@quizRouter.post("/quiz/answer")
async def create_quiz(userAnswer:UserQuestion,access_token: str = Cookie(...),quizService: QuizService = Depends(getQuizService)):
    return quizService.registerUserAnswer(access_token,userAnswer)

