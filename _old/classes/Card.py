"""Some classes to help with Card management."""

from typing import Literal, Tuple
from functions import *
from classes.placeholders.placeholders import *

class Card:
    """Represents a card."""
    def __init__(self):
        self.type: CardCategory | None = None
        self.tags = []