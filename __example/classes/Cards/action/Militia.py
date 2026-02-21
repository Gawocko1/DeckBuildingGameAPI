import functions as f
from Card import Card
from CardCategory import CardCategory

class Militia(Card):
    def __init__(self):
        super().__init__()
        self.name = "Militia"
        self.price = 4
        self.types = {CardCategory.ACTION, CardCategory.ATTACK}
        self.tags = {"phase:action",
                     "reaction_blockable",
                     "money_gain",
                     "terminal",
                     "trashable",
                     "gainable",
                     "discardable"}
        self.description = "You get 2 coins. Each other player discards down to 3 cards in their hand."
        self.bonuses = {
            "coins": 2
        }
    
    def play(self, game):
        super().play(game)

        for i, other in enumerate(game.players):
            if other == game.activePlayer:
                continue
            hand_size = len(other.hand)
            for _ in range(max(0, len(other.hand) - 3)):
                f.discard_card(game, i, 1, None)