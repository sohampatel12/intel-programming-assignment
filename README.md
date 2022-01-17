# War Card Game

A card game named 'War' based on https://en.wikipedia.org/wiki/War_(card_game)

## Usage

1. Clone the repository using 
```bash
git clone https://www.github.com/sohampatel12/war-card-game
```
2. Move to the src directory
```bash
cd war-card-game/src
```
3. Run the driver code
```bash
python driver.py
```

## Assumptions

Assumptions about the game include:
1. The player's won hands are only moved to the current cards in hand when the current cards become empty
2. If the player runs out of cards at any point in the game (even during war), the game ends immediately
3. Player2 is assumed to be a Bot in the driver code
4. To avoid cases where the game goes on indefinitely, an upper cap is added at a 1000 MAX_ROUNDS after which the game is a Tie.

## Features to be added

In the lieu of time, the game is less interactive.
Given more time I could add the following features:
1. Create an interactive terminal to collect names of players
2. Ask players to play each round instead of automatically playing
3. Add show/hide card feature in case of a 'War'
4. Add option to exit game in the middle of a game

## License
[MIT](https://choosealicense.com/licenses/mit/)
