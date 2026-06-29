import random

wins = 0  # New feature: count wins

def show_instructions():
    print()
    print('Guess a number between 1 and 50.')
    print('Try to win in as few attempts as possible.')
    print()

def play_game():
    global wins  # Use the win counter

    secret_number = random.randint(1, 50)

    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input('Guess a number between 1 and 50: '))
            attempts += 1
        except ValueError:
            print('Please enter a number')
            continue

        if guess < secret_number:
            print('Guess higher')
        elif guess > secret_number:
            print('Guess lower')

    wins += 1  # Add a win
    print(f"You win, it took you {attempts} attempts")

def menu():
    while True:
        choice = input('''
Press 1 to play
Press 2 to show instructions
Press 3 to exit

Your choice: ''')

        if choice.isdigit():
            choice = int(choice)
            if choice in (1, 2, 3):
                return choice
            else:
                print("Please enter 1, 2 or 3")
        else:
            print("Please enter a number")


print('Welcome to the number guessing game')

while True:
    choice = menu()

    if choice == 1:
        play_game()

    elif choice == 2:
        show_instructions()

    elif choice == 3:
        print(f"You won {wins} game(s). Thanks for playing!")
        break