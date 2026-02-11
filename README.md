# Complete FastAPI Course

## uvicorn -> This is the server that fastapi uses

## uvicorn main:app -> This command is generally used to run the server. The 'main' refers to the file name where all api's are listed (the main file), 'app' refers to name that you gave to the fastapi instance after loading the library in the main file.

## --reload is generally used to automatically load the current changes without having to rerurn the server evertime. Which genreally uses WatchFiles (WARNING:  WatchFiles detected changes in 'main.py'. Reloading...)

## By default the server runs on this port -> "http://127.0.0.1:8000"

## One thing to remember is that the order of APIs do matter if there are multiple apis of same routes and methods.

## Here is an example of how order of the routes matter because if we have a route which is /posts/{id} and another route which is /posts/latest then if we put the /posts/{id} route before the /posts/latest route then when we try to access the /posts/latest route it will give us an error because it will try to match the /posts/latest route with the /posts/{id} route and it will not find any match and it will give us an error. So we have to put the /posts/latest route before the /posts/{id} route so that it can match the /posts/latest route first and then it will not give us an error.

## We need a way to validate whether we get correct data in request and send correct in response, this is why we use "Pydantic".
## Pydantic is a python that is used to validate data (thanks to it's BaseModel).

## Pydantic also automatically coverts data intp proper datatype if possible.
## Like if we send "7" in a variable where only int in allowed then here pydantic will perform automatic type conversion.

## The data that we get from the body in the response is in the form of pydantic model and we can convert it into dict using the dict() method.

## There are 4 types of oeperations(CRUD):
1. Create (Post) --> Add new data in the database.
2. Read (Get) --> Get data from database (either get all or get by id).
3. Update (Put) --> Update data in database.
4. Delete (Delete) --> Delete data from database.

## If we ever pass an array in response of a request, then pydantic will automatically converts it in json so that it is properly structured

## By default FastAPI provides documentation on "/docs" and on "/redoc".

## Now that we have moved out main.py file in the app directory we have to remember that the previous command to run the uvicorn server do not work. The new command would be -
## uvicorn app.main:app --reload    -> Here the app.main tells FastAPI to look under a pacakge(folder in python) named app to find main file(app folder is a package because it has __init__.py file which is necessary to tell python that this folder is a package).