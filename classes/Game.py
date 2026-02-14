from functions import *

class Game:
    def __init__(self, players):
        self._activePlayerIndex = 0
        self.activePlayer = players[wraparound_index(players, self._activePlayerIndex)].name
        self.nextPlayer = players[wraparound_index(players, self._activePlayerIndex+1)].name
        self.previousPlayer = players[wraparound_index(players, self._activePlayerIndex-1)].name