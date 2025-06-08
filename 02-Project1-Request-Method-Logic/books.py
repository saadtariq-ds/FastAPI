from fastapi import FastAPI, Body

app = FastAPI()


BOOKS = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "category": "Science"},
    {"title": "The Lean Startup", "author": "Eric Ries", "category": "Business"},
    {"title": "1984", "author": "George Orwell", "category": "Dystopian"},
    {"title": "The Art of War", "author": "Sun Tzu", "category": "Philosophy"},
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "category": "History"}
]

####################################################
#              G E T    R E Q U E S T              #
####################################################
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


####################################################
#             P O S T    R E Q U E S T             #
####################################################
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


####################################################
#              P U T    R E Q U E S T              #
####################################################
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


####################################################
#           D E L E T E    R E Q U E S T           #
####################################################
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
