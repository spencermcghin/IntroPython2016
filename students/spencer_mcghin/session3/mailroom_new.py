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


""" Input args """

# Input for donation amount #

donation_amount = input("Please enter a donation amount '\n'"
                        "> ")

"""

Functions for program

"""

"""Main menu prompt"""

def user_input():
    print("From the menu, please select from the following options: '\n'"
          "1.) Generate a Thank You Letter '\n'"
          "2.) Generate a Donor Report '\n'"
          "3.) Exit '\n'"
          "You may exit the program at any time by typing 'Exit' or return to the main menu by typing 'Menu'")
    selection = input("> ")
    try:
        selection = int(selection) or "Exit" or "Menu"
    except ValueError:
        print("Please enter a selection from the list.")
    else:
        if selection == 1:
            prompt_donor()



"""Send a thank you functions"""

# Prompt for donor name #

def prompt_donor():
    print("Please enter a donor name or type 'List' for a current donor list: ")
    prompt_donor_input = input("> ")
    try:
        prompt_donor_input = str(prompt_donor_input)
    except TypeError:
        print("Your input must be a string.")
    else:


# Check if donor input is in current donor list #

def check_donor():


# Print donor list #

def print_donor_list():
    for donor, donation in sorted(donors.items()):
        print(donor)

# Add donor name to list #

def add_donor():
    donors.update()

# Add donation amount to new donor #

def add_amount():
    donors.update({# Variable) : int(donation_amount)})

# Verify donation amount is an integer #

def check_donation():
    try:
        donation_amount = int(donation_amount)
    except ValueError:
            print("Donation amount must be an integer.")
        else:
            add_amount()

# Print email to terminal #


def print_email():
        print("Hello %r, Thank you so much for your generous donation to our very charitable organization." '\n'
              "Your contribution will help us to further our reach in providing charitable services to those in need." '\n'
              "We hope that you will continue to support our organization in the future." '\n'
              "Sincerely," '\n'
              '\n'
              "Spencer McGhin")


"""

Print donor donation report functions

"""

# Generate combined dictionary objects for tabulate data input format #

def report_data():
    # establish separate dictionary objects #
    results = collections.OrderedDict()
    donor_dict = {"Donors": []}
    totals_dict = {"Total $": []}
    num_results = {"Number of Donations": []}
    avg_results = {"Average Donation": []}
    # loop through donors data set and perform aggregate functions #
    for donor, donations in sorted(donors.items()):
        donor_dict["Donors"].append(donor)
        totals_dict["Total $"].append((sum(donations)))
        num_results["Number of Donations"].append(len(donations))
        avg_results["Average Donation"].append(int(numpy.mean(donations)))
    # combine dictionary objects into one for tabulate data input format #
    results.update(donor_dict)
    results.update(totals_dict)
    results.update(num_results)
    results.update(avg_results)
    return results

print(tabulate(report_data(), headers="keys", tablefmt="fancy_grid", numalign="center"))

if __name__ == '__main__':
