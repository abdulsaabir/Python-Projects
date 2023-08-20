import random

# Get the user's input and validate it
while True:
    top_of_range = input("Type a positive number: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print('Please type a number larger than 0.')
        else:
            break
    else:
        print('Please type a valid number.')

# Generate a random number within the specified range
random_number = random.randint(0, top_of_range)
guesses = 0

# Start the guessing loop
while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        
        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You guessed too high!")
        else:
            print("You guessed too low!")
    else:
        print('Please type a valid number.')

# Display the results
if guesses == 1:
    print("You got it in 1 guess.")
else:
    print("You got it in", guesses, "guesses.")
