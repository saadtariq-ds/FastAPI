from fastapi.params import Depends
import models
from models import Todos, TodoRequest
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import FastAPI, Path, Query, HTTPException
from starlette import status
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

# Fetching all the data
@app.get(path="/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()


# Fetching Data by ID
@app.get(path="/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not Found")


# Creating Data
@app.post(path="/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()