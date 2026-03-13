from db.connection import ConnectionDB
from repository.animalRepository import AnimalRepository
from repository.userRepository import UserRepository
from service.animalService import AnimalService
from service.userService import UserService

db = ConnectionDB()
userRepository = UserRepository(db)
userService = UserService(userRepository)

animalRepository = AnimalRepository(db)
animalService = AnimalService(animalRepository)

def getUserService():
    return userService

def getAnimalService():
    return animalService