from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: str


BOOKS = [
    Book(id=1, title="Computer Science Pro", author="codingwithroby", description="A very nice book!", rating=5),
    Book(id=2, title="Be Fast with FastAPI", author="codingwithroby", description="A great book!", rating=5),
    Book(id=3, title="Master Endpoints", author="codingwithroby", description="A awesome book!", rating=5),
    Book(id=4, title="HP1", author="Author 1", description="Book Description", rating=2),
    Book(id=5, title="HP2", author="Author 2", description="Book Description", rating=3),
    Book(id=6, title="HP3", author="Author 3", description="Book Description", rating=1),
]

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create_book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)