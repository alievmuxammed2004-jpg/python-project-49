import random
import operator

def generate_question():
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op_symbol = random.choice(list(ops.keys()))
    op_func = ops[op_symbol]
    correct_answer = op_func(a, b)
    question = f"{a} {op_symbol} {b}"
    return question, correct_answer

def play():
    print("Brain Calc: посчитай выражение и введи ответ.")
    while True:
        question, correct_answer = generate_question()
        user_input = input(f"Вопрос: {question} = ")
        try:
            user_answer = int(user_input)
        except ValueError:
            print("Это не число. Попробуй ещё раз.")
            continue

        if user_answer == correct_answer:
            print("Верно!")
        else:
            print(f"Неверно. Правильный ответ: {correct_answer}")

        again = input("Ещё один вопрос? (y/n): ").strip().lower()
        if again != 'y':
            print("Пока!")
            break

if __name__ == "__main__":
    play()
