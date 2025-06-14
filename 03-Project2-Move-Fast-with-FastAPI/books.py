from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=20)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra" : {
            "example" : {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description",
                "rating": 5,
                "published_date": 2029
            }
        }
    }


BOOKS = [
    Book(id=1, title="Computer Science Pro", author="codingwithroby", description="A very nice book!", rating=5, published_date=2012),
    Book(id=2, title="Be Fast with FastAPI", author="codingwithroby", description="A great book!", rating=5, published_date=2014),
    Book(id=3, title="Master Endpoints", author="codingwithroby", description="A awesome book!", rating=5, published_date=2016),
    Book(id=4, title="HP1", author="Author 1", description="Book Description", rating=2, published_date=2020),
    Book(id=5, title="HP2", author="Author 2", description="Book Description", rating=3, published_date=2020),
    Book(id=6, title="HP3", author="Author 3", description="Book Description", rating=1, published_date=2020),
]

@app.get(path="/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get(path="/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


"Fetching Book by Rating"
@app.get(path="/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

"Fetching Book by Published Date"
@app.get(path="/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.post(path="/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


@app.put(path="/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True

    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")

@app.delete(path="/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break

    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book