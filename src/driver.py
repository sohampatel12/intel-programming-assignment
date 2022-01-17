import Deck, Player, War

"""
Create a new deck of Cards
"""
deck = Deck.Deck()

"""
Create two players
"""
player1 = Player.Player("Soham")
player2 = Player.Player()

"""
Create a war object for new game and start the game
"""
war = War.War(deck, player1, player2)
war.new_game()
winner = war.start_game()

print(f"{winner} wins!!")
