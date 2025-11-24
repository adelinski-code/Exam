print("Welcome to Wordle! You have 6 attempts to guess the correct 5-letter word! Let's start!")

user_input = input("Your guess: ")

wordle = "hello"
attempts_allowed = 6
attempts_used = 0
guess = input("Try again: ")

while attempts_used > attempts_allowed:
    print(guess)

if len(guess) != 5:
    print("You need to enter 5 letters!")
    attempts_left = attempts_allowed - attempts_used
    print("You have", attempts_left, "attempts remaining.")
