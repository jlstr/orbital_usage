import httpx

MESSAGES_URL = "https://owpublic.blob.core.windows.net/tech-task/messages/current-period"
REPORT_URL = "https://owpublic.blob.core.windows.net/tech-task/reports/{id}"

async def fetch_messages() -> list:
  async with httpx.AsyncClient() as client:
    response = await client.get(MESSAGES_URL)
    response.raise_for_status()
    return response.json()

async def fetch_report(report_id: str) -> dict | None:
  async with httpx.AsyncClient() as client:
    response = await client.get(REPORT_URL.format(id = report_id))

    if response.status_code == 404:
      return None

    response.raise_for_status()
    return response.json()