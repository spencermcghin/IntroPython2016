"""

DICE ROLLER FOR ALL YOUR GAMING NEEDS!
This program will allow a user to pick from a number of dice types
and roll them individually, in multiples of the same dice, or as an assortment
of different dice.

"""
import collections
import random
from pprint import pprint

# Define Global Variables
dice_dict = {"d2": [random.randint(1, 2)],
             "d4": [random.randint(1, 4)],
             "d6": [random.randint(1, 5)],
             "d8": [random.randint(1, 6)],
             "d10": [random.randint(1, 10)],
             "d12": [random.randint(1, 12)],
             "d20": [random.randint(1, 20)],
             "d100": [random.randint(1, 100)]}

dice_list = ["d2", "d4", "d6", "d8", "d10", "d12", "d20", "d100"]

number_of_dice = [str(x) + '.' for x in range(1, len(dice_list) + 1)]

selection_list = []


# Define program functions


def main():
    print("Hi there and welcome to the Super Dice Roller!" '\n'
          "Please choose from the menu below, and then follow any additional instructions.")
    print("Choose the type of die you'd like roll. '\n'"
          "You'll be able to choose more and/or different dice afterwards.")
    dice_options = zip(number_of_dice, dice_list)
    for number, dice in dice_options:
        print(number, dice)
    try:
        user_input = int(input("> "))
    except ValueError:
        print("Please try again.")
    else:
        selection_dict.append(user_input)
        print(selection_dict)


def roll_die(**dice):
    """ Roll dice function. Will take input as dice_dict key and append result to list for output."""
    for k, v in dice.items():
        print(k, v)


def add_die(die_variable):
    """ Append die selected from menu to selection_dict for later output."""


main()
