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
    
    def getAnimals(self,offset:int) -> dict:
        offset = offset * 10
        self.Db.createConnection()

        sql = """
                SELECT 
                    animal_name, 
                    MIN(id) AS id, 
                    MIN(animal_imagem_url) AS animal_imagem_url,
                    MIN(animal_height) AS animal_height,
                    MIN(animal_weight) AS animal_weight
                FROM tb_animal
                GROUP BY animal_name
                LIMIT 10 OFFSET %s;
        """
        try:
            self.Db.myCursor.execute(sql, (offset,))
            row = self.Db.myCursor.fetchall()
            self.Db.myDb.commit()
            self.Db.closeConnection()

            return row

        except Exception as e:
            print(e)
            raise ValueError("Erro obter dados dos animais", e)
        
    def getAnimalCharacteristics(self,animalId:int) -> dict:
        self.Db.createConnection()

        sql = """
            SELECT animal.id,animal.animal_name,animal.animal_imagem_url,animal.animal_height,animal.animal_weight,cha.habitat,cha.habits,cha.practice,cha.region FROM tb_animal AS animal INNER JOIN tb_characteristics AS cha ON animal.caracteristics_id = cha.id WHERE animal.id = %s;
        """
        try:
            self.Db.myCursor.execute(sql, (animalId,))
            row = self.Db.myCursor.fetchone()
            self.Db.myDb.commit()
            self.Db.closeConnection()

            return row

        except Exception as e:
            print(e)
            raise ValueError("Erro obter dados dos animais", e)
    
    def getAnimalsLocation(self,offset:int) -> dict:
        self.Db.createConnection()

        sql = """
                SELECT 
                MIN(animal.id),
                animal.animal_name,
                MIN(animal.animal_imagem_url),
                MIN(cha.location),
                MIN(cha.location_description)
                FROM tb_animal AS animal 
                INNER JOIN tb_characteristics AS cha 
                ON animal.caracteristics_id = cha.id
                GROUP BY animal_name
                LIMIT 10 OFFSET %s;
        """
        try:
            self.Db.myCursor.execute(sql, (offset,))
            row = self.Db.myCursor.fetchall()
            self.Db.myDb.commit()
            self.Db.closeConnection()

            return row

        except Exception as e:
            print(e)
            raise ValueError("Erro obter localização dos animais", e)
    
 
    def deleteAnimalById(self,animalId:int) -> None:
        self.Db.createConnection()

        sql = """
            DELETE FROM tb_animal WHERE id = %s;
        """
        try:
            self.Db.myCursor.execute(sql, (animalId,))
            self.Db.myDb.commit()
            self.Db.closeConnection()

        except Exception as e:
            print(e)
            raise ValueError("Erro deletar animal", e)
    
    def getAnimalNameAndId(self) -> dict:
        self.Db.createConnection()

        sql = """
            SELECT MIN(id) AS id,MIN(animal_name) AS name 
            FROM tb_animal 
            GROUP BY animal_name;   
        """
        try:
            self.Db.myCursor.execute(sql,())
            row = self.Db.myCursor.fetchall()
            self.Db.myDb.commit()
            self.Db.closeConnection()
            
            return row

        except Exception as e:
            print(e)
            raise ValueError("Erro buscar animais", e)
    
    def isAnimalExists(self,animalId:int) -> dict:
        self.Db.createConnection()

        sql = """
            SELECT EXISTS(SELECT 1 FROM tb_animal WHERE id = %s);  
        """
        try:
            self.Db.myCursor.execute(sql,(animalId,))
            row = self.Db.myCursor.fetchone()
            self.Db.myDb.commit()
            self.Db.closeConnection()
            
            return row

        except Exception as e:
            print(e)
            raise ValueError("Erro verificar se animal existe", e)
        
        
    
        
