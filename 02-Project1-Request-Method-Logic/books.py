from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "category": "Science"},
    {"title": "The Lean Startup", "author": "Eric Ries", "category": "Business"},
    {"title": "1984", "author": "George Orwell", "category": "Dystopian"},
    {"title": "The Art of War", "author": "Sun Tzu", "category": "Philosophy"},
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "category": "History"}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


# Path Parameter
@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


# Query Parameter
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


# Path and Query Parameter
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get("author").casefold() == book_author.casefold() and
                book.get("category").casefold() == category.casefold()):
            books_to_return.append(book)

    return books_to_return
