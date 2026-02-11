## Complete FastAPI Course

# uvicorn -> This is the server that fastapi uses

# uvicorn main:app -> This command is generally used to run the server. The 'main' refers to the file name where all api's are listed (the main file), 'app' refers to name that you gave to the fastapi instance after loading the library in the main file.

# --reload is generally used to automatically load the current changes without having to rerurn the server evertime. Which genreally uses WatchFiles (WARNING:  WatchFiles detected changes in 'main.py'. Reloading...)

# By default the server runs on this port -> "http://127.0.0.1:8000"

# One thing to remember is that the order of APIs do matter if there are multiple apis of same routes and methods.