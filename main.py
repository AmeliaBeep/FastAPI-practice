# main.py
from fastapi import FastAPI, HTTPException, status
from models import Book
from typing import List, Optional

app = FastAPI()

books = [
    Book(id=1, title="Book 1", author="Author 1"),
    Book(id=2, title="Book 2", author="Author 2"),
]

@app.get("/books/", response_model=List[Book])
async def read_books():
    return books

@app.post("/books/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    books.append(book)
    return book

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    for i, existing_book in enumerate(books):
        if existing_book.id == book_id:
            books[i] = book
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")