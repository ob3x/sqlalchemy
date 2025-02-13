from table import Books
from basemodel import CreateBook, Book
from sqlalchemy.orm import Session
from db import get_db

from fastapi import FastAPI, Depends
import uvicorn

app = FastAPI()

@app.post("/add-books/", response_model=Book)
def create_book(book : CreateBook, db : Session = Depends(get_db)):
    new_book = Books(
                title = book.title, 
                author = book.author, 
                description = book.description, 
                year = book.year)
    
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return {"Book" : new_book}

# @app.get("/books/")
# def get_books(db : Session = Depends(get_db)):
#     return db.query()

if __name__ == "__main__":
    uvicorn.run(app)