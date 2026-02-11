from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content:str
    published: bool = True
    rating: Optional[int] = None


# # Here the order of the the apis matter because we have 2 routes which are same.
# @app.get("/")
# async def post():
#     return {",message": "Hii Guys this is my post"}


@app.get("/")
async def root():
    return {"message": "Hii Guys Welcome back"}


@app.get("/post")
async def get_post():
    return {"post": "My post"}


@app.post("/create_posts")
async def create_posts(data: Post):
    # new = data.dict()    # The data that we are getting from the body is in the form of pydantic model and we can convert it into dict using the dict() method.
    # print(new)
    return f"Created post with title: {data.title}, and content: {data.content}, and published: {data.published}, and rating: {data.rating}"    

