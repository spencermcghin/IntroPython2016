import random
import tabulate

side_dict = {"1": 2,
             "2": 4,
             "3": 6,
             "4": 8,
             "5": 10,
             "6": 12,
             "7": 20,
             "8": 100}


class Dice(object):
    roll_dict = {}
    agg_dict = {}

    def __init__(self, number=0, side=None):
        self.number = number
        self.side = side

    @staticmethod
    def roll_dice(side, number):
        rolls = []
        try:
            for _ in range(number + 1):
                rolls.append(random.randint(1, side_dict[side]))
        except KeyError:
            print("Please select a value from the dice list, knave!")
        else:
            Dice.roll_dict[side] = rolls

    @staticmethod
    def agg_rolls():
        try:
            Dice.agg_dict.update({'d' + k: [sum(v)] for k, v in Dice.roll_dict.items()})
        except TypeError:
            print("Incompatible data type for function. Must be a dictionary.")


def print_die_results():
    """ Print contents of agg_dict to a nice report. """
    print(tabulate.tabulate(Dice.agg_dict, headers="keys", tablefmt="fancy_grid", numalign="center"))

#####

d = Dice()

d.roll_dice('5', 10)

d.roll_dice('3', 4)

d.agg_rolls()

print_die_results()