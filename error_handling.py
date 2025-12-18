# error_handling.py
from fastapi import FastAPI, HTTPException, status
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item not found")
    return {"item_id": item_id}

@app.get("/divide/{a}/{b}")
async def divide(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return {"result": a / b}

@app.exception_handler(ZeroDivisionError)
async def zero_division_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": f"Zero division error: {exc}"},
    )