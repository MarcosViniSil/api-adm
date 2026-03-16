from datetime import datetime, timedelta
from fastapi import HTTPException
import jwt
from dotenv import load_dotenv
load_dotenv()
import os

def createJwtToken(email:str) -> str:
    if email is None:
        raise ValueError("Email não informado, portanto não é possível gerar token")
    
    SECRET_KEY = None
    try:
        SECRET_KEY = os.environ["KEY_JWT"] 
    except Exception as e:
        raise ValueError("Não foi possível capturar chave para gerar o token")
    
    payload = createPayLoad(email)

    algorithm = 'HS256'
    try:
        token = jwt.encode(payload, SECRET_KEY, algorithm=algorithm)
        return token
    except Exception as e:
        raise ValueError(f"Ocorreu um erro ao gerar token jwt, erro: {e} [DEV]")

def validateJwtToken(token: str) -> dict:
    if token is None:
        raise ValueError("Token não foi informado")
    
    SECRET_KEY = None
    try:
        SECRET_KEY = os.environ["KEY_JWT"] 
    except Exception as e:
        raise HTTPException(status_code=401,detail="token não informado")

    algorithm = 'HS256'
    try:
        response = jwt.decode(token, SECRET_KEY, algorithms=[algorithm])
        return response
    except jwt.ExpiredSignatureError:
         raise HTTPException(status_code=401,detail="token expirado")
    except jwt.InvalidTokenError:
         raise HTTPException(status_code=401,detail="token inválido")

def createPayLoad(email:str) -> dict:
    payload = {
        'userEmail': email,
        'exp': datetime.now() + timedelta(hours=168) 
    }

    return payload    