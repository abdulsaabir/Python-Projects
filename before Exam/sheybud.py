import random

items = ["wah", "kisi", "dhaban"]

current_player = "User 1"

while True:
    # Player selects an item
    selected_item = random.choice(items)
    print(selected_item)
    print(f"{current_player} has hidden an item. Now it's {'User 2' if current_player == 'User 1' else 'User 1'}'s turn to guess!")

    for _ in range(3):
        # Opponent guesses the item
        guess = input(f"Enter your guess as number (1-wah, 2-kisi, 3-dhaban): ")

        if guess.isdigit() and  1 <= int(guess) <= len(items) and items[int(guess) -1] == selected_item:
            player = 
            print(f"Congratulations! {'User 2' if current_player == 'User 1' else 'User 1'} guessed correctly. {'User 2' if current_player == 'User 1' else 'User 1'} wins this round!")
            exit()

        print("Incorrect guess. Try again!")

    print(f"{current_player} wins this round! The correct item was '{selected_item}'.")
    current_player = 'User 2' if current_player == 'User 1' else 'User 1'
    print()
    print('----------------------------------------')
    print()
