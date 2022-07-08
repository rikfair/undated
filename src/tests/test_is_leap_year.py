#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Unit tests for the undated module
        Benchmarking against calendar

    ASSUMPTIONS:
        No assumptions to note

    LIMITATIONS:
        No limitations to note
"""
# -----------------------------------------------

import calendar
import unittest

import undated._core as udc      # noqa

# -----------------------------------------------


class TestDayOfWeek(unittest.TestCase):
    """ Tests the add_days function """

    def test_valid(self):
        """ Tests valid parameters give expected answers, benchmarking against calendar """

        for i in range(1890, 2890):
            cleap = calendar.isleap(i)
            uleap = udc.is_leap_year(i)
            self.assertEqual(cleap, uleap, f'Unexpected answer: {i}')


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
