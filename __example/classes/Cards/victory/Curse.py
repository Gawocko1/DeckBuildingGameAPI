import functions as f
from Card import Card
from CardCategory import CardCategory

class Curse(Card):
    def __init__(self):
        super().__init__()
        self.name = "Curse"
        self.price = 0
        self.types = {CardCategory.VICTORY}
        self.description = "Takes away 1 victory point from your stock."
        self.bonuses = {
            "victory": -1,
        }