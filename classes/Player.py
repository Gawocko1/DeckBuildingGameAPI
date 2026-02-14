from typing import List

class Player:
    def __init__(self, name):
        self.name = name
        self.actions = 1
        self.max_health = 100
        self.health = 100
        self.buys = 1
        self.money = 0
        self.hand: List = []
        self.cards: List = []
        self.drawpile: List = []
        self.discardpile: List = []