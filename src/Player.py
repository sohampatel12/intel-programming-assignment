class Player:
    """
    A class to represent a Player
    -----------
    Attributes:
    -----------
    winner: bool
        Represents if a player has won
    name: str
        Name of the player; Default: Bot
    cards: List[Card]
        Cards that the player currently holds
    hands_won: List[Card]
        Cards that the player has won
    --------
    Methods:
    --------
    play(self) -> Card | None
        Player plays a card from cards
        - If cards is empty, hands_won is moved to cards
        - If both cards and hands_won is empty, returns None
    add_card(self) -> None
        Adds a card to Player's cards
    add_won_card(self) -> None
        Adds a won card to Player's hands_won
    set_winner(self, value) -> None, is_winner(self) -> bool
        Getter and setter for winner attribute of Player
    get_card_count(self) -> int
        Returns the total cards a Player has (cards + hands_won)
    """
    def __init__(self, name="Bot"):
        self.winner = False
        self.name = name
        self.cards = []
        self.hands_won = []

    def __str__(self):
        return self.name
    
    def play(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        elif len(self.hands_won) > 0:
            while len(self.hands_won) > 0:
                self.cards.append(self.hands_won.pop())
            return self.cards.pop()
        return None

    def add_card(self, card):
        self.cards.append(card)

    def add_won_card(self, card):
        self.hands_won.append(card)

    def set_winner(self, value):
        self.winner = value
    
    def is_winner(self):
        return self.winner

    def get_card_count(self):
        return len(self.cards) + len(self.hands_won)
