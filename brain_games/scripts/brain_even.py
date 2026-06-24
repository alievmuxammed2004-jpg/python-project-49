import prompt
from brain_games.even import play_game
from random import randint

RULE = "Answer 'yes' if the number is even, otherwise answer 'no'."


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_round() -> tuple[str, str]:
    number = randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer


def main():
    play_game()


if __name__ == "__main__":
    main()
