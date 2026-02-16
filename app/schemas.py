from pydantic import BaseModel, EmailStr
from datetime import datetime

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

class Post(PostBase):    # THis is the response model where we can define the fields that we want to return
    id: int
    created_at: datetime
    
    class Config:         # This is the configuration class where we can define the configuration for the pydantic model. Here we are setting orm_mode to True which means that we can use the pydantic model with the ORM models and it will automatically convert the ORM models to pydantic models.
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True