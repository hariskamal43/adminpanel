from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from  .routers import user, auth
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
        password='5432', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection is successful!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return{"message": "Welcome to api!!!!!"}
