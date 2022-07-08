#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Timing to check how the undated module compares with datetime
        when using dates that are int type

    ASSUMPTIONS:
        No assumptions to note

    LIMITATIONS:
        No limitations to note
"""
# -----------------------------------------------

import datetime
import timeit

from dateutil.relativedelta import relativedelta

import undated as ud
import undated.utils as udu

# -----------------------------------------------


def run_timings(number=10_000, iymd=2019_01_15, months=None):
    """ Executes the timing routine """

    if not months:
        months = [1, -1, 12, -12, 20, -20, 100, -100]

    ymd = ud.YMD(iymd)

    for mth in months:
        print(f'\nTiming months: {mth}')
        test_a = timeit.timeit(lambda: udu.add_months(iymd, mth), number=number)
        print(f'-Utils.....: {test_a}')
        test_b = timeit.timeit(lambda: ud.add_months(ymd, mth), number=number)
        print(f'-Tools.....: {test_b}')
        test_c = timeit.timeit(lambda: int(
            (datetime.datetime.strptime(str(iymd), '%Y%m%d')
             + relativedelta(months=mth)).strftime('%Y%m%d')), number=number)
        print(f'-DateTime..: {test_c}')


# -----------------------------------------------

if __name__ == '__main__':
    run_timings()

# -----------------------------------------------
# End.
