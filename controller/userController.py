from typing import Optional
from fastapi import APIRouter, Depends, Response
from uuid import UUID

from models.dependencies import getUserService
from models.user import User, UserLogin
from service.userService import UserService

userRouter = APIRouter()

@userRouter.post("/user")
async def create_user(user:User,userService: UserService = Depends(getUserService)):
    return userService.createUser(user)

@userRouter.post("/user/login")
async def login_user(user:UserLogin,response: Response,userService: UserService = Depends(getUserService)):
    token = userService.logInUser(user)['token']
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True,
        samesite="none"
    )
