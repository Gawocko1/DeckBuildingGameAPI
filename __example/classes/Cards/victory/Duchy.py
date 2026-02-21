import functions as f
from Card import Card
from CardCategory import CardCategory

class Duchy(Card):
    def __init__(self):
        super().__init__()
        self.name = "Duchy"
        self.price = 5
        self.types = {CardCategory.TREASURE}
        self.description = "Adds 3 victory points to your stock."
        self.tags = {"gain_victory",
                     "non_terminal",
                     "trashable",
                     "gainable",
                     "discardable"}
        self.bonuses = {
            "victory": 3,
        }