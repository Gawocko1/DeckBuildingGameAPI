from classes.Card   import Card
from classes.Game   import Game
from classes.Player import Player
import functions
from classes.Trash import Trash
from classes.Display import Display
from game_state import set_game, game

#? ========= Constants =========

players = [
    Player("Fred"),  # All player `name`s must be unique
    Player("Bob"),   #
    Player("John"),  #
    Player("Andrew") #
]
trash = Trash()
display = Display()
shop = []
set_game(Game(players,
              trash,
              display,
              shop))

#? =============================