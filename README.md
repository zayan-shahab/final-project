# Dice Game

A simple dice game for one or multiple players. The game involves rolling dice, making strategic decisions on re-rolls, and competing to achieve the highest score.

## Features
- Supports multiple players.
- Automatic dice rolling and scoring.
- Special conditions:
  - **TUPLE OUT**: If all three dice show the same value, the player scores `0` for the turn.
  - **Fixed Dice**: If at least two dice have the same value, the player cannot re-roll.
- Players can strategically choose which dice to re-roll.
- **Turn Timer**: Players are given a time limit of 60 seconds per turn. If the timer runs out, their turn ends automatically, and they score `0` for that turn.
- **Game Data Tracking**: Game data, including player names, turn numbers, scores, number of re-rolls, and turn durations, is recorded and saved to a CSV file (`game_data.csv`) for analysis.

---

## How to Play

1. **Setup**: Enter the number of players when prompted.  
2. **Player Turn**:  
   - Roll three dice automatically.  
   - Decide whether to re-roll any of the dice or keep the current roll.  
   - Repeat until:  
     - The player decides not to re-roll.  
     - A "TUPLE OUT" or "Fixed Dice" condition occurs.  
     - The 60-second turn timer runs out.  
   - The turn ends, and the score is added to the player's total.  
3. **Winning**: The first player to reach or exceed the target score of 50 wins.

---

## Rules

1. **TUPLE OUT**:  
   - If all dice have the same value, the player's score for that turn is `0`.  

2. **Fixed Dice**:  
   - If at least two dice have the same value, the dice are "fixed," and the player cannot re-roll.  

3. **Turn Timer**:  
   - Each player has **60 seconds** to complete their turn. If the timer runs out, their turn ends automatically, and their score for that turn is `0`.  

4. **Scoring**:  
   - If neither the "TUPLE OUT" nor "Fixed Dice" condition occurs, the player's score is the sum of the dice values.

---

## Game Data Tracking

At the end of the game, detailed data about each turn is saved in a CSV file (`game_data.csv`) for analysis. The recorded data includes:  

- **Player Name**: Identifies the player for each turn.  
- **Turn Number**: Indicates which turn the data corresponds to.  
- **Score**: The score earned by the player in that turn.  
- **Re-rolls**: The number of dice re-rolled during the turn.  
- **Turn Duration**: The time taken by the player to complete their turn.  

### Example CSV File:
```csv
Player,Turn,Score,Re-rolls,Turn Duration
Player 1,1,11,2,8.43
Player 2,1,0,0,3.15
```
## How to Run

1. Clone the repository or download the game script.
2. Run the script using Python
