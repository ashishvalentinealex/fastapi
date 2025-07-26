from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# Dependency for getting DB session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Pydantic schema for creating/updating a book
class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        orm_mode = True

# Pydantic schema for returning a book (with id)
class BookOut(Book):
    id: int

# GET all books
@app.get("/", response_model=List[BookOut])
def read_books(db: Session = Depends(get_db)):
    return db.query(models.Books).all()

# POST a new book
@app.post("/", response_model=BookOut)
def create_book(book: Book, db: Session = Depends(get_db)):
    book_model = models.Books(
        title=book.title,
        author=book.author,
        description=book.description,
        rating=book.rating
    )
    db.add(book_model)
    db.commit()
    db.refresh(book_model)
    return book_model

# PUT to update a book by ID
@app.put("/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if not book_model:
        raise HTTPException(status_code=404, detail="Book not found")

    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.commit()
    db.refresh(book_model)
    return book_model

# DELETE a book by ID
@app.delete("/{book_id}", response_model=BookOut)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if not book_model:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book_model)
    db.commit()
    return book_model
