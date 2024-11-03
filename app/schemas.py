from pydantic import BaseModel


class CreateUser(BaseModel):
    username = str
    firstname = str
    lastname = str
    age = int


class UpdateUser(BaseModel):
    firstname = str
    lastname = str
    age = int


class CreateTsdk(BaseModel):
    title = str
    content = str
    prioritY = int


class UpdateTsdk(BaseModel):
    title = str
    content = str
    prioritY = int
