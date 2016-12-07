#!/usr/bin/env python

""" Test code for Ultimate_Dice_Roller.py """

from Ultimate_Dice_Roller import Dice


def test_roll_dice():
    d = Dice()
    d.roll_dice('3', 5)
    assert len(d.roll_dice.rolls) == 5
    assert d.roll_dict.key() == 'd6'