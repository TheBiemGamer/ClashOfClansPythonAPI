import asyncio
import os
from coc_api import ClashOfClansAPI
from coc_api.models import Player
from dotenv import load_dotenv

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
        clan = await api.clans.get(player.clan.tag)
        print(clan.member_list)
    except Exception as e:
        print("An error occurred while fetching player data:")
        print(repr(e))
    finally:
        await api.close()

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
