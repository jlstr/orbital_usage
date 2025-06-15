from src.orbital_usage_api.models import UsageResponse, UsageRecord
from src.orbital_usage_api.data import fetch_messages, fetch_report
from src.orbital_usage_api.calculations import calculate_credits
from typing import List

async def compute_usage_report() -> UsageResponse:
  messages = await fetch_messages()
  usage_response: List[UsageRecord] = []

  for message in messages:
    report_id, report_name = message.get("report_id"), None

    if report_id:
      report = await fetch_report(report_id)

      if report:
        credits = report["credit_cost"]
        report_name = report["name"]
      else:
        credits = calculate_credits(message["text"])
    else:
      credits = calculate_credits(message["text"])

    usage_response.append(
      UsageRecord(
        message_id = message["id"],
        timestamp = message["timestamp"],
        report_name = report_name,
        credits_used = round(credits, 2)
      )
    )

  return UsageResponse(usage = usage_response)