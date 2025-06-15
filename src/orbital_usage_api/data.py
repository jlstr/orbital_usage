import httpx

MESSAGES_URL = "https://owpublic.blob.core.windows.net/tech-task/messages/current-period"
REPORT_URL = "https://owpublic.blob.core.windows.net/tech-task/reports/{id}"

# Using httpx library to handle Http calls using its Async client
async def fetch_messages() -> list:
  async with httpx.AsyncClient() as client:
    response = await client.get(MESSAGES_URL)
    response.raise_for_status()
    data = response.json()
    return data["messages"]

async def fetch_report(report_id: str) -> dict | None:
  async with httpx.AsyncClient() as client:
    response = await client.get(REPORT_URL.format(id = report_id))

    if response.status_code == 404:
      return None

    response.raise_for_status()
    data = response.json()

    if "name" not in data or "credit_cost" not in data:
      print(f"Unexpected report format for Report ID: {report_id}: {data}")
      return None

    return data