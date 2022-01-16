import Card, random

class Deck:

    cards = []

    def __init__(self):
        for suit in range(4):
            for rank in range(13):
                self.cards.append(Card.Card(suit, rank))
        random.shuffle(self.cards)
    
    def __str__(self):
        return " ".join([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def deal_card(self):
        return self.cards.pop()