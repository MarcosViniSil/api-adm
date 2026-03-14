from fastapi import APIRouter, Depends

from models.animal import RegisterAnimal
from models.dependencies import getAnimalService
from service.animalService import AnimalService
from service.userService import UserService

animalRouter = APIRouter()

@animalRouter.post("/animal")
async def create_animal(registerAnimal:RegisterAnimal,animalService: AnimalService = Depends(getAnimalService)):
    return animalService.createAnimal(registerAnimal)

@animalRouter.get("/animals")
async def get_animals(offset:int,animalService: AnimalService = Depends(getAnimalService)):
    return animalService.getAnimals(offset)

@animalRouter.get("/animal/characteristics")
async def get_animal_characteristics(animalId:int,animalService: AnimalService = Depends(getAnimalService)):
    return animalService.getAnimalCharacteristics(animalId)

@animalRouter.get("/animals/location")
async def get_animals_location(offset:int,animalService: AnimalService = Depends(getAnimalService)):
    return animalService.getAnimalsLocation(offset)

@animalRouter.delete("/animal")
async def delete_animal(animalId:int,animalService: AnimalService = Depends(getAnimalService)):
    return animalService.deleteAnimalById(animalId)

