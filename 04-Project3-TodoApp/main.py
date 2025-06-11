from fastapi.params import Depends
import models
from models import Todos
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import FastAPI
from database import engine, SESSION_LOCAL

app = FastAPI()

models.BASE.metadata.create_all(bind=engine)


def get_db():
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()
