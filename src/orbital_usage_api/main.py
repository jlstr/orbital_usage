from fastapi import FastAPI
from src.orbital_usage_api.data import fetch_messages

app = FastAPI()

@app.get("/")
def root():
  return { "message": "successfully created API" }

@app.get("/messages")
async def messages():
  messages = await fetch_messages()

  return messages