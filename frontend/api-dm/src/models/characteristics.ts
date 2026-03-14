import type { Animal } from "./animal"

export class Characteristics{
    habitat!:string
    region!:string
    practice!:string
    habits!:string
    location!:Location
    location_description!:string
}

export class Location{
    latitude!:number
    longitude!:number
}

export class CreateAnimalModel{
    animal!:Animal
    characteristics!:Characteristics
}

