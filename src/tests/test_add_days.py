#!/usr/bin/python3
# -----------------------------------------------
"""
Unit tests for the undated module
Benchmarking against datetime

**ASSUMPTIONS**
    No assumptions to note

**LIMITATIONS**
    No limitations to note
"""
# -----------------------------------------------

import datetime
import unittest
from dataclasses import dataclass

import undated as ud
import undated.utils as udu

# -----------------------------------------------


@dataclass
class TestData:
    """ Test data record """
    iymd: int
    days: int
    comment: str


TEST_DATA = (
    TestData(2022_01_01, 10, 'Initial test from 1/1'),
    # ---
    TestData(2022_12_01, 1, 'Add spanning month and year, normal'),
    TestData(2022_01_31, -1, 'Minus spanning month and year, normal'),
    # ---
    TestData(2022_01_29, 1, '29/1 + 1 on non leap year = 28/2'),
    TestData(2022_01_30, 1, '30/1 + 1 on non leap year = 28/2'),
    TestData(2022_01_31, 1, '31/1 + 1 on non leap year = 28/2'),
    # ---
    TestData(2020_01_29, 1, '29/1 + 1 on leap year = 29/2'),
    TestData(2020_01_30, 1, '30/1 + 1 on leap year = 29/2'),
    TestData(2020_01_31, 1, '31/1 + 1 on leap year = 29/2'),
    # ---
    TestData(2022_03_29, -1, '29/3 - 1 on non leap year = 28/2'),
    TestData(2022_03_30, -1, '30/3 - 1 on non leap year = 28/2'),
    TestData(2022_03_31, -1, '31/3 - 1 on non leap year = 28/2'),
    # ---
    TestData(2020_03_29, -1, '29/3 - 1 on leap year = 29/2'),
    TestData(2020_03_30, -1, '30/3 - 1 on leap year = 29/2'),
    TestData(2020_03_31, -1, '31/3 - 1 on leap year = 29/2'),
    # ---
    TestData(2019_02_28, 12, '28/2 + 1yr, ends on leap year = 28/2'),
    TestData(2019_02_28, 24, '28/2 + 1yr, spans leap year = 28/2'),
    TestData(2020_02_29, -12, '29/2 - 1yr, ends on leap year = 28/2'),
    TestData(2021_02_28, -24, '28/2 - 1yr, spans leap year = 28/2'),
)


# -----------------------------------------------


def get_datetime_answer(input_date, days):
    """ Calculates the datetime answer """

    ans = datetime.datetime.strptime(str(input_date), '%Y%m%d') + datetime.timedelta(days=days)
    ans = int(ans.strftime('%Y%m%d'))
    return ans


# -----------------------------------------------


class TestAddDays(unittest.TestCase):
    """ Tests the add_days function """

    def test_specific(self):
        """ Tests edge values, benchmarking against datetime """

        for i in TEST_DATA:
            for j in [1, -1]:
                i.days = i.days * j
                adday_ans = udu.add_days(i.iymd, i.days)
                dtime_ans = get_datetime_answer(i.iymd, i.days)

                self.assertEqual(adday_ans, dtime_ans, f'Add days udu: {i} ({j})')
                adday_ud_ans = ud.add_days(ud.YMD(i.iymd), i.days)
                self.assertEqual(adday_ans, adday_ud_ans, f'Add days ud: {i} ({j})')

                dbtwn_ans = udu.days_between(i.iymd, adday_ans)
                self.assertEqual(dbtwn_ans, i.days, f'Days between udu: {i} ({j}')
                dbtwn_ud_ans = ud.days_between(ud.YMD(i.iymd), ud.YMD(adday_ans, trusted=True))
                self.assertEqual(dbtwn_ans, dbtwn_ud_ans, f'Days between ud: {i} ({j}')

    # ---

    def test_invalid(self):
        """ Tests invalid parameters are handled as expected """

        ymd = ud.YMD(0)
        self.assertEqual(ymd.iymd, None, 'Invalid ymd')
        self.assertEqual(ud.add_days(ymd, 1), ud.INVALID_YMD)
        self.assertEqual(ud.days_between(ymd, ud.YMD(20220101)), None)

    # ---

    def test_loop(self):
        """ Increamental test, benchmarking against datetime """

        start_year, start_month, start_day = 1998, 1, 1
        start_ud = ud.YMD(start_year, start_month, start_day)
        start_dt = datetime.datetime(start_year, start_month, start_day)

        for factor in [1, -1]:
            for i in range(50_000):
                i *= factor
                test_ud = start_ud + i
                test_dt = int((start_dt + datetime.timedelta(days=i)).strftime('%Y%m%d'))
                self.assertEqual(test_ud, test_dt, f'Not equal: {test_ud}, {i}')


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
