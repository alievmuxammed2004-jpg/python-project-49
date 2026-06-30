import random

from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine import run_game


def is_play():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer


def run_even_game():
    run_game(is_play,EVEN_INSTRUCTION)

