import prompt
from random import randint
from brain_games.scripts.greeting import greeting
from brain_games.scripts.greeting import name

def main():
    greeting()
    name()
    print(f'Hello, {name()}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    right_answers = 0
    while right_answers != 3:
        char = randint(1, 1000)
        print(f'Question: {char}')
        answer = prompt.string('Your answer: ')
        if char % 2 == 0:
            right = 'yes'
        elif char % 2 != 0:
            right = 'no'
        if answer == right:
            right_answers += 1
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{right}'. Let's try again, {name}!""")
            right_answers = 0
    print(f'Congratulations, {name}!')
