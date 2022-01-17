import Deck, Player, War

deck = Deck.Deck()
player1 = Player.Player("Soham")
player2 = Player.Player()
war = War.War(deck, player1, player2)
war.new_game()
war.start_game()


