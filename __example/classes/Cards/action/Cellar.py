import functions as f
from Card import Card
from CardCategory import CardCategory

class Cellar(Card):
    def __init__(self):
        super().__init__()
        self.name = "Cellar"
        self.price = 2
        self.types = {CardCategory.ACTION}
        self.tags = {"phase:action",
                     "action_gain",
                     "card_gain",
                     "discard_cards",
                     "non_terminal",
                     "trashable",
                     "gainable",
                     "discardable"}
        self.description = "You get 1 action. Discard 1 card. Draw 1 card" #Discard any number of cards, then draw that many.
        self.bonuses = {
            "cards": 1
        }
    
    def play(self, game):
        f.discard_card(game, game.activePlayer, n=1, condition=None)

        super().play(game)