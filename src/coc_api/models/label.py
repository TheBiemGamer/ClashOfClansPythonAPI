from typing import Literal

class Label:
    def __init__(self, data, icon_size: Literal["small", "medium"] = "medium"):
        self.id = data.get("id")
        self.name = data.get("name")
        self.icon = data.get("iconUrls", {}).get(icon_size)

    def to_dict(self):
        return vars(self)
    
    def __str__(self):
        import json
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return str(self)