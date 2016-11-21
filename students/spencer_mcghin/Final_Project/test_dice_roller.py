#!/usr/bin/env python
""" Test code for Ulimate_Dice_Roller.py """

from Ulimate_Dice_Roller import Dice


def test_init():
    d = Dice

    d = Dice("This is an object.")


def test_get_dice_value():
    d = Dice

    d.get_