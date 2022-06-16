from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name:str
    username:str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id:int
    name:str
    email: EmailStr
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Token_Data(BaseModel):
    id: Optional[str] = None
    username: Optional[str] = None

