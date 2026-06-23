import random

def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0

def play_even_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # Количество раундов для победы
    rounds_to_win = 5

    for _ in range(rounds_to_win):
        # Генерируем случайное число
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()

        # Определяем правильный ответ
        correct_answer = "yes" if is_even(number) else "no"

        # Проверяем ответ пользователя
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при неверном ответе

    # Если все ответы были правильными
    print(f"Congratulations, {name}!")

# Запуск игры
if __name__ == "__main__":
    play_even_game()
