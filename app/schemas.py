from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class PostCreate(BaseModel):
    text: constr(min_length=1)

class PostOut(BaseModel):
    post_id: str
    owner_email: EmailStr
    text: str
