# Short Blackjack Game

A simplified, console-based version of the Blackjack card game implemented in Python.<br>
This game pits the player against a dealer, adhering to basic Blackjack rules such as hitting,<br>
standing, busting, and score comparisons.

## Project Structure

```
short_blackjack/
│
├── blackjack.py      # Main game logic
├── art.py            # External file containing ASCII logo and outcome messages
```

---

## Features

- Simulates a simplified Blackjack game.
- Dealer draws until at least 17.
- Ace automatically adjusts value from 11 to 1 to avoid busting.
- Scoreboard tracks the number of wins per session.
- Includes user-friendly prompts and console output.

---

## How to Run

Make sure you have Python 3 installed. Place `blackjack.py` and `art.py` in the same directory.

```bash
python blackjack.py
```

---

## Game Flow

1. Game starts with two cards dealt to both player and dealer.
2. The player chooses to **Hit** (`'h'`) or **Stand** (`'s'`).
3. If the player **Hits**:
   - A new card is added to their hand.
   - If their score exceeds 21, they **bust**.
4. If the player **Stands**:
   - Dealer draws cards until reaching at least 17.
5. The game evaluates hands and announces the winner.
6. Scores are updated and the player is prompted to play again.

---

## Example Game Output

```text
Do you want to play a game of Blackjack? Type 'y' or 'n': y

Scoreboard:
Dealer Wins: 0
Player Wins: 0

Dealer's Hand:
_, 10

Your Hand:
8, 7

Type 'h' to hit, type 's' to stand: s

Dealer's Hand:
6, 10, 5

Your Hand:
8, 7

You win!
```
