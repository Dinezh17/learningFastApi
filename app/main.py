from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Book
from schemas import BookCreate, BookResponse
import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.post("/addbook/", response_model=BookResponse)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)



@app.get("/listbook", response_model=list[BookResponse])
async def list_books(db: Session = Depends(get_db)):
    return crud.get_books(db=db)

@app.put("/updatebooks/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    return crud.update_book(db=db, book_id=book_id, book=book)



@app.get("/getBook/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book(db=db, book_id=book_id)




@app.delete("/deletebook/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db=db, book_id=book_id)





@app.get("/")
async def read_root():
    return {
        "hello": "welcome to my app"
    }
