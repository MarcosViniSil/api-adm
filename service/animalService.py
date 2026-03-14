from fastapi import HTTPException
import re
from models.animal import Animal, AnimalCharacteristics, AnimalList, AnimalLocation, Characteristics, RegisterAnimal
from models.user import User, UserLogin
from repository.animalRepository import AnimalRepository
from security.hash import createHashForPassword,isPasswordEqualDB
from security.jwtService import createJwtToken

class AnimalService:

    def __init__(self,animalRepository:AnimalRepository):
        self.animalRepository = animalRepository

    
    
    def createAnimal(self, registerAnimal:RegisterAnimal):

        self.validateAnimal(registerAnimal.animal)
        self.validateCharacteristics(registerAnimal.characteristics)

        self.animalRepository.Db.createConnection()

        try:
            characteristicsId = self.animalRepository.createCharacteristics(
                registerAnimal.characteristics
            )

            self.animalRepository.createAnimal(
                registerAnimal.animal,
                characteristicsId
            )

            self.animalRepository.Db.myDb.commit()

        except Exception as e:
            print(e)
            self.animalRepository.Db.myDb.rollback()

            raise HTTPException(
                status_code=400,
                detail="Ocorreu um erro ao criar animal"
            )

        finally:
            self.animalRepository.Db.closeConnection()

        return {"message": "Animal cadastrado com sucesso"}
    
    def getAnimals(self,offset:int) -> list[AnimalList]:
        if offset < 0:
            raise HTTPException(status_code=400, detail="Offset deve ser maior ou igual a 0.")
        
        try:
            animals = self.animalRepository.getAnimals(offset)
            animalsList = []
            for animal in animals:
                animalsList.append(AnimalList(id=animal[1],name=animal[0],imageUrl=animal[2],height=animal[3],weight=animal[4]))
            
            return animalsList

        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Ocorreu um erro ao buscar dados dos animais.")
    
    def deleteAnimalById(self, animalId:int) -> dict:
        if animalId <= 0:
            raise HTTPException(status_code=400, detail="Id deve ser maior que 0")
        
        try:
            self.animalRepository.deleteAnimalById(animalId)
            return {"message":"animal deletado com sucessp"}

        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Ocorreu um erro ao deletar animal.")
        

    def getAnimalCharacteristics(self,animalId:int) -> AnimalCharacteristics:
        if animalId <= 0:
            raise HTTPException(status_code=400, detail="id deve ser maior que 0")
            
        characteristics = self.animalRepository.getAnimalCharacteristics(animalId)
        if characteristics is None:
            raise HTTPException(status_code=404, detail="O animal informado não existe")
        print(characteristics)
        try:
            return AnimalCharacteristics(id=characteristics[0],name=characteristics[1],imageUrl=characteristics[2],height=characteristics[3],weight=characteristics[4],habitat=characteristics[5],habits=characteristics[6],practice=characteristics[7],region=characteristics[8])

        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Ocorreu um erro ao buscar dados do animal.")
    
    def getAnimalsLocation(self,offset:int) -> list[AnimalLocation]:
        if offset < 0:
            raise HTTPException(status_code=400, detail="offset deve ser maior ou igual a 0")
            
        locations = self.animalRepository.getAnimalsLocation(offset)
        try:
            locationList = []
            for location in locations:
                locationList.append(AnimalLocation(id=location[0],name=location[1],imageUrl=location[2],location=location[3],locationDescription=location[4]))
            
            return locationList

        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Ocorreu um erro ao buscar dados do animal.")

    def validateAnimal(self, animal: Animal) -> None:
        if not animal.name.strip():
            raise HTTPException(status_code=400, detail="Nome vazio.")

        if not animal.image_url or not re.match(r"^https?://.+\.(jpg|jpeg|png|gif|svg)$", animal.image_url, re.IGNORECASE):
            raise HTTPException(status_code=400, detail="URL da imagem inválida.")

        if not animal.color.strip():
            raise HTTPException(status_code=400, detail="Cor vazia.")
        
        if not animal.height.strip():
            raise HTTPException(status_code=400, detail="Altura vazia")
        
        if not animal.weight.strip():
            raise HTTPException(status_code=400, detail="Peso vazio")

    
    def validateCharacteristics(self, characteristics: Characteristics) -> None:
        if not characteristics.habitat.strip():
            raise HTTPException(status_code=400, detail="Habitat vazio.")

        if not characteristics.region.strip():
            raise HTTPException(status_code=400, detail="Região vazia.")

        if not characteristics.practice.strip():
            raise HTTPException(status_code=400, detail="Prática vazia.")
        
        if not characteristics.location_description.strip():
            raise HTTPException(status_code=400, detail="Descrição da localização vazia.")

        if not characteristics.habits.strip():
            raise HTTPException(status_code=400, detail="Hábitos vazio.")
        
        if not isinstance(characteristics.location.latitude, (int, float)):
            raise HTTPException(status_code=400, detail="Latitude deve ser um número.")
        
        if not isinstance(characteristics.location.longitude, (int, float)):
            raise HTTPException(status_code=400, detail="Longitude deve ser um número.")


