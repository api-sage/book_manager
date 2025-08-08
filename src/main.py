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
    all_books = await get_all_books_from_db()
    return BasicResponse(status=True, message="successful", data=all_books)

#Inserts a book into the Books list
@app.post("/insert_a_book", status_code=status.HTTP_201_CREATED)
async def insert_book(book_request: BookRequest) -> BasicResponse:
    await insert_book_into_db(book_request)
    return BasicResponse(status=True, message="successful", data=None)

#Get target book using the specified id
@app.get("/get_book_by_id/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)) -> BasicResponse:
    book = await find_book_by_id(book_id)
    if book is not None:
        return BasicResponse(status=True, message="successful", data=BookResponse(**book.__dict__))
    raise HTTPException(status_code=404, detail="Book not found")

#Gets all books with the specified rating
@app.get("/get_book_by_rating", status_code=status.HTTP_200_OK)
async def get_book_by_rating(book_rating: int = Query(gt=0, lt=6)) -> BasicResponse:
    books = await get_books_by_rating(book_rating)
    if len(books) < 1:
        raise HTTPException(status_code=404, detail="No book was found")
    return BasicResponse(status=True, message="successful", data=[BookResponse(**book.__dict__) for book in books])

#Updates target book as requested
@app.put("/update_a_book/{book_id}", status_code=status.HTTP_200_OK)
async def update_a_book(book_id:int = Path(gt=0), book_request: BookRequest = Body()) -> BasicResponse:
    mapped_book = Book(**book_request.model_dump())
    updated_book = await update_book(book_id, mapped_book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return BasicResponse(status=True, message="successful", data=BookResponse(**updated_book.__dict__))

#Deletes target book
@app.delete("/delete_a_book/{book_id}", status_code=status.HTTP_200_OK)
async def delete_a_book(book_id: int = Path(gt=0)) -> BasicResponse:
    if not await delete_book(book_id):
        raise HTTPException(status_code=404, detail="No book was found")
    return BasicResponse(status=True, message="successful", data=None)
