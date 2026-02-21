import functions as f
from Card import Card
from CardCategory import CardCategory

class Province(Card):
    def __init__(self):
        super().__init__()
        self.name = "Province"
        self.price = 8
        self.types = {CardCategory.VICTORY}
        self.description = "Adds 6 victory points to your stock."
        self.bonuses = {
            "victory": 6,
        }