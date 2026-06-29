import random

from brain_games.consts import CALC_INSTRUCTION, MATH_SIGNS
from brain_games.engine import run_game


def generate_math_expression_and_result():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_sign = random.choice(MATH_SIGNS)

    # Заменяем eval(expression) на логику с if
    if math_sign == '+':
        result = num1 + num2
    elif math_sign == '-':
        result = num1 - num2
    elif math_sign == '*':
        result = num1 * num2
    else:
        # Обработка других возможных знаков (например, деление)
        result = 0

    expression = f'{num1} {math_sign} {num2}'

    return expression, str(result)


def run_calc_game():
    run_game(generate_math_expression_and_result, CALC_INSTRUCTION)
