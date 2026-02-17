from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth
from .config import Settings

settings = Settings()

print(settings.database_username)

models.Base.metadata.create_all(bind=engine) # This will create the tables in the database if they do not exist already. We have to import the models file here because we have defined the tables in the models file and we need to create the tables in the database before we can use them in our application.

app = FastAPI()

# # Here the order of the the apis matter because we have 2 routes which are same.
# @app.get("/")
# async def post():
#     return {",message": "Hii Guys this is my post"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hii Guys Welcome back"}

# # Test Route
# @app.get("/sqlalchemy")
# async def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}
