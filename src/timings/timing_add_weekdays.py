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
import undated.utils as udu

# -----------------------------------------------


def run_timings(number=10_000, ymd=2019_01_15, days=None):
    """ Executes the timing routine. """

    converted_ymd = ud.YMD(ymd)

    if not days:
        days = [4, 400]

    for day in days:
        print(f'\nTiming add weekdays, day: {day}')
        test_a = timeit.timeit(lambda: udu.add_weekdays(ymd, day), number=number)
        print(f'-Utils...: {test_a}')
        test_b = timeit.timeit(lambda: ud.add_weekdays(converted_ymd, day), number=number)
        print(f'-Tools...: {test_b}')


# -----------------------------------------------

if __name__ == '__main__':
    run_timings()

# -----------------------------------------------
# End.
