import random


def check_guess(lucky_number: int, user_guess: str) -> str:
    try:
        user_guess = int(user_guess)
    except ValueError:
        raise ValueError("Invalid input: not a number")

    if user_guess < 1 or user_guess > 100:
        raise ValueError("number out of range")

    if user_guess == lucky_number:
        return "BINGO!!"
    elif user_guess < lucky_number:
        return "guess higher"
    else:
        return "guess lower"


def play_guessing_game():
    lucky_number: int = random.randint(1, 100)
    while True:
        user_guess = input("Guess a number between 1-100: ")
        try:
            feedback: str = check_guess(lucky_number, user_guess)
            print(feedback)
            if feedback == "BINGO!!":
                break
        except ValueError as ex:
            print(ex)
