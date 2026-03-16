from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from controller.userController import userRouter
from controller.animalController import animalRouter
from controller.quizController import quizRouter

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "working"}


app.include_router(userRouter)
app.include_router(animalRouter)
app.include_router(quizRouter)
#app.include_router(userRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)