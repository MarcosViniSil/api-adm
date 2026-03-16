from datetime import datetime, timedelta
import mysql.connector
from mysql.connector import errorcode
from db.connection import ConnectionDB
from models.user import User



class UserRepository:
    
    def __init__(self, db: ConnectionDB):
        self.Db = db

    def createUser(self,user:User) -> None:

        self.Db.createConnection()

        sql = """
                INSERT INTO tb_user (user_name,user_email,user_password) VALUES (%s,%s,%s);
        """
        try:
            self.Db.myCursor.execute(sql, (user.name,user.email,user.password))
            self.Db.myDb.commit()
            self.Db.closeConnection()

        except mysql.connector.IntegrityError as e:
            if e.errno == errorcode.ER_DUP_ENTRY:  
                self.Db.closeConnection()
                raise ValueError("E-mail já cadastrado.")
            else:
                self.Db.closeConnection()
                raise ValueError(f"Erro inesperado ao criar usuário: {e}")
        except Exception as e:
            self.Db.closeConnection()
            raise ValueError(f"Erro inesperado ao criar usuário: {e}")
    
    def getHashedPassword(self,email:str) -> dict:

        self.Db.createConnection()

        sql = """
                SELECT user_password FROM tb_user WHERE user_email = %s; 
        """
        try:
            self.Db.myCursor.execute(sql, (email,))
            row = self.Db.myCursor.fetchone()
            self.Db.myDb.commit()
            self.Db.closeConnection()

            return row

        except Exception as e:
            print(e)
            raise ValueError("Erro ao verificar dados para login", e)
    
    def getUserId(self, userEmail:str) -> None:
        self.Db.createConnection()

        sql = """
                SELECT id FROM tb_user WHERE user_email = %s; 
        """
        try:
            self.Db.myCursor.execute(sql, (userEmail,))
            row = self.Db.myCursor.fetchone()
            self.Db.myDb.commit()
            self.Db.closeConnection()

            return row

        except Exception as e:
            print(e)
            raise ValueError("Erro ao obter id do usuário", e)
        
