import random

# generate a random number between 1 and 100
answer = random.randint(1, 100)

# player's initial guess
guess = None

# number of attempts
attempts = 0

while guess != answer:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < answer:
        print("Too low, try again.")
    elif guess > answer:
        print("Too high, try again.")
    else:
        print("Correct! You took", attempts, "attempts.")
