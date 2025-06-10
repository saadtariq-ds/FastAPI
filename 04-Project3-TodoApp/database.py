from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SESSION_LOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)

BASE = declarative_base()