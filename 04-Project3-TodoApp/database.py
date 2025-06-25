from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# FOR SQLITE 3
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
# engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

# FOR POSTGRES
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234!@localhost/TodoApplicationDatabase"

engine = create_engine(url=SQLALCHEMY_DATABASE_URL)

SESSION_LOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)

BASE = declarative_base()