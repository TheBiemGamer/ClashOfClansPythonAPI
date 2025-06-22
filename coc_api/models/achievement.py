class Achievement:
    def __init__(self, data):
        self.name = data.get("name")
        self.stars = data.get("stars")
        self.value = data.get("value")
        self.target = data.get("target")
        self.info = data.get("info")
        self.completion_info = data.get("completionInfo")
        self.village = data.get("village")

    def to_dict(self):
        return vars(self)
    
    def __str__(self):
        import json
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return str(self)