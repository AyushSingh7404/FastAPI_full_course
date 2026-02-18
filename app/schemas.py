from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional

# class Post(BaseModel):
#     title: str
#     content:str
#     published: bool = True

# class CreatePost(BaseModel):
#     title: str
#     content:str
#     published: bool = True

# class UpdatePost(BaseModel):
#     title: str
#     content:str
#     published: bool

class PostBase(BaseModel):
    title: str
    content:str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

class Post(PostBase):    # This is the response model where we can define the fields that we want to return
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:         # This is the configuration class where we can define the configuration for the pydantic model. Here we are setting orm_mode to True which means that we can use the pydantic model with the ORM models and it will automatically convert the ORM models to pydantic models.
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int
    
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
