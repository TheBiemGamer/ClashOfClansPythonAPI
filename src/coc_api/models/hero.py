from coc_api.models.equipment import Equipment

class Hero:
    def __init__(self, data):
        self.name = data.get("name")
        self.level = data.get("level")
        self.max_level = data.get("maxLevel")
        self.equipment = [Equipment(e) for e in data.get("equipment", [])]
        self.village = data.get("village")

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "max_level": self.max_level,
            "village": self.village,
            "equipment": [e.to_dict() for e in self.equipment]
        }
    
    def __str__(self):
        import json
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return str(self)