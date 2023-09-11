from art import logo
import random
import os


def game():
    print(logo)
    easy_attempt = 10
    hard_attempt = 5
    print("Welcome to Number Guessing Number!")
    print("I'm thinking of a number between 1 and 100")
    level = input(
        "Choose a difficulty. Type 'easy' or 'hard':").lower().rstrip()
    answer = random.randint(1, 100)
    flag = False
    value = easy_attempt if (level == "easy") else hard_attempt
    while (not flag and value != 0):
        print(f"You have {value} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        value = value - 1
        if (guess == answer):
            flag = True
            print(f"You got it😎😎! The answer was {answer}")
        elif (guess > answer):
            print("Too high")
        elif (guess < answer):
            print("Too low")

        if (not flag and value != 0):
            print("Guess again")
    if (value == 0 and not flag):
        print(f"You've run out of guesses, you lose😤. The answer was {answer}")
        print("Better luck next time😊")

    again = input(
        "Did you want to challange again? 'Yes' or 'No' ").lower().rstrip()
    if (again == "yes"):
        os.system('clear')
        game()


game()
