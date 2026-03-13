from db.connection import ConnectionDB
from models.animal import Animal, Characteristics
import json

class AnimalRepository:

    def __init__(self, db: ConnectionDB):
        self.Db = db

    def createCharacteristics(self, characteristics: Characteristics) -> int:
        
        location_json = json.dumps(characteristics.location.model_dump())
        
        sql = """
        INSERT INTO tb_characteristics
        (habitat,region,practice,habits,location,location_description)
        VALUES (%s,%s,%s,%s,%s,%s);
        """

        self.Db.myCursor.execute(sql, (
            characteristics.habitat,
            characteristics.region,
            characteristics.practice,
            characteristics.habits,
            location_json,
            characteristics.location_description
        ))

        return self.Db.myCursor.lastrowid


    def createAnimal(self, animal: Animal, characteristicsId: int):

        sql = """
        INSERT INTO tb_animal
        (animal_name,animal_imagem_url,animal_color,animal_height,animal_weight,caracteristics_id)
        VALUES (%s,%s,%s,%s,%s,%s);
        """

        self.Db.myCursor.execute(sql, (
            animal.name,
            animal.image_url,
            animal.color,
            animal.height,
            animal.weight,
            characteristicsId
        ))
        
    
        
