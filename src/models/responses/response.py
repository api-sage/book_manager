from typing import *
from pydantic import BaseModel

class BasicResponse(BaseModel):
    status: bool
    message: str
    data: Any

