from typing import List, Optional
from src.models.requests.book_request import BookRequest
from src.models.responses.book_response import BookResponse
from src.commons.book import Book

#Synthetic Books database
Books = [
    Book(1, "Computer Science", "Paul Afolabi", "Introduction to computer science", 1),
    Book(2, "Philosophy Science", "Paul Cook", "Philosophy and humans", 2),
    Book(3, "Arts", "Tim Cook", "Graffiti art", 3)
]

#Advises new book entries on id value
def get_latest_book_id(book: Book) -> Book:
    book.id = 1 if len(Books) == 0 else Books[-1].id + 1
    return book

#Finds a book with specified id
async def find_book_by_id(book_id: int) -> Optional[Book]:
    for book in Books:
        if book.id == book_id:
            return book
    return None

async def get_all_books_from_db() -> List[BookResponse]:
    return [BookResponse(**book.__dict__) for book in Books]

async def insert_book_into_db(book: BookRequest) -> None:
    mapped_book = Book(**book.model_dump())
    Books.append(get_latest_book_id(mapped_book))
    return None

async def get_books_by_rating(rating: int) -> List[Book]:
    books_to_return = []
    for book in Books:
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return

async def update_book(book_id: int, updated_book: Book) -> Optional[Book]:
    book = await find_book_by_id(book_id)
    if book is None:
        return None
    book.title = updated_book.title
    book.author = updated_book.author
    book.description = updated_book.description
    book.rating = updated_book.rating
    return book

async def delete_book(book_id: int) -> bool:
    book = await find_book_by_id(book_id)
    if book:
        Books.remove(book)
        return True
    return False