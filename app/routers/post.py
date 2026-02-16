from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas    # here .. means that we are going back to the parent directory and then importing the models, schemas and utils files from there.
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[schemas.Post])   # Here we are setting the response model to a list of Post because we are returning a list of posts in the response and we want to validate the response using the pydantic model. So we have to set the response model to a list of Post.
async def get_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    
    return posts   # If we ever pass an array in response of a request, then pydantic will automatically converts it in json so that it is properly structured


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
async def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # new = data.dict()    # The data that we are getting from the body is in the form of pydantic model and we can convert it into dict using the dict() method.
    # print(new)
    # post_dict = post.dict()
    # post_dict["id"] = randrange(0, 1000000)
    # my_posts.append(post_dict)
    # print(my_posts)
    post.dict()
    new_post = models.Post(**post.dict())
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post


@router.get("/{id}")
async def get_post(id: int, response: Response, db: Session = Depends(get_db), response_model=schemas.Post):  # Here if we do not set id to int we will get an error because we are comparing the id with the id in the list which is of type int and if we do not set it to int then it will be of type str and we will get an error because we cannot compare str with int.
    # for post in my_posts:
    #     if post['id'] == id:
    #         return {"post_detail": post}
    
    # # if post['id'] != id:    # Here this is a broken logic as the variable post is never defined outside the above for loop but in python the check variable exists outside the for loop with the last checked value. So this is how this works.
    # #     response.status_code = status.HTTP_404_NOT_FOUND
    # #     return {"message": f"Post with id {id} not found!"}

    # # response.status_code = status.HTTP_404_NOT_FOUND
    # # return {"message": f"Post with id {id} not found!"}
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found!")   # This is the better way to handle the error as it is more readable and we can also pass the detail of the error in the response.
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    # for i, post in enumerate(my_posts):
    #     if post['id'] == id:
    #         my_posts.pop(i)
    #         return Response(status_code=status.HTTP_204_NO_CONTENT)
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist!")   # Here we are returning the response with the status code and the content of the response which is the error message.
    
    deleted_post.delete(synchronize_session=False) 
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
async def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), response_model=schemas.Post):
    # post_dict = post.dict()
    # post_dict["id"] = id
    # for i, post in enumerate(my_posts):
    #     if post['id'] == id:
    #         my_posts[i] = post_dict
    #         return {"message": f"Post with id {id} updated successfully!", "post": post_dict}
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist!")   # Here we are returning the response with the status code and the content of the response which is the error message.
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    
    return post_query.first()
