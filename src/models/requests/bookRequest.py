from pydantic import BaseModel

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

