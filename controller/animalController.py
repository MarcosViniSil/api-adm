from fastapi import APIRouter, Depends

from models.animal import RegisterAnimal
from models.dependencies import getAnimalService
from service.animalService import AnimalService
from service.userService import UserService

animalRouter = APIRouter()

@animalRouter.post("/animal")
async def create_animal(registerAnimal:RegisterAnimal,animalService: AnimalService = Depends(getAnimalService)):
    return animalService.createAnimal(registerAnimal)

