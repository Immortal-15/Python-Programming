import random

target = random.randint(1, 100)
attempts_allowed = 10
attempts_made = 0

print(f"You need to guess a number between 1 and 100. \nYou have {attempts_allowed} attempts to guess the correct number.!")

while attempts_made < attempts_allowed:
    guess = int(input("Guess the number: "))
    attempts_made += 1

    if guess == target:
        print(f"You guessed the number correctly! \nYour total attempts made: {attempts_made}")
        print("Thank You for playing!")
        break
    elif guess < target:
        print("Too low")
    else:
        print("Too high")
if guess != target:
    print(f"\nYou failed to guess! The target number was {target}.")