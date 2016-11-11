"""

DICE ROLLER FOR ALL YOUR GAMING NEEDS!
This program will allow a user to pick from a number of dice types
and roll them individually, in multiples of the same dice, or as an assortment
of different dice.

"""

# Imports
import random


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
    dice_menu()


def dice_menu():
    dice_options = zip(number_of_dice, dice_list)
    for number, dice in dice_options:
        print(number, dice)
    while True:
        user_input = input("> ") + '.'
        if user_input not in number_of_dice:
            print("Please try again.")
        else:
            die_amount_selector(user_input)


def roll_die(**dice):
    """ Roll dice function. Will take input as dice_dict key and append result to list for output."""
    for k, v in dice.items():
        print(k, v)


def die_amount_selector(user_input):
    """ Prompt user for amount of dice to roll"""
    while True:
        try:
            die_amount = int(input("How many would you like to roll? '\n>"))
        except TypeError:
            print("Please enter an appropriate value.")
        else:
            selection_list.append(user_input.strip('.') * die_amount)
            print(selection_list)



main()