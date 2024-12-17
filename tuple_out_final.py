import random
import time
import pandas as pd

game_data = pd.DataFrame(columns=["Player", "Turn", "Score", "Re-rolls", "Turn Duration"])

def roll_dice():
    """Rolls three dice and returns their values."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    print(f"Dice rolled: {dice1}, {dice2}, {dice3}")
    return dice1, dice2, dice3

def is_tuple_out(dice):
    """Checks if all three dice have the same value."""
    return dice[0] == dice[1] == dice[2]

def is_fixed(dice):
    """Checks if at least two dice have the same value."""
    return len(set(dice)) < 3

def calculate_score(dice):
    """Calculates the score for a given set of dice."""
    if is_tuple_out(dice):
        return 0
    else:
        return sum(dice)

def player_turn(player_name, turn_number):
    """
    Manages a single player's turn in the dice game.

    Tracks time taken for the turn and number of re-rolls.
    Stores relevant data in the game_data DataFrame.
    """
    global game_data

    start_time = time.time()
    dice = list(roll_dice())
    score = 0
    re_rolls = 0
    time_limit = 60  

    while True:
        if is_tuple_out(dice):
            print("TUPLE OUT! You score 0 points.")
            score = 0
            break

        if is_fixed(dice):
            print("Fixed dice. You cannot re-roll.")
            score = calculate_score(dice)
            break

        # Check time limit
        if time.time() - start_time >= time_limit:
            print("Time's up! Turn ends automatically.")
            score = 0
            break

        print(f"Time remaining: {int(time_limit - (time.time() - start_time))} seconds")
        print("Do you want to re-roll any dice? (y/n)")
        choice = input().lower()

        if choice == 'n':
            score = calculate_score(dice)
            break

        re_roll_dice = []
        for i in range(3):
            if input(f"Re-roll dice {i+1}? (y/n)").lower() == 'y':
                re_roll_dice.append(i)

        for i in re_roll_dice:
            dice[i] = random.randint(1, 6)
        re_rolls += len(re_roll_dice)
        print(f"Dice after re-roll: {dice}")

    end_time = time.time()
    turn_duration = end_time - start_time

    # Add turn data to DataFrame
    game_data = pd.concat([
        game_data,
        pd.DataFrame({
            "Player": [player_name],
            "Turn": [turn_number],
            "Score": [score],
            "Re-rolls": [re_rolls],
            "Turn Duration": [turn_duration]
        })
    ], ignore_index=True)

    return score

def main():
    num_players = int(input("Enter the number of players: "))
    player_names = [f"Player {i+1}" for i in range(num_players)]
    scores = [0] * num_players
    current_player = 0
    turn_number = 1

    while True:
        player_name = player_names[current_player]
        print(f"{player_name}'s turn (Turn {turn_number}):")
        score = player_turn(player_name, turn_number)
        scores[current_player] += score
        print(f"{player_name}'s total score: {scores[current_player]}")

        # Check for game end condition
        if any(score >= 50 for score in scores):
            break

        # Next player's turn
        current_player = (current_player + 1) % num_players
        if current_player == 0:
            turn_number += 1

    winner = scores.index(max(scores))
    print(f"{player_names[winner]} wins!")

    # Display and save game data
    print("\nGame Summary:")
    print(game_data)
    game_data.to_csv("game_data.csv", index=False)
    print("Game data saved to 'game_data.csv'.")

if __name__ == "__main__":
    main()
