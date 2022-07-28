#!/usr/bin/python3
# -----------------------------------------------
"""
Timing to check the undated module performance

**ASSUMPTIONS**
    No assumptions to note

**LIMITATIONS**
    No limitations to note
"""
# -----------------------------------------------

import timeit

import undated as ud
import undated.utils as udu

# -----------------------------------------------


def run_timings(number=10_000, quarters=None):
    """ Executes the timing routine """

    if not quarters:
        quarters = [2022_03, 2022_09_20]

    for quarter in quarters:
        ymd = ud.YMD(quarter)
        print(f'\nTiming quarter: {quarter}')
        test_a = timeit.timeit(lambda x=ymd: ud.quarter(x), number=number)
        print(f'-Tools...: {test_a}')
        test_b = timeit.timeit(lambda x=quarter: udu.quarter(x), number=number)
        print(f'-Utils...: {test_b}')


# -----------------------------------------------

if __name__ == '__main__':
    run_timings()

# -----------------------------------------------
# End.
