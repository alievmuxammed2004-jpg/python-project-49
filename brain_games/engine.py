import prompt

from brain_games.consts import AMOUNT_OF_ROUNDS


def run_game(generate_fn, instruction):
   name = prompt.string('Welcome to the Brain Games!\n'
                        'May i know your name? ')
   print(f'Hello, {name}!\n'
         f'{instruction}')

   for _ in range(AMOUNT_OF_ROUNDS):
       question, correct_answer = generate_fn()
       user_answer = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')

       if user_answer == correct_answer:
           print('Correct!')
       else:
           print(f"'{user_answer}' is wrong answer ;(. "
                 f"Correct answer is '{correct_answer}'.\n"
                 f"Let's try again, {name}!")
           return

   print(f'Congratulation, {name}!')