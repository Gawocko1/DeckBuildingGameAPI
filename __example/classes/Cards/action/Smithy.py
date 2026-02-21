import functions as f
from Card import Card
from CardCategory import CardCategory

class Smithy(Card):
    def __init__(self):
        super().__init__()
        self.name = "Smithy"
        self.price = 4
        self.types = {CardCategory.ACTION}
        self.tags = {"draw",
                     "phase:action",
                     "terminal",
                     "trashable",
                     "gainable",
                     "discardable"}
        self.description = "Draws 3 cards."
        self.bonuses = {
            "cards": 3,
        }