export class Question{
    id!:number
    value!:string
}
export class options{
    id!:number
    value!:string
}
export class QuizRequest{
    questionStatement!:string
    questionPossibilities!:options[]
    answerId!:number
    answerDetails!:string
    animalId!:number
}