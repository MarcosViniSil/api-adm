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
async def login_user(
    user: UserLogin,
    userService: UserService = Depends(getUserService)
):

    result = userService.logInUser(user)

    token = result["token"]

    return {
        "access_token": token,
        "token_type": "bearer"
    }
