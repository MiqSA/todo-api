from pydantic import BaseModel
import datetime


class UserIn(BaseModel):
    username: str
    email: str
    password: str


class UserInDB(BaseModel):
    hashed_id: str
    username: str
    email: str
    hashed_password: str


class UserOut(BaseModel):
    email: str
    message: str = "Success!"


class Login(BaseModel):
    email: str
    password: str

class TokenOut(BaseModel):
    access_token: str
    refresh_token: str


class ChangePassword(BaseModel):
    email:str
    old_password:str
    new_password:str


class TokenCreate(BaseModel):
    user_id:str
    access_token:str
    refresh_token:str
    status:bool
    created_date:datetime.datetime
