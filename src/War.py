import Card, Deck, Player

class War:
    """
    A class used to represent War game
    -----------
    Attributes:
    -----------
    player1: Player, player2: Player
        War game is played among player1 and player2
    deck: Deck
        Deck of cards to play the game
    cards_played: List[Card]
        Cards played that are currently on the table
    --------
    Methods:
    --------
    new_game(self) -> None
        Method used to create new game; deal cards and sets both players winner=False
    start_game(self) -> Player
        Method called to start playing game and return the winner
    play_cards(self) -> (Card, Card)
        Method used to play cards by each player and add the cards to cards_played
    check_game_winner(self, p1_card, p2_card) -> Player | False
        Method used to check if the game is over and return the winner if so.
    check_hand_winner(self, p1_card, p2_card) -> Player | None
        Method used to check the winner of current hand
    """
    def __init__(self, deck, player1, player2):
        """
        Parameters
        ----------
        deck: Deck
            A deck of cards
        player1: Player, player2: Player
            Players 1 & 2 to play the game
        """
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        self.cards_played = []

    def new_game(self):
        """
        Initializes player cards and sets winner = False for each player
        """
        while len(self.deck) > 1:
            self.player1.add_card(self.deck.deal_card())
            self.player2.add_card(self.deck.deal_card())
        self.player1.set_winner(False)
        self.player2.set_winner(False)

    def start_game(self):
        """
        1. Starts the game printing results of each round
        2. If there is a war, 
            each player plays 4 cards and there is battle on the 4th card
            continues till a winner of the game/round
        3. Adds the cards on the table to the winner of the round
        4. Returns the winner
        """
        war = False
        while not self.player1.is_winner() and not self.player2.is_winner():
            for _ in range(4 if war else 1):
                p1_card, p2_card = self.play_cards()
                winner = self.check_game_winner(p1_card, p2_card)
                if winner:
                    return winner
            
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
            print("----------------------------")
    
    def play_cards(self):
        """
        Each player plays a card and the played cards are added to cards_played
        """
        p1_card = self.player1.play()
        if p1_card:
            self.cards_played.append(p1_card)
        p2_card = self.player2.play()
        if p2_card:
            self.cards_played.append(p2_card)
        return p1_card, p2_card            

    def check_game_winner(self, p1_card, p2_card):
        """
        Checks if the game has a winner and returns the winner, else False
        """
        if not p1_card:
            self.player2.set_winner(True)
            return self.player2
        if not p2_card:
            self.player1.set_winner(True)
            return self.player1
        return False

    def check_hand_winner(self, p1_card, p2_card):
        """
        Compares cards and for the condition of a winner:
            1. Adds the cards on the table to the winner
            2. Return winner
        Returns None if both cards are the same which represents 'War'
        """
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
