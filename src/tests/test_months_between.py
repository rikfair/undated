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

import unittest
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import undated as ud
import undated._core as udc   # noqa

# -----------------------------------------------


class TestMonthsBetween(unittest.TestCase):
    """ Tests the add_days function """

    def test_valid(self):
        """ Tests valid parameters give expected answers, benchmarking against datetime """

        start_iymd = 2019_07_01

        for day in range(50):
            test_date = datetime(*udc.explode_iymd(start_iymd)) + timedelta(days=day)
            test_ymd = ud.YMD(test_date.year, test_date.month, test_date.day)
            for mth in range(50):
                end_date = test_date + relativedelta(months=mth)
                end_ymd = ud.YMD(end_date.year, end_date.month, end_date.day)

                answer = ud.months_between(test_ymd, end_ymd)
                self.assertEqual(answer, mth, f'(+) {test_ymd} -> {end_ymd}, {answer}!={mth}')

                answer = ud.months_between(end_ymd, test_ymd)
                mth = mth * -1
                self.assertEqual(answer, mth, f'(-) {end_ymd} -> {test_ymd}, {answer}!={mth}')


# -----------------------------------------------
# End.
