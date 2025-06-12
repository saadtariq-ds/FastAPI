from fastapi import APIRouter, Path, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SESSION_LOCAL
from models import CreateUserRequest, Users
from passlib.context import CryptContext
from starlette import status
from typing import Annotated


router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_db():
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post(path="/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )


    db.add(create_user_model)
    db.commit()