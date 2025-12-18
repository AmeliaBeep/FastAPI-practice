# debug_example.py
from fastapi import FastAPI
import pdb

app = FastAPI()

@app.get("/debug/")
async def debug():
    pdb.set_trace()
    return {"message": "Debugging"}