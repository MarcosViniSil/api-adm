from db.connection import ConnectionDB
from models.animal import Animal, Characteristics
import json

from models.quiz import Quiz

class QuizRepository:

    def __init__(self, db: ConnectionDB):
        self.Db = db

    def createQuiz(self, quiz: Quiz) -> int:
        
        self.Db.createConnection()
        
        sql = """
        INSERT INTO tb_question
        (question_statement,question_possibilities,answer_id,answer_details,animal_id,question_code)
        VALUES (%s,%s,%s,%s,%s,%s);
        """

        try:
            self.Db.myCursor.execute(sql, (
            quiz.questionStatement,
            quiz.questionPossibilities,
            quiz.answerId,
            quiz.answerDetails,
            quiz.animalId,
            quiz.questionCode))
            self.Db.myDb.commit()
            self.Db.closeConnection()

        except Exception as e:
            print(e)
            raise ValueError("Erro ao criar questão", e)
    
    def listAllQuestions(self) -> int:
        
        self.Db.createConnection()
        
        sql = """
            SELECT id,question_statement FROM tb_question;
        """

        try:
            self.Db.myCursor.execute(sql)
            rows = self.Db.myCursor.fetchall()
            self.Db.myDb.commit()
            self.Db.closeConnection()
            
            return rows

        except Exception as e:
            print(e)
            raise ValueError("Erro ao criar questão", e)
    
    def deleteQuestionById(self,questionId:int) -> None:
        self.Db.createConnection()
        
        sql = """
            DELETE FROM tb_question WHERE id = %s;
        """

        try:
            self.Db.myCursor.execute(sql,(questionId,))
            self.Db.myDb.commit()
            self.Db.closeConnection()
            
        except Exception as e:
            print(e)
            raise ValueError("Erro ao deletar questão", e)

    def getQuizPerUser(self,animalId:int,userId:int) -> None:
        self.Db.createConnection()
        
        sql = """
            SELECT 
                tbq.question_statement,
                tbq.question_possibilities,
                tbq.question_code
            FROM tb_question tbq
            WHERE tbq.animal_id = %s
            AND NOT EXISTS (
                SELECT 1
                FROM tb_user_answer tbu
                WHERE tbu.question_id = tbq.id
                AND tbu.user_id = %s
                AND tbu.was_correct_answer = TRUE
            );
        """

        try:
            self.Db.myCursor.execute(sql,(animalId,userId))
            rows = self.Db.myCursor.fetchall()
            self.Db.myDb.commit()
            self.Db.closeConnection()
            
            return rows
            
        except Exception as e:
            print(e)
            raise ValueError("Erro ao buscar questão", e)
    
    def getDefaultQuestions(self,animalId:int) -> None:
        self.Db.createConnection()
        
        sql = """
            SELECT 
                tbq.question_statement,
                tbq.question_possibilities,
                tbq.question_code
            FROM tb_question tbq
            WHERE tbq.animal_id = %s
        """

        try:
            self.Db.myCursor.execute(sql,(animalId,))
            rows = self.Db.myCursor.fetchall()
            self.Db.myDb.commit()
            self.Db.closeConnection()
            
            return rows
            
        except Exception as e:
            print(e)
            raise ValueError("Erro ao buscar questão", e)
    
    def registerUserAnswer(self,wasRight:bool,userId:int,questionId:int) -> None:
        self.Db.createConnection()
        
        sql = """
            INSERT INTO tb_user_answer (was_correct_answer,user_id,question_id)
            VALUES(%s,%s,%s);
        """

        try:
            self.Db.myCursor.execute(sql,(wasRight,userId,questionId))
            self.Db.myDb.commit()
            self.Db.closeConnection()
            
        except Exception as e:
            print(e)
            raise ValueError("Erro ao registrar resposta", e)
    
    def getQuestionDetailsByCode(self,questionCode:int) -> None:
        self.Db.createConnection()
        
        sql = """
            SELECT id,answer_id,answer_details FROM tb_question WHERE question_code = %s;
        """

        try:
            self.Db.myCursor.execute(sql,(questionCode,))
            row = self.Db.myCursor.fetchone()
            self.Db.myDb.commit()
            self.Db.closeConnection()
            
            return row
            
        except Exception as e:
            print(e)
            raise ValueError("Erro ao buscar questão", e)
        




        
        
    
        
