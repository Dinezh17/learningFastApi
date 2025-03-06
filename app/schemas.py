from pydantic import BaseModel



class BookCreate(BaseModel):
    name: str
    author: str
    publishing_year: int





class BookResponse(BookCreate):
    id: int

    class Config:
        orm_mode = True
