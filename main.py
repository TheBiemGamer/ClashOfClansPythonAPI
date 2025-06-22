import asyncio
from coc_api.client import ClashOfClansAPI
from coc_api.endpoints.players import PlayerEndpoints
import os

API_TOKEN = os.getenv("API_TOKEN")
PLAYER_TAG = "#L8PRCJVL2"

async def main():
    api = ClashOfClansAPI(token=API_TOKEN, proxy=True)
    player_api = PlayerEndpoints(api)

    try:
        player_data = await player_api.get_player(PLAYER_TAG)
        print(player_data)
    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        await api.close()

if __name__ == "__main__":
    asyncio.run(main())