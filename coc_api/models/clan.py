from typing import Literal

class Clan:
    def __init__(self, data, icon_size: Literal["small", "medium", "large"] = "small"):
        self.tag = data.get("tag")
        self.name = data.get("name")
        self.clan_level = data.get("clanLevel")
        self.icon = data.get("badgeUrls", {}).get(icon_size)

    def to_dict(self):
        return vars(self)
    
    def __str__(self):
        import json
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return str(self)