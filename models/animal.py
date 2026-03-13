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