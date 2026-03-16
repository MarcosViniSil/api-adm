from pydantic import BaseModel, Json

class QuizRequest(BaseModel):
    questionStatement:str
    questionPossibilities:str
    answerId:int
    answerDetails:str
    animalId:int


class Quiz(BaseModel):
    questionStatement:str
    questionPossibilities:str
    answerId:int
    answerDetails:str
    animalId:int
    questionCode:int
    
class QuestionDetailsList(BaseModel):
    id:int
    statement:str


class QuestionUser(BaseModel):
    statement:str
    options:str
    code:int

class QuestionDetails(BaseModel):
    id:int
    answerId:int
    answerDetails:str
    
class UserQuestion(BaseModel):
    questionCode:int
    userAnswer:int
    
class QuestionFeedback(BaseModel):
    isAnswerRight:bool
    answerDetails:str