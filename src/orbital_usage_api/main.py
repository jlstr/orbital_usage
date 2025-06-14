from fastapi import FastAPI
from src.orbital_usage_api.data import fetch_messages

app = FastAPI()

@app.get("/")
def root():
  return { "message": "successfully created API" }

# @app.get("/messages")
# async def messages():
#   return await fetch_messages()