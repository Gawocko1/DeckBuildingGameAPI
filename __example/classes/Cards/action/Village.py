import functions as f
from Card import Card
from CardCategory import CardCategory

class Village(Card):
    def __init__(self):
        super().__init__()
        self.name = "Village"
        self.price = 3
        self.types = {CardCategory.ACTION}
        self.tags = {"draw",
                     "phase:action",
                     "action_gain",
                     "non_terminal",
                     "trashable",
                     "gainable",
                     "discardable"}
        self.description = "Draws another card and gives you 2 actions."
        self.bonuses = {
            "cards": 1,
            "actions": 2
        }