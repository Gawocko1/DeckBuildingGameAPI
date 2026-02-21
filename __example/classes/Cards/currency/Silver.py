import functions as f
from Card import Card
from CardCategory import CardCategory

class Silver(Card):
    def __init__(self):
        super().__init__()
        self.name = "Silver"
        self.price = 3
        self.types = {CardCategory.TREASURE}
        self.description = "Adds 2 coins to your money this turn."
        self.bonuses = {
            "coins": 2,
        }