# Complete FastAPI Course

uvicorn -> This is the server that fastapi uses

uvicorn main:app -> This command is generally used to run the server. The 'main' refers to the file name where all api's are listed (the main file), 'app' refers to name that you gave to the fastapi instance after loading the library in the main file.

--reload is generally used to automatically load the current changes without having to rerurn the server evertime. Which genreally uses WatchFiles (WARNING:  WatchFiles detected changes in 'main.py'. Reloading...)

By default the server runs on this port -> "http://127.0.0.1:8000"

One thing to remember is that the order of APIs do matter if there are multiple apis of same routes and methods.

Here is an example of how order of the routes matter because if we have a route which is /posts/{id} and another route which is /posts/latest then if we put the /posts/{id} route before the /posts/latest route then when we try to access the /posts/latest route it will give us an error because it will try to match the /posts/latest route with the /posts/{id} route and it will not find any match and it will give us an error. So we have to put the /posts/latest route before the /posts/{id} route so that it can match the /posts/latest route first and then it will not give us an error.

We need a way to validate whether we get correct data in request and send correct in response, this is why we use "Pydantic".
Pydantic is a python that is used to validate data (thanks to it's BaseModel).

Pydantic also automatically coverts data intp proper datatype if possible.
Like if we send "7" in a variable where only int in allowed then here pydantic will perform automatic type conversion.

The data that we get from the body in the response is in the form of pydantic model and we can convert it into dict using the dict() method.

There are 4 types of oeperations(CRUD):
1. Create (Post) --> Add new data in the database.
2. Read (Get) --> Get data from database (either get all or get by id).
3. Update (Put) --> Update data in database.
4. Delete (Delete) --> Delete data from database.

If we ever pass an array in response of a request, then pydantic will automatically converts it in json so that it is properly structured

By default FastAPI provides documentation on "/docs" and on "/redoc".

Now that we have moved out main.py file in the app directory we have to remember that the previous command to run the uvicorn server do not work. The new command would be -
uvicorn app.main:app --reload    -> Here the app.main tells FastAPI to look under a pacakge(folder in python) named app to find main file(app folder is a package because it has __init__.py file which is necessary to tell python that this folder is a package).

There are 2 major used python database library psycopg2 and sqlalchemy

There is a limitation of SQLAlchemy like if we define a table in our models then on each run it will check whether the table is present there or not. If not present it will create the table, but the limitation is that id the table already exists and then even if we change constraints/schema of the table it will not do anything.

To overcome this limitation we should normally use another software named as 'Alembic'.

We can also set the validation that we would be sending as response by setting the "response_model" in the api decorator which will validate whether the response is in correct format or not.

Whenever we want to store some sensitive information of user such as passwords we can not simply store it as a string as it can be leaked during a security attack.
Instead we save it as a hash in the database which can not be reverse engineered to get the original password.
For this we need to install 2 libraries:
1. passlib
2. Bcrypt
pip uninstall -y bcrypt passlib
pip install passlib[bcrypt]==1.7.4 bcrypt==4.1.1

If we a making a backend then we might have far too many apis that we can include all of them in the main.py, instead what we do is that we store them in different files using the APIRouter functionality of fastapi.

In the process of making api we might have multiple apis which have the same route name, so instead of writing the same route everywhere we can do this:
router = APIRouter(
    prefix="/posts"   # Here we are setting the prefix for all the routes in this router to /posts so that we do not have to write /posts in every route and it will be automatically added to the route. For example, if we have a route / then it will become /posts/ and if we have a route /{id} then it will become /posts/{id} and so on.
)

We generally use a file named as .env which stores all of our configurations so that we do not have to hardcode them in the code.

In this tutorial we have seen how much powerful a tool such as SQL Alchemy can se but still it has a major limitation like we can not update a table if it already exists in the database, and also we can not track the changes like with do with git.

For that purpose we will be using another tool name as alembic.