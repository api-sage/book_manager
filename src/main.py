from fastapi import *
from src.models.responses.book_response import BookResponse
from src.models.requests.book_request import *
from src.models.responses.response import *
from src.business_logic.book_service import *

app = FastAPI()

#####################################################
###############<<<<<<<ENDPOINTS>>>>>>>###############
#####################################################

#Gets all books
@app.get("/get_all_books", status_code=status.HTTP_200_OK)
async def get_all_books() -> BasicResponse:
    book_response = [BookResponse(**book.__dict__) for book in Books]
    return BasicResponse(status=True, message="successful", data=book_response)

#Inserts a book into the Books list
@app.post("/insert_a_book", status_code=status.HTTP_201_CREATED)
async def insert_book(book_request: BookRequest) -> BasicResponse:
    mapped_book = Book(**book_request.model_dump())
    Books.append(get_latest_book_id(mapped_book))
    return BasicResponse(status=True, message="successful", data=None)

#Get target book using the specified id
@app.get("/get_book_by_id/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)) -> BasicResponse:
    for book in Books:
        if book.id == book_id:
            return BasicResponse(status=True, message="successful", data=BookResponse(**book.__dict__))
    raise HTTPException(status_code=404, detail="Book not found")

#Gets all books with the specified rating
@app.get("/get_book_by_rating", status_code=status.HTTP_200_OK)
async def get_book_by_rating(book_rating: int = Query(gt=0, lt=6)) -> BasicResponse:
    books_to_return = []
    for book in Books:
        if book.rating == book_rating:
            books_to_return.append(book)
    if len(books_to_return) < 1:
        raise HTTPException(status_code=404, detail="No book was found")
    return BasicResponse(status=True, message="successful", data=[BookResponse(**book.__dict__) for book in books_to_return])

#Updates target book as requested
@app.put("/update_a_book/{book_id}", status_code=status.HTTP_200_OK)
async def update_a_book(book_id:int = Path(gt=0), book_request: BookRequest = Body()) -> BasicResponse:
    mapped_book = Book(**book_request.model_dump())
    target_book = find_book_by_id(book_id)
    if target_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    target_book.title = mapped_book.title
    target_book.rating = mapped_book.rating
    target_book.description = mapped_book.description
    target_book.author = mapped_book.author
    return BasicResponse(status=True, message="successful", data=BookResponse(**target_book.__dict__))

#Deletes target book
@app.delete("/delete_a_book/{book_id}", status_code=status.HTTP_200_OK)
async def delete_a_book(book_id: int = Path(gt=0)) -> BasicResponse:
    for book in Books:
        if book.id == book_id:
            Books.remove(book)
            return BasicResponse(status=True, message="successful", data=None)
    raise HTTPException(status_code = 404, detail="No book was found")
