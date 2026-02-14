from classes.placeholders.placeholders import PlayerPosition, CardLocation
from classes.Card import CardCondition
from typing import Literal

#? UTILS ==================================

#* QUERIERS ===============================

def current_player(game) -> PlayerPosition:
    return game.activePlayer

def next_player(game) -> PlayerPosition:
    return game.nextPlayer

def previous_player(game) -> PlayerPosition:
    return game.previousPlayer

def location(location: CardLocation = "drawpile") -> CardLocation:
    return location

#& FUNCTIONS ==============================

def is_in_range(n: float | int, low: float | int, high: float | int) -> bool:
    if low <= n <= high:
        return True
    else: return False

def wraparound_index(seq, idx):
    return (idx) % len(seq)

def add_action(player: PlayerPosition, n=1):
    pass

def draw_card(player: PlayerPosition, n=1, location: CardLocation = location("drawpile")):
    pass

def add_buy(player: PlayerPosition, n=1):
    pass

def discard_card(player: PlayerPosition, n=1, condition: CardCondition | None = None):
    pass

def gain_card(player: PlayerPosition, n=1, condition: CardCondition | None = None):
    pass

def look_at_card(player: PlayerPosition, n=1, location: CardLocation = location("drawpile")):
    pass

def play_card(player: PlayerPosition, n=1, condition: CardCondition | None = None):
    pass

def reveal_card(n=1, location: CardLocation = location("drawpile")):
    pass

def trash_card(player: PlayerPosition, n=1, location: CardLocation = location("drawpile")):
    pass

def move_card(original_location: CardLocation = location("drawpile"), new_location: CardLocation = location("hand"), condition: CardCondition | None = None):
    pass

def return_card(condition: CardCondition | None = None, refund_pct: float = 0.00):
    pass

def win():
    pass

def lose():
    pass