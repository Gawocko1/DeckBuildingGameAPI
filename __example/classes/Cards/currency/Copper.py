import functions as f
from Card import Card
from CardCategory import CardCategory

class Copper(Card):
    def __init__(self):
        super().__init__()
        self.name = "Copper"
        self.price = 0
        self.types = {CardCategory.TREASURE}
        self.tags = {"gain_money",
                     "non_terminal",
                     "trashable",
                     "gainable",
                     "discardable"}
        self.description = "Adds 1 coin to your money this turn."
        self.bonuses = {
            "coins": 1,
        }