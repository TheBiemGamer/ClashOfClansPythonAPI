from clashofclans_api.client import ClashOfClansAPI

class WarLeagueEndpoints:
    def __init__(self, api: ClashOfClansAPI):
        self.api = api

    async def get_war_league(self, league_id: int):
        return await self.api._get(f"/warleagues/{league_id}")

    async def list_war_leagues(self, limit: int = 10, after: str = None, before: str = None):
        params = {"limit": limit}
        if after: params["after"] = after
        if before: params["before"] = before
        return await self.api._get("/warleagues", params=params)
