export class Question{
    id!:number
    value!:string
}
export class QuizRequest{
    questionStatement!:string
    questionPossibilities!:string
    answerId!:number
    answerDetails!:string
    animalId!:number
}