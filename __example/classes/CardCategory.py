from enum import Enum, auto

class CardCategory(Enum):
    ACTION = auto()
    TREASURE = auto()
    VICTORY = auto()
    ATTACK = auto()
    REACTION = auto()
    DURATION = auto()
    CURSE = auto()