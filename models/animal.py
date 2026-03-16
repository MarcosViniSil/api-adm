from pydantic import BaseModel, Json

class Animal(BaseModel):
    name: str
    image_url:str
    color:str
    height:str
    weight:str

class Location(BaseModel):
    latitude: float
    longitude: float

class Characteristics(BaseModel):
    habitat: str
    region: str
    practice: str
    habits: str
    location: Location
    location_description:str
    
class RegisterAnimal(BaseModel):
    animal: Animal
    characteristics:Characteristics 
    
class AnimalList(BaseModel):
    id:int
    name:str
    imageUrl:str
    height:str
    weight:str
    
class AnimalCharacteristics(BaseModel):
    id:int
    name:str
    imageUrl:str
    height:str
    weight:str
    habitat:str
    habits:str
    practice:str
    region:str
    
class AnimalLocation(BaseModel):
    id:int
    name:str
    imageUrl:str
    location:Json
    locationDescription:str
    
class AnimalNameAndId(BaseModel):
    id:int
    name:str