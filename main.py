from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content:str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "First post", "content": "This is the content of the first post", "published": True, "rating": 5, "id": 1},
    {"title": "Second post", "content": "This is the content of the second post", "published": False, "rating": 4, "id": 2},
    {"title": "Third post", "content": "This is the content of the third post", "published": True, "rating": 3, "id": 3}
]


# # Here the order of the the apis matter because we have 2 routes which are same.
# @app.get("/")
# async def post():
#     return {",message": "Hii Guys this is my post"}


@app.get("/")
async def root():
    return {"message": "Hii Guys Welcome back"}


@app.get("/posts")
async def get_post():
    return {"post": my_posts}   # If we ever pass an array in response of a request, then pydantic will automatically converts it in json so that it is properly structured


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    # new = data.dict()    # The data that we are getting from the body is in the form of pydantic model and we can convert it into dict using the dict() method.
    # print(new)
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"data": post_dict}


@app.get("/posts/{id}")
async def get_post(id: int, response: Response):  # Here if we do not set id to int we will get an error because we are comparing the id with the id in the list which is of type int and if we do not set it to int then it will be of type str and we will get an error because we cannot compare str with int.
    for post in my_posts:
        if post['id'] == id:
            return {"post_detail": post}
    
    # if post['id'] != id:    # Here this is a broken logic as the variable post is never defined outside the above for loop but in python the check variable exists outside the for loop with the last checked value. So this is how this works.
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"message": f"Post with id {id} not found!"}

    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {"message": f"Post with id {id} not found!"}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found!")   # This is the better way to handle the error as it is more readable and we can also pass the detail of the error in the response.


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    for i, post in enumerate(my_posts):
        if post['id'] == id:
            my_posts.pop(i)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist!")   # Here we are returning the response with the status code and the content of the response which is the error message.


@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    post_dict = post.dict()
    post_dict["id"] = id
    for i, post in enumerate(my_posts):
        if post['id'] == id:
            my_posts[i] = post_dict
            return {"message": f"Post with id {id} updated successfully!", "post": post_dict}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist!")   # Here we are returning the response with the status code and the content of the response which is the error message.
