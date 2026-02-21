"""Some classes to help with Card management."""

from typing import Literal, Tuple, List
from functions import *
from classes.placeholders.placeholders import *
from classes.Game import Game

class Card:
    """Represents a card."""
    def __init__(self):
        self.type: set[CardCategory] = set()
        self.tags: set[str] = set()
        self.price = 0
        self.name = "Example"
        self.description = "Does stuff."
        self.bonuses = {
            "coins": 0,
            "actions": 0,
            "buys": 0,
            "victory": 0,
            "cards": 0,
        }
    
    def play(self, game: Game):
        """Called when you play this card.

        Args:
            game (Game): The current state of the game
        """
        pass

    def automatic(self, game: Game):
        """Called when it's your turn and this card is in your hand.

        Args:
            game (Game): The current state of the game
        """
        for key, value in self.bonuses.items():
            if key == "cards":
                draw_card(game, game.activePlayer, value)
            elif key == "actions":
                add_action(game, game.activePlayer, value)
            elif key == "buys":
                add_buy(game, game.activePlayer, value)
            elif key == "coins":
                add_money(game, game.activePlayer, value)

    def on_gain(self, game: Game):
        """Called when you gain this card to your hand.

        Args:
            game (Game): The current state of the game
        """
        pass

    def on_buy(self, game: Game):
        """Called when you buy this card.

        Args:
            game (Game): The current state of the game
        """
        pass

    def on_trash(self, game: Game):
        """Called when you trash this card.

        Args:
            game (Game): The current state of the game
        """
        pass

    def on_attacked(self, game: Game, attacker):
        """Called when you were attacked and this card is in your hand.

        Args:
            game (Game): The current state of the game
            attacker (_type_): Your attacker
        """
        pass