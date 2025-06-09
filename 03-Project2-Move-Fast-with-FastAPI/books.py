from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=20)


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
    BOOKS.append(find_book_id(new_book))



def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book