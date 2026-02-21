import functions as f
from Card import Card
from CardCategory import CardCategory

class Estate(Card):
    def __init__(self):
        super().__init__()
        self.name = "Estate"
        self.price = 2
        self.types = {CardCategory.TREASURE}
        self.description = "Adds 1 victory point to your stock."
        self.tags = {"gain_victory",
                     "non_terminal",
                     "trashable",
                     "gainable",
                     "discardable"}
        self.bonuses = {
            "victory": 1,
        }