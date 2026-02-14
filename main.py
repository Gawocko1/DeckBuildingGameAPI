from classes.Card   import Card
from classes.Game   import Game
from classes.Player import Player
import functions
from classes.Trash import Trash

#? ========= Constants =========

players = [
    Player("Fred"),  # All player `name`s must be unique
    Player("Bob"),   #
    Player("John"),  #
    Player("Andrew") #
]
trash = Trash()
game = Game(players,
            )

#? =============================