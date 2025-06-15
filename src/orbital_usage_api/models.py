from typing import Optional, List
from pydantic import BaseModel

class UsageRecord(BaseModel):
  message_id: int
  timestamp: str
  report_name: Optional[str] = None
  credits_used: float

class UsageResponse(BaseModel):
  usage: List[UsageRecord]