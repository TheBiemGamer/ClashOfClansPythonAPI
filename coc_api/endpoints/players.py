from coc_api.client import ClashOfClansAPI
from urllib.parse import quote
from coc_api.models.player import Player

class PlayerEndpoints:
    def __init__(self, api: ClashOfClansAPI):
        self.api = api

    async def get_player(self, player_tag: str) -> Player:
        encoded_tag = quote(player_tag)
        data = await self.api._get(f"/players/{encoded_tag}")
        return Player(data)
    
    async def verify_token(self, player_tag: str, token: str):
        encoded_tag = quote(player_tag)
        data = {"token": token}
        return await self.api._post(f"/players/{encoded_tag}/verifytoken", json_data=data)