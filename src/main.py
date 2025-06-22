import asyncio
import os
from coc_api.client import ClashOfClansAPI
from coc_api.models.player import Player

API_TOKEN = os.getenv("API_TOKEN")
PLAYER_TAG = "#L8PRCJVL2"

async def main() -> None:
    """
    Example usage of the ClashOfClansAPI to fetch and print player data.
    """
    if not API_TOKEN:
        raise ValueError("API_TOKEN environment variable is not set.")

    api = ClashOfClansAPI(token=API_TOKEN, proxy=True)

    try:
        # Fetch player data
        player: Player = await api.players.get(PLAYER_TAG)
        print("Player Info:")
        print(f"Name: {player.name}")
        print(f"Town Hall Level: {player.town_hall_level}")
        print(f"Clan: {player.clan.name if player.clan else 'No clan'}")
    except Exception as e:
        print("An error occurred while fetching player data:")
        print(repr(e))
    finally:
        await api.close()

if __name__ == "__main__":
    asyncio.run(main())
