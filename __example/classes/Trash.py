from typing import List

class Trash:
    def __init__(self):
        self.contents: List = []

    def append(self, thing):
        self.contents.append(thing)