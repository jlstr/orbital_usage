from fastapi import FastAPI
from src.orbital_usage_api.models import UsageResponse
from src.orbital_usage_api.usage_logic import compute_usage_report

# Main FastAPI Object used to expose endpoints
app = FastAPI()

# API's /usage endpoint
@app.get("/usage", response_model = UsageResponse)
async def calculate_usage():
  return await compute_usage_report()

@app.get("/")
def root():
  return { "message": "Welcome", "success": True }