import httpx
from typing import Optional
from httpx import HTTPStatusError

BASE_URL = "https://api.clashofclans.com/v1"

class ClashOfClansAPI:
    def __init__(self, token: str, timeout: int = 10):
        self.token = token
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        self.client = httpx.AsyncClient(headers=self.headers, timeout=timeout)

    async def _get(self, endpoint: str, params: Optional[dict] = None):
        try:
            response = await self.client.get(f"{BASE_URL}{endpoint}", params=params)
            response.raise_for_status()
            return response.json()
        except HTTPStatusError as http_err:
            print(f"HTTP error: {http_err.response.status_code} - {http_err.response.text}")
            raise
        except Exception as err:
            print(f"Unexpected error: {err}")
            raise

    async def _post(self, endpoint: str, json_data: dict):
        try:
            response = await self.client.post(f"{BASE_URL}{endpoint}", json=json_data)
            response.raise_for_status()
            return response.json()
        except HTTPStatusError as http_err:
            print(f"HTTP error: {http_err.response.status_code} - {http_err.response.text}")
            raise
        except Exception as err:
            print(f"Unexpected error: {err}")
            raise

    async def close(self):
        await self.client.aclose()
