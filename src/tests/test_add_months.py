#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Unit tests for the undated module
        Benchmarking against datetime

    ASSUMPTIONS:
        No assumptions to note

    LIMITATIONS:
        No limitations to note
"""
# -----------------------------------------------

import datetime
import unittest
from dataclasses import dataclass

from dateutil.relativedelta import relativedelta

import undated.utils as udu

# -----------------------------------------------


@dataclass
class TestData:
    """ Test data record """
    input_date: int
    months: int
    answer: int
    comment: str


TEST_DATA = (
    TestData(2022_01_01, 10, 2022_11_01, 'Initial test from 1/1'),
    # ---
    TestData(2022_12_01, 1, 2023_01_01, 'Add spanning month and year, normal'),
    TestData(2022_01_31, -1, 2021_12_31, 'Minus spanning month and year, normal'),
    # ---
    TestData(2022_01_29, 1, 2022_02_28, '29/1 + 1 on non leap year = 28/2'),
    TestData(2022_01_30, 1, 2022_02_28, '30/1 + 1 on non leap year = 28/2'),
    TestData(2022_01_31, 1, 2022_02_28, '31/1 + 1 on non leap year = 28/2'),
    # ---
    TestData(2020_01_29, 1, 2020_02_29, '29/1 + 1 on leap year = 29/2'),
    TestData(2020_01_30, 1, 2020_02_29, '30/1 + 1 on leap year = 29/2'),
    TestData(2020_01_31, 1, 2020_02_29, '31/1 + 1 on leap year = 29/2'),
    # ---
    TestData(2022_03_29, -1, 2022_02_28, '29/3 - 1 on non leap year = 28/2'),
    TestData(2022_03_30, -1, 2022_02_28, '30/3 - 1 on non leap year = 28/2'),
    TestData(2022_03_31, -1, 2022_02_28, '31/3 - 1 on non leap year = 28/2'),
    # ---
    TestData(2020_03_29, -1, 2020_02_29, '29/3 - 1 on leap year = 29/2'),
    TestData(2020_03_30, -1, 2020_02_29, '30/3 - 1 on leap year = 29/2'),
    TestData(2020_03_31, -1, 2020_02_29, '31/3 - 1 on leap year = 29/2'),
    # ---
    TestData(2019_02_28, 12, 2020_02_28, '28/2 + 1yr, ends on leap year = 28/2'),
    TestData(2019_02_28, 24, 2021_02_28, '28/2 + 1yr, spans leap year = 28/2'),
    TestData(2020_02_29, -12, 2019_02_28, '29/2 - 1yr, ends on leap year = 28/2'),
    TestData(2021_02_28, -24, 2019_02_28, '28/2 - 1yr, spans leap year = 28/2'),
)


# -----------------------------------------------


def datetime_answer(input_date, months):
    """ Calculates the datetime answer """

    ans = datetime.datetime.strptime(str(input_date), '%Y%m%d') + relativedelta(months=months)
    ans = int(ans.strftime('%Y%m%d'))
    return ans


# -----------------------------------------------


class TestAddMonths(unittest.TestCase):
    """ Tests the add_months function """

    def test_valid(self):
        """ Tests valid parameters give expected answers, benchmarking against datetime """

        for i in TEST_DATA:
            self.assertEqual(
                udu.add_months(i.input_date, i.months),
                datetime_answer(i.input_date, i.months),
                f'Unexpected answer: {i.input_date} + {i.months}; {i.comment}'
            )


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
