from fastapi import FastAPI
from data.database import init_database
from routers.profiles_ro import profile_router


import uvicorn



init_database()

app = FastAPI(title='Workshop 2')
app.include_router(profile_router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)








