import uvicorn
from fastapi import FastAPI
from routers import task, user

app = FastAPI()


@app.get('/')
async def welcom() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
