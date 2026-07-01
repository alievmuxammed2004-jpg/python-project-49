import random

from brain_games.consts import PROGRESSION_INSTRUCTION
from brain_games.engine import run_game


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    return [start + i * step for i in range(length)]

def get_question_and_answer():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])

    question_parts = [
        str(num) if i != hidden_index else ".."
        for i, num in enumerate(progression)
    ]
    question = " ".join(question_parts)

    return question, correct_answer

def run_progression_game():
    run_game(get_question_and_answer,PROGRESSION_INSTRUCTION)

if __name__ == "__main__":
    run_progression_game()
