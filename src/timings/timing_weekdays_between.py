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


def run_timings(number=10_000, iymd=2019_01_15, days=None):
    """ Executes the timing routine. """

    converted_ymd = ud.YMD(iymd)

    if not days:
        days = [2022_01_14, 2023_07_25]

    for day in days:
        print(f'\nTiming weekdays between, day: {day}')
        test_a = timeit.timeit(lambda d=day: udu.weekdays_between(iymd, d), number=number)
        print(f'-Utils...: {test_a}')
        converted_day = ud.YMD(day)
        test_b = timeit.timeit(
            lambda cd=converted_day: ud.weekdays_between(converted_ymd, cd), number=number
        )
        print(f'-Tools...: {test_b}')


# -----------------------------------------------

if __name__ == '__main__':
    run_timings()

# -----------------------------------------------
# End.
