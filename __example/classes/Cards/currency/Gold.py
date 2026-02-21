import functions as f
from Card import Card
from CardCategory import CardCategory

class Gold(Card):
    def __init__(self):
        super().__init__()
        self.name = "Gold"
        self.price = 6
        self.types = {CardCategory.TREASURE}
        self.tags = {"gain_money",
                     "non_terminal",
                     "trashable",
                     "gainable",
                     "discardable"}
        self.description = "Adds 3 coins to your money this turn."
        self.bonuses = {
            "coins": 3,
        }