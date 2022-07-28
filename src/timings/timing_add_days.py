#!/usr/bin/python3
# -----------------------------------------------
"""
Timing to check how the undated module compares with datetime
when using dates that are int type

**ASSUMPTIONS**
    No assumptions to note

**LIMITATIONS**
    No limitations to note
"""
# -----------------------------------------------

import datetime
import timeit

import undated.utils as udu

# -----------------------------------------------


def run_timings(number=10_000, ymd=2020_01_15, days=None):
    """ Executes the timing routine """

    if not days:
        days = [1, -1, 12, -12, 30, -30, 100, -100]

    for day in days:
        print(f'\nTiming days: {day}')
        test_a = timeit.timeit(lambda d=day: udu.add_days(ymd, d), number=number)
        print(f'-Undated...: {test_a}')
        test_b = timeit.timeit(lambda d=day: int(
            (datetime.datetime.strptime(str(ymd), '%Y%m%d')
             + datetime.timedelta(days=d)).strftime('%Y%m%d')), number=number)
        print(f'-DateTime..: {test_b}')


# -----------------------------------------------

if __name__ == '__main__':
    run_timings()

# -----------------------------------------------
# End.
