class Player:
    
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

    def print_cards(self):
        print(" ".join(str(card) for card in self.cards))