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

import datetime
import timeit

import undated as ud
import undated.utils as udu

# -----------------------------------------------


def run_timings(number=10_000, iymd=2019_01_15, data=None):
    """ Executes the timing routine. """

    ymd = ud.YMD(iymd, trusted=True)
    dte = datetime.datetime.strptime(str(iymd), '%Y%m%d')

    if not data:
        data = [2022_01_14, 2023_07_25]

    for i in data:
        print(f'\nTiming days between, day: {i}')

        test_a = timeit.timeit(lambda i_=i: udu.days_between(iymd, i_), number=number)
        print(f'-Utils......: {test_a}')

        test_b = timeit.timeit(
            lambda i_=i: ud.days_between(ymd, ud.YMD(i_, trusted=True)),
            number=number
        )
        print(f'-Tools......: {test_b}')

        test_c = timeit.timeit(
            lambda: dte - datetime.datetime.strptime(str(iymd), '%Y%m%d'),
            number=number
        )
        print(f'-Datetime...: {test_c}')


# -----------------------------------------------

if __name__ == '__main__':
    run_timings()

# -----------------------------------------------
# End.
