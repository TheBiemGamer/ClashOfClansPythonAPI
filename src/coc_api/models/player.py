from coc_api.models.clan import Clan
from coc_api.models.league import League
from coc_api.models.achievement import Achievement
from coc_api.models.troop import Troop
from coc_api.models.hero import Hero
from coc_api.models.heroes import Heroes
from coc_api.models.equipment import Equipment
from coc_api.models.spell import Spell
from coc_api.models.label import Label
from typing import Optional, List, Dict

class Player:
    def __init__(self, data: dict):
        self.tag: str = data.get("tag")
        self.name: str = data.get("name")
        self.town_hall_level: int = data.get("townHallLevel")
        self.town_hall_weapon_level: int = data.get("townHallWeaponLevel")
        self.exp_level: int = data.get("expLevel")
        self.trophies: int = data.get("trophies")
        self.best_trophies: int = data.get("bestTrophies")
        self.war_stars: int = data.get("warStars")
        self.attack_wins: int = data.get("attackWins")
        self.defense_wins: int = data.get("defenseWins")
        self.builder_hall_level: int = data.get("builderHallLevel")
        self.builder_trophies: int = data.get("builderBaseTrophies")
        self.builder_best_trophies: int = data.get("bestBuilderBaseTrophies")
        self.donations: int = data.get("donations")
        self.donations_received: int = data.get("donationsReceived")
        self.clan_capital_contributions: int = data.get("clanCapitalContributions")
        self.clan: Optional[Clan] = None
        clan_data: dict = data.get("clan", {})
        if clan_data:
            self.clan = Clan(clan_data)
        self.league: League = League(data.get("league", {}))
        self.builder_league: League = League(data.get("builderBaseLeague", {}))
        self.achievements: List[Achievement] = [Achievement(a) for a in data.get("achievements", [])]
        self._achievement_map: Dict[Achievement] = {a.name: a for a in self.achievements}
        self.labels: List[Label] = [Label(l) for l in data.get("labels", [])]
        self.troops: List[Troop] = [Troop(t) for t in data.get("troops", [])]
        self.heroes: Heroes[Hero] =  Heroes([Hero(h) for h in data.get("heroes", [])])
        self.hero_equipment: List[Equipment] = [Equipment(e) for e in data.get("heroEquipment", [])]
        self.spells: List[Spell] = [Spell(s) for s in data.get("spells", [])]

    def get_achievement(self, name: str):
        return self._achievement_map.get(name)

    def to_dict(self):
        def serialize(obj):
            if isinstance(obj, list):
                return [serialize(i) for i in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict()
            elif hasattr(obj, "__dict__"):
                return {k: serialize(v) for k, v in vars(obj).items()}
            else:
                return obj
        
        return {k: serialize(v) for k, v in vars(self).items() if not k.startswith("_")}
    
    def __str__(self):
        import json
        return json.dumps(self.to_dict(), indent=2)