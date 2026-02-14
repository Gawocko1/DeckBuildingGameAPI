"""Some classes to help with Card management."""

from typing import Literal, Tuple
from functions import *
from classes.placeholders.placeholders import *

class Card:
    """Represents a card."""
    def __init__(self):
        self.type: CardCategory | None = None
        self.tags = []

class CardCondition:
    """Conditions related to card placements and requirements."""
    def __init__(self, tags: list[str] | None = None, cost_range: Tuple[int, int] | None = None):
        self.tags = tags or []
        self.cost_range = cost_range

    def is_met(self, card) -> bool:
        if self.tags:
            if all(tag in card.tags for tag in self.tags):
                return True

        if self.cost_range is not None and is_in_range(card.cost,
                                                       self.cost_range[0],
                                                       self.cost_range[1]):
            return True

        return False
