#!/usr/bin/env python3

import numpy, collections

from tabulate import tabulate

"""Dictionary of Donors and Amounts Donated"""

donors = {"nick padgett": [12312, 34230, 38593],
          "julia allen": [49203, 5023, 9052],
          "pete tamisin": [9503, 2093, 10932, 40923],
          "charles elliott": [209, 50912, 9026],
          "andy rocha": [20968, 2091, 8934],
          "beth desousa": [29092, 5906, 8734]}

"""

Functions for program

"""

# Main menu prompt #

def user_input():
    print("From the menu, please select from the following options: '\n'"
          "1.) Generate a Thank You Letter '\n'"
          "2.) Generate a Donor Report '\n'"
          "3.) Exit '\n'"
          "You may exit the program at any time by typing 'exit' or return to the main menu by typing 'menu'")
    while True:
        choices = ['1', '2', '3', 'exit', 'menu']
        selection = input("> ")
        if selection in choices:
            route_selection(selection)
        else:
            print("Please choose an option from the menu.")


# Route selection from user_input to proper function #

def route_selection(selection):
    if selection == '1':
        prompt_donor()
    elif selection == '2':
        report_data()
    elif selection == '3' or 'exit':
        quit()
    elif selection == 'menu':
        user_input()
    else:
        raise ValueError("Input does not correspond to a menu value")



"""

Send a thank you functions

"""



# Prompt for donor name #

def prompt_donor():
    print("Please enter a donor name or type 'list' to see a current donor list: ")
    while True:
        prompt_donor_input = input("> ")
        if prompt_donor_input == 'list':
            print_donor_list()
        else:
            check_donor(prompt_donor_input)



# Check if donor input is in current donor list #

def check_donor(prompt_donor_input):
    if prompt_donor_input in donors.keys():
        print_email(prompt_donor_input)

# Print donor list #

def print_donor_list():
    for donor, donation in sorted(donors.items()):
        print(donor)

# Print donor list with donation amount #

def donation_list():
    # establish separate dictionary objects #
    results = collections.OrderedDict()
    donor_dict = {"Donors": []}
    totals_dict = {"Total $": []}
    # loop through donors data set and perform aggregate functions #
    for donor, donations in sorted(donors.items()):
        donor_dict["Donors"].append(donor)
        totals_dict["Total $"].append((sum(donations)))
    # combine dictionary objects into one for tabulate data input format #
    results.update(donor_dict)
    results.update(totals_dict)
    print(tabulate(results, headers="keys", tablefmt="fancy_grid", numalign="center"))

# Add donor name to list #

def add_donor():
    donors.update()

# Print email to terminal #


def print_email(prompt_donor_input):
        print("Hello {}, Thank you so much for your generous donation to our very charitable organization." '\n'
              "Your contribution will help us to further our reach in providing charitable services to those in need." '\n'
              "We hope that you will continue to support our organization in the future." '\n'
              "Sincerely," '\n'
              '\n'
              "Spencer McGhin".format(prompt_donor_input))


user_input()
