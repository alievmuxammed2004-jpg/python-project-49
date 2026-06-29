import math
import random

from brain_games.consts import GCD_INSTRUCTION  # исправлено имя модуля
from brain_games.engine import run_game


def get_nums_pair_gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer


def run_gcd_game():
    run_game(get_nums_pair_gcd, GCD_INSTRUCTION)


if __name__ == "__main__":
    run_gcd_game()

