class Card:
    """
    A class to represent a Card
    -----------
    Attributes:
    -----------
    __SUITS: List[str]
        String representation of a suit
    __RANKS: List[str]
        String represenattion of a rank
    suit: int
        Represents the suit of a Card
    rank: int
        Represents the rank of a Card
    """
    __SUITS = ['\u2663', '\u2666', '\u2665', '\u2660']
    __RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        """
        Parameters:
        -----------
        suit: int
            suit of the created card
        rank: int
            rank of the created card
        """
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        """
        String representation of the Card object for pretty prints
        """
        return f"{self.__RANKS[self.rank]}{self.__SUITS[self.suit]}"

    def __lt__(self, other):
        """
        Less than comparator implementation to compare two cards
        """
        return self.rank < other.rank

    def __le__(self, other):
        """
        Less than equal to implementation to compare two cards
        """
        return self.rank <= other.rank
    
    def __eq__(self, other):
        """
        Equal to comparator implementation to compare two cards
        """
        return self.rank == other.rank
