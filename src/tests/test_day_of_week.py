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

import undated as ud
import undated._core as udc   # noqa

# -----------------------------------------------


class TestDayOfWeek(unittest.TestCase):
    """ Tests the add_days function """

    def test_valid(self):
        """ Tests valid parameters give expected answers, benchmarking against datetime """

        start_iymd = 2019_07_01
        start_date = datetime.datetime.strptime(str(start_iymd), '%Y%m%d')
        days = 10_000

        for i in range(days):
            day = start_date + datetime.timedelta(days=i)
            dt_dow = int(day.strftime('%w'))
            ud_dow = udc.day_of_week(udc.epoch_from_parts(day.year, day.month, day.day))
            self.assertEqual(ud_dow, dt_dow, f'Unexpected day: {day}')
            # ---
            weekday = day.isoweekday() < 6
            self.assertEqual(
                udc.is_weekday(day.year, day.month, day.day), weekday,
                f'Weekday udc: {day}'
            )
            # ---
            ymd = ud.YMD(day.year, day.month, day.day)
            self.assertEqual(ymd.is_weekday(), weekday, f'Weekday ud: {day}')


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
