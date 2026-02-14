from classes.placeholders.placeholders import PlayerPosition, CardLocation
from classes.Card import CardCondition
from typing import Literal
from main import trash

#? UTILS ==================================

# nothing here yet

#? ========================================

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

def prompt_player(action, **kwargs):
    if action == "trash":
        player = kwargs["player"]
        valid_cards = kwargs["cards"]
        n_times = kwargs["n"]

        # TODO do something about prompting the player for cards

        cards = []
        for card in cards:
            trash.append(player.hand.pop(card))

    if action == "discard":
        player = kwargs["player"]
        valid_cards = kwargs["cards"]
        n_times = kwargs["n"]

        # TODO do something about prompting the player for cards

        cards = []
        for card in cards:
            player.discardpile.append(player.hand.pop(card))

def is_in_range(n: float | int, low: float | int, high: float | int) -> bool:
    if low <= n <= high:
        return True
    else: return False

def wraparound_index(seq, idx):
    return (idx) % len(seq)

def add_action(players, player: PlayerPosition, n=1):
    players[player].actions += n

def draw_card(players, player: PlayerPosition, n=1, location: CardLocation = location("drawpile")):
    if location == "drawpile":
        players[player].hand.append(players[player].drawpile.pop())
    if location == "discardpile":
        players[player].hand.append(players[player].discardpile.pop())

def add_buy(players, player: PlayerPosition, n=1):
    players[player].buys += n

def discard_card(players, player: PlayerPosition, n=1, condition: CardCondition | None = None):
    valid_cards = []
    for card in players[player].hand:
        if card.is_met():
            valid_cards.append(card)
    prompt_player("discard", player=players[player], cards=valid_cards, n=n)

def gain_card(players, player: PlayerPosition, n=1, condition: CardCondition | None = None):
    raise NotImplementedError

def look_at_card(players, player: PlayerPosition, n=1, location: CardLocation = location("drawpile")):
    raise NotImplementedError

def play_card(players, player: PlayerPosition, n=1, condition: CardCondition | None = None):
    raise NotImplementedError

def reveal_card(n=1, location: CardLocation = location("drawpile")):
    raise NotImplementedError

def trash_card(players, player: PlayerPosition, n=1, location: CardLocation = location("drawpile")):
    valid_cards = []
    for card in players[player].hand:
        if card.is_met():
            valid_cards.append(card)
    prompt_player("trash", player=players[player], cards=valid_cards, n=n)

def move_card(original_location: CardLocation = location("drawpile"), new_location: CardLocation = location("hand"), condition: CardCondition | None = None):
    raise NotImplementedError

def return_card(condition: CardCondition | None = None, refund_pct: float = 0.00): #! DO THIS NEXT ===============================================================================================================================================================
    raise NotImplementedError

def win():
    raise NotImplementedError

def lose():
    raise NotImplementedError