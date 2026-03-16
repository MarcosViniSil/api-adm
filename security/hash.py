import bcrypt
import logging
def createHashForPassword(password:str) -> str:
    print("password ",password)
    if password is None:
        raise ValueError(f"A senha não foi informada")
    logging.info("password ",password)
    passwordBytes = password.encode("utf-8")
    logging.info("passwordBytes ",passwordBytes)
    try:
        passwordHash = bcrypt.hashpw(password, bcrypt.gensalt())
        return passwordHash
    except Exception as e:
        raise ValueError(f"Não foi possível gerar o hash da senha informada, tente novamente {e} [DEV]")

def isPasswordEqualDB(hashDataBase:bytes, password:str) -> bool:
    if hashDataBase is None or password is None:
        raise ValueError(f"Senha ou hashing não informado")
    
    passwordBytes = password.encode("utf-8")
    
    try:
        if bcrypt.checkpw(passwordBytes, hashDataBase):
            return True
        else:
            return False
    except Exception as e:
        raise ValueError(f"Ocorreu um erro ao verificar senha, erro: {e} [DEV]")