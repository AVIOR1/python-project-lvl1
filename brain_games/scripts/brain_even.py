import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!\nAnswer 'yes' if the number is even, otherwise answer 'no'.")
    random_number = randint(1, 100)
    print(f"Question: {random_number}")
    def random_number():
        return randint(1, 100)
    def condition():
        win_count = 0
        user_answer = prompt.string("Your answer: ")
        if (user_answer == 'yes' and random_number  % 2 == 0) or (user_answer == 'no' and random_number % 2 != 0):
            win_count = win_count + 1
            print('Correct!\nQuestion: ' + str(random_number())
        elif user_answer == 'yes' and random_number % 2 !=0:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {user_name}!\nQuestion: " + str(random_number)
        elif user_answer == 'no' and random_number % 2 == 0:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {user_name}!\nQuestion: " + str(random_number)
    count = 0
    while count < 3:
        print(condition())
        count = count + 1
