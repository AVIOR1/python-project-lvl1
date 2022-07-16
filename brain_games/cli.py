"""Add user greeting and ask for a name."""


import prompt

name = prompt.string('May I have your name? ')
greeting = 'Hello, '
exclamation = '!'

def welcome_user():
    return greeting + name + exclamation
