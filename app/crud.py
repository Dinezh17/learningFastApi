from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreate

def create_book(db: Session, book: BookCreate):
    db_book = Book(name=book.name, author=book.author, publishing_year=book.publishing_year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, book: BookCreate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db_book.name = book.name
        db_book.author = book.author
        db_book.publishing_year = book.publishing_year
        db.commit()
        db.refresh(db_book)
        return db_book
    raise HTTPException(status_code=404, detail="Book not found")

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return {"message": "Book is deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
