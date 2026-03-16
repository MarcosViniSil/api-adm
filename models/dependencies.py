from db.connection import ConnectionDB
from repository.animalRepository import AnimalRepository
from repository.quizRepository import QuizRepository
from repository.userRepository import UserRepository
from service.animalService import AnimalService
from service.quizService import QuizService
from service.userService import UserService

db = ConnectionDB()
userRepository = UserRepository(db)
userService = UserService(userRepository)

animalRepository = AnimalRepository(db)
animalService = AnimalService(animalRepository,userService)

quizRepository = QuizRepository(db)
quizService = QuizService(quizRepository,animalService,userService)

def getUserService():
    return userService

def getAnimalService():
    return animalService

def getQuizService():
    return quizService