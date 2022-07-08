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


def run_timings(number=10_000, ymd=2019_01_15, data=None):
    """ Executes the timing routine. """

    converted_ymd = ud.YMD(ymd)

    if not data:
        data = [(2022_01_01, 'Ymd'), (2022_01, 'Ym'), (12_01_22, 'mdy')]

    for i in data:
        print(f'\nTiming as_ymd: {i}')
        test_a = timeit.timeit(lambda: ud.as_ymd(*i), number=number)
        print(f'-Undated...: {test_a}')


# -----------------------------------------------

if __name__ == '__main__':
    run_timings()

# -----------------------------------------------
# End.
