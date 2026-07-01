import random

from brain_games.consts import PRIME_INSTRUCTION
from brain_games.engine import run_game


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_num_and_prime_ans():
    number = random.randint(1, 100)
    answer = "yes" if is_prime(number) else "no"
    return number, answer


def run_prime_game():
    run_game(get_num_and_prime_ans,PRIME_INSTRUCTION)

if __name__ == "__main__":
    run_prime_game()
