print("Welcome to Wordle! You have 6 attempts to guess the correct 5-letter word! Let's start!")

user_input = input("Your guess: ")

wordle_letters = len(wordle)

if wordle_letters == 5:
    print(user_input)

else:
    print("You need to enter 5 letters!")