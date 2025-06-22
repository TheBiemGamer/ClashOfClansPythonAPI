from dataclasses import dataclass, field
from typing import List, Dict, Optional, Iterator
from coc_api.models import Hero

@dataclass
class Heroes:
    _hero_list: List[Hero] = field(default_factory=list)
    _heroes: Dict[str, Hero] = field(init=False, default_factory=dict)

    def __post_init__(self):
        for hero in self._hero_list:
            key = self._format_attr_name(hero.name)
            self._heroes[key] = hero
            setattr(self, key, hero)

    def _format_attr_name(self, name: str) -> str:
        return name.replace(" ", "").replace("-", "").replace("_", "")

    def __getitem__(self, name: str) -> Optional[Hero]:
        return self._heroes.get(self._format_attr_name(name))

    def __iter__(self) -> Iterator[Hero]:
        return iter(self._hero_list)
