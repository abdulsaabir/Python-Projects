import random


def roll():
    MIN_VALUE = 1
    MAX_VALUE = 6
    roll = random.randint(MIN_VALUE, MAX_VALUE)

    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]
isPlaying = True

while True:
    isPlaying = True
    for player_idx in range(players):
        if not isPlaying:
            break
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            if player_scores[player_idx] + current_score >= max_score:
                print("You have won!")
                isPlaying = False
                break

            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score )

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])
    if not isPlaying:
        break

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)