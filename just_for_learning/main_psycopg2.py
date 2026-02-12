from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

class Post(BaseModel):
    title: str
    content:str
    published: bool = True
    rating: Optional[int] = None

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='your_password', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as e:
        print("Error while connecting to the database: ", e)


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
    cursor.execute("""SELECT * FROM posts""")
    post = cursor.fetchall()
    return {"post": post}   # If we ever pass an array in response of a request, then pydantic will automatically converts it in json so that it is properly structured


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
async def get_post(id: int, response: Response):  # Here if we do not set id to int we will get an error because we are comparing the id with the id in the list which is of type int and if we do not set it to int then it will be of type str and we will get an error because we cannot compare str with int.
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    get_post = cursor.fetchone()
    if not get_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found!")   # This is the better way to handle the error as it is more readable and we can also pass the detail of the error in the response.
    
    return {"post_detail": get_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist!")   # Here we are returning the response with the status code and the content of the response which is the error message.


@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist!")   # Here we are returning the response with the status code and the content of the response which is the error message.
    return {"data": updated_post}

