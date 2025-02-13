#################################################
# This program runs a game of "higher or lower" #
# Author: Sandra K.J            Python 3.12     #
#################################################

import random

def high_low():
    """
    print welcome message
    """
    print("Welcome to the game :)")
    print("this is a guessing game!")
    print("It works like this: You give me a number, and I'll pick a random number between one and your number!")
    print("Then, you guess, and I tell you wether it's higher or lower!")
    understand = input("got it? ")
    if understand in ("y", "yes", "Y", "Yes", "yep", "Yep"):
        print("Perfect!")
        get_number()
    elif understand in ("n", "no", "N", "No", "nope", "Nope", "naur"):
        print("Okay, i'll repeat!")
        high_low()
    else:
        print("Maybe you didn't quite get it... I'll repeat.")
        high_low()

def get_number():
    """
    get a numerical input from the user
    """
    print("I need a number from you, so we can play :)")
    try:
        number = int(input("What's my max number? "))
    except ValueError:
        print("whoops. Thats not a number, lets try again.")
        get_number()
    else:
        random_number(number)

def random_number(number):
    """
    choose a random number
    between 1 and n (number)
    """
    answer = random.randint(1, number)
    the_game(answer)

def the_game(answer):
    """
    play the game;
    Takes an input, evaluates wether low, high, or right.
    Tells the user the result of the guess.
    Calls itself.
    """
    guess = int(input("Okay! Take your guess: \n"))
    if guess < answer:
        print("higher!")
        the_game(answer)
    elif guess > answer:
        print("lower...")
        the_game(answer)
    elif guess == answer:
        print(f"heck yea buddy! {answer} is the answer!")
        end_dialogue()

def end_dialogue():
    """
    talk the user through the end of the game
    and the possible new beginning
    """
    choice = input("that was a fun game, do you wanna play again? ")
    if choice in ("y", "yes", "Y", "Yes", "Yes!", "yes!", "YES!", "YES"):
        print("wonderful!")
        get_number()
    elif choice in ("n", "no", "N", "No", "No!", "no!", "NO!", "NO"):
        print("Oh! okay. Thank you for the game.")
        print("goodbye...")
        print(" :( ")
        quit()
    else:
        print("sorry, I din't quite catch that. I'll try again")
        end_dialogue()

"""
time to call the game
"""
high_low()