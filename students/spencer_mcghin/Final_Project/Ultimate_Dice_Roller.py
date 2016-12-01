#! /usr/bin/env python3

"""

DICE ROLLER FOR ALL YOUR GAMING NEEDS!
This program will allow a user to pick from a number of dice types
and roll them individually, in multiples of the same dice, or as an assortment
of different dice.

"""

# Imports
import random
import tabulate


# Define Global Variables
""" Dict object that takes user input (keys) and matches it with the side (value). """

side_dict = {"1": 2,
             "2": 4,
             "3": 6,
             "4": 8,
             "5": 10,
             "6": 12,
             "7": 20,
             "8": 100}

""" List objects that are used to generate menu in dice_menu. """

dice_list = ["d2", "d4", "d6", "d8", "d10", "d12", "d20", "d100"]

number_of_dice = [str(x) + '.' for x in range(1, len(dice_list) + 1)]


# Classes
class Dice(object):

    def __init__(self, number=0, side=None):
        self.number = number
        self.side = side

    @classmethod
    def roll_dice(side, number):
        """ Generate a number of random values based on user input for die_amount in die_amount_selector. """
        rolls = []
        for _ in range(number + 1):
            rolls.append(random.randint(1, side_dict[side]))


# Functions for main program
def main():
    print("Hail Champion and welcome to the Super Dice Roller!" '\n'
          "Please choose a dice to roll from the menu below, and then follow any additional instructions." '\n'
          "You'll be able to choose more and/or different dice afterwards.")
    dice_menu()


def dice_menu():
    """ Print out menu of dice options. """
    dice_options = zip(number_of_dice, dice_list)
    for number, dice in dice_options:
        print(number, dice)
    while True:
        user_input = input("> ") + '.'
        if user_input not in number_of_dice:
            print("Please try again.")
        else:
            die_amount_selector(user_input)


def die_amount_selector(user_input):
    """ Prompt user for amount of dice to roll and then add to selection_list object. """
    d = Dice()
    try:
        die_amount = int(input("How many would you like to roll? '\n> "))
    except ValueError:
        print("Please enter an appropriate value.")
        die_amount_selector(user_input)
    else:
        d.side = user_input.strip('.')
        d.number = die_amount
        d.add_dice(side=user_input.strip('.'), number=die_amount)
        roll_more_prompt(d)


def roll_more_prompt(d):
    """ Check with user if they would like to roll more / different dice. """
    print("Would you like to roll any additional dice?")
    while True:
        confirm = input("Yes (y) or No (n)? '\n> ")
        if confirm == 'y':
            dice_menu()
        elif confirm == 'n':
            d.roll_dice()
            # ToDo - Include print die results function here


def print_die_results(d):
    """ Print contents of dice_roll_dict to a nice report. """
    print(tabulate.tabulate(d.get_dice_value(), headers="keys", tablefmt="fancy_grid", numalign="center"))

if __name__ == '__main__':
    main()
