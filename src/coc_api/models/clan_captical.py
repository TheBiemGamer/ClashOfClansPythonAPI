from dataclasses import dataclass, field
from typing import List, Dict, Any
from coc_api.models import District

@dataclass
class ClanCapital:
    capital_hall_level: int
    districts: List[District] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClanCapital":
        return cls(
            capital_hall_level=data.get("capitalHallLevel"),
            districts=[District.from_dict(d) for d in data.get("districts", [])]
        )