from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class Book(BaseModel):
    name : str
    author : str
    publishing_year : int

fake_db ={}
@app.post("/addbook/")
async def create_book(book:Book):
    book_id = len(fake_db)+1
    fake_db[book_id] = book
    return {
        "message":"Book is added", "Book id":book_id,"Book name":book.name , "Book author":book.author , "Publishing year":book.publishing_year
    }
@app.get("/listbook",response_model=list[Book])
async def list_books():
    return list(fake_db.values())


@app.put("/updatebooks/{book_id}",response_model=Book)
async def update_book(book_id:int,book:Book):
    if book_id not in fake_db:
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        fake_db[book_id]=book
    return book
@app.get("/getBook/{book_id}",response_model=Book)
async def get_book(book_id:int):
    if book_id not in fake_db:
         raise HTTPException(status_code=404, detail="Book not found")
    else:
        book = fake_db[book_id]
    return book
@app.delete("/deletebook/{book_id}")
async def del_book(book_id:int):
    if book_id not in fake_db:
         raise HTTPException(status_code=404, detail="Book not found")
    del fake_db[book_id]
    return {
        "message:" : "Books is deleted"
    }
    


@app.get("/")
async def read_root():
    return {
        "hello":"welcome to my app"
    }