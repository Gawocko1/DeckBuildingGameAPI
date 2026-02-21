from classes.placeholders.placeholders import PlayerPosition, CardLocation
from typing import Literal, Tuple
from classes.Display import Display
from game_state import set_game, game

#? UTILS ==================================

# nothing here yet

#? ========================================

#^ CLASSES ================================

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

#^ ========================================

#* QUERIERS ===============================

def current_player(game) -> PlayerPosition:
    return game.activePlayer

def next_player(game) -> PlayerPosition:
    return game.nextPlayer

def previous_player(game) -> PlayerPosition:
    return game.previousPlayer

def location(location: CardLocation = "drawpile") -> CardLocation:
    return location

#* ========================================

#& FUNCTIONS ==============================

update_game = set_game

def prompt_player(game, action, **kwargs):
    if action == "trash":
        player = kwargs["player"]
        valid_cards = kwargs["cards"]
        n_times = kwargs["n"]

        game.display.inquiry(game, valid_cards, n_times)

        cards = []
        set_game(game)
        return cards

    if action == "discard":
        player = kwargs["player"]
        valid_cards = kwargs["cards"]
        n_times = kwargs["n"]

        game.display.inquiry(game, valid_cards, n_times)

        cards = []
        set_game(game)
        return cards
    
    set_game(game)
    return []

def add_money(game, player: PlayerPosition, n=1):
    game.players[player].money += n
    set_game(game)

def is_in_range(n: float | int, low: float | int, high: float | int) -> bool:
    if low <= n <= high:
        return True
    else: return False

def wraparound_index(seq, idx):
    return (idx) % len(seq)

def add_action(game, player: PlayerPosition, n=1):
    game.players[player].actions += n
    set_game(game)

def draw_card(game, player: PlayerPosition, n=1, location: CardLocation = location("drawpile")):
    if location == "drawpile":
        game.players[player].hand.append(game.players[player].drawpile.pop())
    if location == "discardpile":
        game.players[player].hand.append(game.players[player].discardpile.pop())
    set_game(game)

def add_buy(game, player: PlayerPosition, n=1):
    game.players[player].buys += n
    set_game(game)

def discard_card(game, player: PlayerPosition, n=1, condition: CardCondition | None = None):
    valid_cards = []
    for card in game.players[player].hand:
        if condition is not None:
            if condition.is_met(card):
                valid_cards.append(card)
    cards = prompt_player(game, "discard", player=game.players[player], cards=valid_cards, n=n)
    for card in cards:
        game.players[player].discardpile.append(game.players[player].hand.pop(card))
    set_game(game)

def gain_card(game, player: PlayerPosition, n=1, condition: CardCondition | None = None):
    valid_cards = []
    for card in game.shop:
        if condition is not None:
            if condition.is_met(card):
                valid_cards.append(card)
    cards = prompt_player(game, "gain_card", player=game.players[player], cards=valid_cards, n=n)
    for card in cards:
        game.players[player].hand.append(card)
    set_game(game)

# TODO add this ==================================================================================================================================================================================================================
def look_at_card(game, player: PlayerPosition, n=1, location: CardLocation = location("drawpile")):
    raise NotImplementedError

def play_card(game, player: PlayerPosition, n=1, condition: CardCondition | None = None):
    valid_cards = []
    for card in game.players[player].hand:
        if condition is not None:
            if condition.is_met(card):
                valid_cards.append(card)
    cards = prompt_player(game, "play_card", player=game.players[player], cards=valid_cards, n=n)
    for card in cards:
        game.players[player].hand[card].play()
    set_game(game)

# TODO add this ==================================================================================================================================================================================================================
def reveal_card(n=1, location: CardLocation = location("drawpile")):
    raise NotImplementedError

def trash_card(game, player: PlayerPosition, n=1, location: CardLocation = location("drawpile")):
    valid_cards = []
    for card in game.players[player].hand:
        if card.is_met():
            valid_cards.append(card)
    cards = prompt_player(game, "trash", player=game.players[player], cards=valid_cards, n=n)
    for card in cards:
        game.trash.append(game.players[player].hand.pop(card))
    set_game(game)

# TODO add this ==================================================================================================================================================================================================================
def move_card(original_location: CardLocation = location("drawpile"), new_location: CardLocation = location("hand"), condition: CardCondition | None = None): 
    raise NotImplementedError

def return_card(game, player: PlayerPosition, condition: CardCondition | None = None, refund_pct: float = 0.00):
    valid_cards = []
    for card in game.players[player].hand:
        if condition is not None:
            if condition.is_met(card):
                valid_cards.append(card)
    set_game(game)

def win(game, player: PlayerPosition):
    game.players[player].win()
    set_game(game)

def lose(game, player: PlayerPosition):
    game.players[player].lose(game)
    set_game(game)