from fastapi import FastAPI
from models.commons.book import Book
from models.requests import bookRequest

Books = [
    Book(1, "Computer Science", "Paul Afolabi", "Introduction to computer science", 1),
    Book(2, "Philosophy Science", "Paul Cook", "Philosophy and humans", 2),
    Book(3, "Arts", "Tim Cook", "Graffiti art", 3)
]
app = FastAPI()

@app.get("/get_all_books")
async def get_all_books():
    return Books

@app.post("/inser_a_book")
async def insert_book(book_request: bookRequest.BookRequest):
    book_to_insert = Book(**book_request.model_dump())
    Books.append(book_to_insert)
    return Books