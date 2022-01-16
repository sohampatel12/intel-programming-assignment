# Class to represent Card objects for the War game.
class Card:
    __SUITS = ['\u2663', '\u2666', '\u2665', '\u2660']
    __RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.__RANKS[self.rank]}{self.__SUITS[self.suit]}"

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank
    
    def __eq__(self, other):
        return self.rank == other.rank
