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
def find_book_by_id(book_id: int) -> Book | None:
    for book in Books:
        if book.id == book_id:
            return book
    return None


