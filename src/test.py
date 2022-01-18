import unittest
import Deck, Card, Player, War

class WarTest(unittest.TestCase):

    def test_card_greater_than(self):
        card1 = Card.Card(0, 1)
        card2 = Card.Card(0, 2)
        self.assertGreater(card2, card1, "should be unequal cards")

    def test_card_equality(self):
        card1 = Card.Card(0, 2)
        card2 = Card.Card(1, 2)
        self.assertEqual(card1, card2, "should be equal cards")

    def test_player_cards_none(self):
        player = Player.Player("Test")
        self.assertIsNone(player.play(), "player should starts with 0 cards")

    def test_deck_len(self):
        deck = Deck.Deck()
        self.assertIsNotNone(len(deck), "deck should have len function")

    def test_deck_size_start(self):
        deck = Deck.Deck()
        self.assertEqual(len(deck), 52, "deck should have 52 cards in the beginning")

    def test_war_object(self):
        deck = Deck.Deck()
        player1 = Player.Player("Test")
        player2 = Player.Player()
        war = War.War(deck, player1, player2)
        self.assertIsNotNone(war, "can create not None War object")

    def test_player_initial_cards(self):
        deck = Deck.Deck()
        player1 = Player.Player("Test")
        player2 = Player.Player()
        war = War.War(deck, player1, player2)
        self.assertEqual(player1.get_card_count(), 0, "player should start with 0 cards")

    def test_player_dealt_cards(self):
        deck = Deck.Deck()
        player1 = Player.Player("Test")
        player2 = Player.Player()
        war = War.War(deck, player1, player2)
        war.new_game()
        self.assertEqual(player1.get_card_count(), 26, "player should have 26 cards")
    
    def test_deck_size_end(self):
        deck = Deck.Deck()
        player1 = Player.Player("Test")
        player2 = Player.Player()
        war = War.War(deck, player1, player2)
        war.new_game()
        self.assertEqual(len(deck), 0, "deck should have 0 cards after dealing")

    def test_card_count(self):
        deck = Deck.Deck()
        player1 = Player.Player("Test")
        player2 = Player.Player()
        war = War.War(deck, player1, player2)
        war.new_game()
        winner = war.start_game()
        count = player1.get_card_count() + player2.get_card_count() + len(war.cards_played)
        self.assertEqual(count, 52, "total cards must be 52 in the end")


if __name__ == '__main__':
    unittest.main()