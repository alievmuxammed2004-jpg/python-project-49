import random


def is_even(number: int) -> bool:
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_streak = 0
    target_streak = 3


    while True:
        # Генерируем случайное число (например, от 1 до 100)
        number = random.randint(1, 100)
        print(f"Question: {number}")

        user_answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if user_answer == correct_answer:
            print("Correct!")
        else:
            # В случае неверного ответа выводим сообщение и завершаем игру
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    play_game()
