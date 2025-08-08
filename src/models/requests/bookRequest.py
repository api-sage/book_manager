from typing import Optional
from numpy.ma.core import min_val, max_val
from pydantic import *

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Id is not required for book creation", default=None)
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=1000)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"Book title",
                "author":"Book author",
                "description":"Book description",
                "rating":1,
            }
        }
    }
