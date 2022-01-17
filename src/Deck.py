import Card, random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                self.cards.append(Card.Card(suit, rank))
        random.shuffle(self.cards)
    
    def __str__(self):
        return " ".join([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
