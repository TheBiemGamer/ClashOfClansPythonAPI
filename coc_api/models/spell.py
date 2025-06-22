class Spell:
    def __init__(self, data):
        self.name = data.get("name")
        self.level = data.get("level")
        self.max_level = data.get("maxLevel")
        self.village = data.get("village")

    def to_dict(self):
        return vars(self)
    
    def __str__(self):
        import json
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return str(self)