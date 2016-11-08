#!/usr/bin/env python3
"""
Excercise: Write unit tests for mailroom.py
November 2, 2016
"""

from mailroom import print_report, proc_donation, get_donation

def test_print_report_1():
    assert print_report() is None

def test_proc_donation_1():
    assert proc_donation('Fred', 269) is None

def test_get_donation_1():
    get_donation()
