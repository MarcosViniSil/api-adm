from fastapi import HTTPException
import re
from models.animal import Animal, Characteristics, RegisterAnimal
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


    def validateAnimal(self, animal: Animal) -> None:
        if not animal.name.strip():
            raise HTTPException(status_code=400, detail="Nome inválido. Deve conter apenas letras e espaços.")

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


