import Card, random

class Deck:
    """
    A class to represent a Deck of cards (Stack)
    -----------
    Attributes:
    -----------
    cards: List[Card]
        Cards in the deck
    --------
    Methods:
    --------
    deal_card(self) -> Card | None
        Returns a card from the deck stack
    """
    def __init__(self):
        """
        Initialize the deck class by adding cards of each suit and rank
        And shuffle the deck of cards
        """
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                self.cards.append(Card.Card(suit, rank))
        random.shuffle(self.cards)
    
    def __str__(self):
        """
        String representation of the deck for easier printing
        """
        return " ".join([str(card) for card in self.cards])

    def __len__(self):
        """
        Method to allow checking number of cards on the deck
        """
        return len(self.cards)

    def deal_card(self):
        """
        Method to help dealing a card whenever needed
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
