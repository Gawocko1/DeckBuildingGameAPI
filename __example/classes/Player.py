from typing import List

class Player:
    def __init__(self, name):
        self.name = name
        self.actions = 1
        self.max_health = 100
        self.health = self.max_health
        self.buys = 1
        self.money = 0
        self.victory = 0
        self.hand: List = []
        self.cards: List = []
        self.drawpile: List = []
        self.discardpile: List = []
    
    def win(self, game):
        game.players = [self]

    def lose(self, game):
        game.players.remove(self)