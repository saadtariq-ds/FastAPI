from sqlalchemy.orm import Session
from fastapi import APIRouter, Path, HTTPException, Depends
from starlette import status
from models import Todos, TodoRequest
from database import SESSION_LOCAL
from typing import Annotated
from .auth import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


def get_db():
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get(path="/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get("user_role") != "admin":
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return db.query(Todos).all()

@router.delete(path="/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get("user_role") != "admin":
        raise HTTPException(status_code=401, detail="Authentication Failed")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo Not Found")

    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
