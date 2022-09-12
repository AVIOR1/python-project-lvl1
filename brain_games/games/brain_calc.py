import prompt
from random import randint
from random import choice
from python-project-lvl1.brain_games.scripts.greeting import greeting

def main():
    greeting.greeting()
    print(f'Hello, {name}!\nWhat is the result of the expression?')
    char1 = randint(1,100)
    char2 = randint(1,100)
    right_answers = 0
    operation = choise("+-*")
    while right_answers != 0:
        print(f"Question: {char_1} {operation} {char_2}")
        answer = prompt.string("Your answer: ")
        if operation == "+":
            result = char1 + char2
        if operation == "-":
            result = char1 - char2
        if operation == "*":
            result = char1 * char2
        if int(answer) == result:
            right_answer += 1
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(.Correct answer was '{result}'.\nLet's try again, {name}!")
            right_answers = 0
        print(f"Congratulations, {name}!")
