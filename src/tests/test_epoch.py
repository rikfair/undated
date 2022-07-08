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

import undated._core as udc   # noqa

# -----------------------------------------------


class TestEpoch(unittest.TestCase):
    """ Tests the epoch calculation """

    def test_benchmark(self):
        """ Tests epoch, benchmarking against datetime """

        start_date = datetime.datetime.strptime('20190701', '%Y%m%d')
        days = 10_000
        expected_epoch = udc.epoch_from_parts(start_date.year, start_date.month, start_date.day)

        for i in range(days):
            day = start_date + datetime.timedelta(days=i)
            this_epoch = udc.epoch_from_parts(day.year, day.month, day.day)
            self.assertEqual(this_epoch, expected_epoch, f'Unexpected epoch: {day}')
            expected_epoch = this_epoch + 1
            day_parts = udc.epoch_to_parts(this_epoch)
            expected_day = datetime.datetime(*day_parts)
            self.assertEqual(day, expected_day, f'Unexpected day: {day}')


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
