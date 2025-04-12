from fastapi import FastAPI # skzbum fastapi

import psycopg2
from psycopg2.extras import RealDictCursor

from models import Base
from database import engine

from auth import users_auth_router
from users import users_router


Base.metadata.create_all(bind=engine)

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='authdb',
    user='postgres',
    password='liana1990',
    cursor_factory=RealDictCursor
)

cursor = conn.cursor()


app = FastAPI()


@app.get("/")
def main():
    return "OK"


app.include_router(users_auth_router)
app.include_router(users_router)
