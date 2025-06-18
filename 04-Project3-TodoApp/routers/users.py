from sqlalchemy.orm import Session
from fastapi import APIRouter, Path, HTTPException, Depends
from starlette import status
from models import Todos, TodoRequest, Users, UserVerification
from database import SESSION_LOCAL
from typing import Annotated
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


def get_db():
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# Getting User Information
@router.get(path="/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return db.query(Users).filter(Users.id == user.get("id")).first()


# Changing User Password
@router.put(path="/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, user_verfication: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    user_model = db.query(Users).filter(Users.id == user.get("id")).first()

    if not bcrypt_context.verify(user_verfication.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail="Authentication Failed")

    user_model.hashed_password = bcrypt_context.hash(user_verfication.new_password)
    db.add(user_model)
    db.commit()
