class Heroes:
    def __init__(self, hero_list):
        self._heroes = {}
        self._hero_list = hero_list
        for hero in hero_list:
            key = self._format_attr_name(hero.name)
            self._heroes[key] = hero
            setattr(self, key, hero)

    def _format_attr_name(self, name: str) -> str:
        return name.replace(" ", "").replace("-", "").replace("_", "")

    def __getitem__(self, name: str):
        return self._heroes.get(self._format_attr_name(name))

    def __iter__(self):
        return iter(self._hero_list)

    def to_dict(self):
        return [hero.to_dict() for hero in self._hero_list]

    def __str__(self):
        import json
        return json.dumps(self.to_dict(), indent=2)

    def __repr__(self):
        return str(self)