#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Timing to check the undated module performance

    ASSUMPTIONS:
        No assumptions to note

    LIMITATIONS:
        No limitations to note
"""
# -----------------------------------------------

import timeit

import undated as ud

# -----------------------------------------------


def run_timings(number=10_000, quarters=None):
    """ Executes the timing routine """

    if not quarters:
        quarters = [2022_03, 2022_09_20]

    for quarter in quarters:
        print(f'\nTiming quarter: {quarter}')
        test_a = timeit.timeit(lambda: ud.quarter(quarter), number=number)
        print(f'-Undated...: {test_a}')


# -----------------------------------------------

if __name__ == '__main__':
    run_timings()

# -----------------------------------------------
# End.
