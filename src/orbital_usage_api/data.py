import httpx

MESSAGES_URL = "https://owpublic.blob.core.windows.net/tech-task/messages/current-period"

async def fetch_messages() -> list:
  async with httpx.AsyncClient() as client:
    response = await client.get(MESSAGES_URL)
    response.raise_for_status()
    return response.json()