import Card, Deck, Player

class War:
    
    def __init__(self, deck:Deck.Deck, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        self.cards_played = []

    def new_game(self):
        while len(self.deck) > 1:
            self.player1.add_card(self.deck.deal_card())
            self.player2.add_card(self.deck.deal_card())
        self.player1.set_winner(False)
        self.player2.set_winner(False)

    def start_game(self):
        war = False
        while not self.player1.is_winner() and not self.player2.is_winner():
            if war:
                for _ in range(3):
                    p1_card, p2_card = self.play_cards()
                    if self.check_game_winner(p1_card, p2_card):
                        return
            p1_card, p2_card = self.play_cards()
            if self.check_game_winner(p1_card, p2_card):
                return
            
            print(f"Your card ({self.player1.get_card_count()}):\t {p1_card}")
            print(f"Bot card ({self.player2.get_card_count()}):\t {p2_card}")
            print(f"Cards on table: {len(self.cards_played)}")

            hand_winner = self.check_hand_winner(p1_card, p2_card)

            if not hand_winner:
                print("Its a War!")
                war = True
            else:
                print("Hand winner: ", hand_winner)
                war = False
    
    def play_cards(self):
        p1_card = self.player1.play()
        if p1_card:
            self.cards_played.append(p1_card)
        p2_card = self.player2.play()
        if p2_card:
            self.cards_played.append(p2_card)
        return p1_card, p2_card            

    def check_game_winner(self, p1_card, p2_card):
        if not p1_card:
            self.player2.set_winner(True)
            return True
        if not p2_card:
            self.player2.set_winner(True)
            return True
        return False

    def check_hand_winner(self, p1_card, p2_card):
        if p1_card > p2_card:
            while len(self.cards_played) > 0:
                self.player1.add_won_card(self.cards_played.pop())
            return self.player1
        elif p1_card < p2_card:
            while len(self.cards_played) > 0:
                self.player2.add_won_card(self.cards_played.pop())
            return self.player2
        else:
            return None
