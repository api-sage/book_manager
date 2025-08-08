from fastapi import *
from models.commons.book import *
from models.requests.bookRequest import *

Books = [
    Book(1, "Computer Science", "Paul Afolabi", "Introduction to computer science", 1),
    Book(2, "Philosophy Science", "Paul Cook", "Philosophy and humans", 2),
    Book(3, "Arts", "Tim Cook", "Graffiti art", 3)
]

def get_latest_book_id(book: Book):
    book.id = 1 if len(Books) == 0 else Books[-1].id + 1
    return book

app = FastAPI()

@app.get("/get_all_books")
async def get_all_books():
    return Books

@app.post("/inser_a_book")
async def insert_book(book_request: BookRequest):
    mapped_book = Book(**book_request.model_dump())
    Books.append(get_latest_book_id(mapped_book))
    return Books