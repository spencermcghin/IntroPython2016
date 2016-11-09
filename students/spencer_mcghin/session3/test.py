#!/usr/bin/env python3

import numpy
import collections

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


#
def prompt_donor():
    print("Please enter a donor name or type 'list' to see a current donor list: ")
    while True:
        prompt_donor_input = input("> ")
        if prompt_donor_input == 'list':
            print_donor_list()
            prompt_donor()
        else:
            print("blargh")


def print_donor_list():
    for donor, donation in sorted(donors.items()):
        print(donor)


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
    print(tabulate(donation_list(), headers="keys", tablefmt="fancy_grid", numalign="center"))


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
    print(tabulate(results, headers="keys", tablefmt="fancy_grid", numalign="center"))
    user_input()


user_input()