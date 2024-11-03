# В файле main.py создайте сущность FastAPI(),
# напишите один маршрут для неё - '/', по которому функция возвращает словарь - {"message": "Welcome to Taskmanager"}.
# Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI,
# объединив все маршруты в одно приложение.
from fastapi import FastAPI
from routers import task, user


app = FastAPI()


@app.get('/')
async def welcom() -> dict:
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)
