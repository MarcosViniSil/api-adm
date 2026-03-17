import json

from fastapi import HTTPException
import re

from pydantic import Json
from models.animal import Animal, AnimalCharacteristics, AnimalList, AnimalLocation, AnimalNameAndId, Characteristics, RegisterAnimal
from models.quiz import QuestionDetails, QuestionDetailsList, QuestionFeedback, QuestionUser, Quiz, QuizRequest, UserQuestion
from models.user import User, UserLogin
from repository.quizRepository import QuizRepository
from service.animalService import AnimalService
import random

from service.userService import UserService

class QuizService:

    def __init__(self,quizRepository:QuizRepository,animalService:AnimalService,userService:UserService):
        self.quizRepository = quizRepository
        self.animalService = animalService
        self.userService = userService


    def createQuiz(self, token:str,quizRequest:QuizRequest) -> None:
        self.userService.getUserId(token)
        self.validateAnimal(quizRequest.animalId)
        self.validateStatement(quizRequest.questionStatement)
        self.validateAnswer(quizRequest.questionPossibilities,quizRequest.answerId)
        self.validateOptions(quizRequest.questionPossibilities)
        print(quizRequest.questionPossibilities)
        try:
            quiz = Quiz(questionStatement=quizRequest.questionStatement,questionPossibilities=json.dumps(
        [opt.model_dump() for opt in quizRequest.questionPossibilities]),answerId=quizRequest.answerId,answerDetails=quizRequest.answerDetails,animalId=quizRequest.animalId,questionCode=self.generateCode())
            self.quizRepository.createQuiz(quiz)
            return '{"message":"questao criada com sucesso"}'
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Ocorreu um erro ao criar questão.")
    
    def listQuestions(self) -> list[QuestionDetailsList]:
        
        try:
            questions = self.quizRepository.listAllQuestions()
            questionList = []
            for question in questions:
                 questionList.append(QuestionDetailsList(id=question[0],statement=question[1]))
            
            return questionList
            
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Ocorreu um erro ao buscar questões.")
    
    def getUserQuestions(self,token:str,animalId:int) -> list[QuestionUser]:
        userId = self.userService.getUserId(token)
        try:
            questions = self.quizRepository.getQuizPerUser(animalId=animalId,userId=userId)
            questionsList = []
            if len(questions) == 0:
                questions = self.quizRepository.getDefaultQuestions(animalId=animalId)
                for question in questions:
                    questionsList.append(QuestionUser(statement=question[0],options=question[1],code=question [2]))
                return questionsList
            else:
                for question in questions:
                    questionsList.append(QuestionUser(statement=question[0],options=question[1],code=question [2]))

            return questionsList
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Ocorreu um erro ao buscar questões.")
    
    def registerUserAnswer(self,token:str,userQuestion:UserQuestion) -> QuestionFeedback:
        userId = self.userService.getUserId(token)
        
        try:
            row = self.quizRepository.getQuestionDetailsByCode(userQuestion.questionCode)
            details = QuestionDetails(id=row[0],answerId=row[1],answerDetails=row[2])
            
            self.quizRepository.registerUserAnswer(userQuestion.userAnswer == details.answerId,userId,details.id)
            
            return QuestionFeedback(isAnswerRight=userQuestion.userAnswer == details.answerId,answerDetails=details.answerDetails)
            
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Ocorreu um erro ao registrar resposta.")
    
    def deleteQuestionById(self,token:str,questionId:int) -> None:
        self.userService.getUserId(token)
        if questionId <= 0:
            raise HTTPException(status_code=400, detail="Id deve ser maior que 0.")
        try:
            self.quizRepository.deleteQuestionById(questionId)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Ocorreu um erro ao deletar questão.")
        
    def validateStatement(self,statement:str) -> None:
        if not statement.strip():
            raise HTTPException(status_code=400, detail="Enunciado da questão é obrigatório.")
    
    def validateAnimal(self,animalId) -> None:    
        if not self.animalService.isAnimalIdExists(animalId):
            raise HTTPException(status_code=404, detail="O animal informado não existe.")

    def validateAnswer(self, options, responseId: int) -> None:
        for opt in options:
            if opt.id == responseId:
                return
        raise HTTPException(status_code=404, detail="A resposta informada não existe.")
    
    def validateOptions(self, options) -> None:
        if len(options) < 2:
            raise HTTPException(status_code=404, detail="Mínimo de 2 opções.")
    
    def generateCode(self) -> int:
        return random.randint(1000000, 9999999)
    
    
        