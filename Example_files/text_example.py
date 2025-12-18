# test_example.py
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Hello World"}

def test_read_books():
    response = client.get("/books/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) >= 1

def test_create_book():
    book_data = {"title": "Test Book", "author": "Test Author"}
    response = client.post("/books/", json=book_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == book_data