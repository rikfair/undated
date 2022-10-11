#!/usr/bin/python3
# -----------------------------------------------
"""
Unit tests for the undated module

**ASSUMPTIONS**
    No assumptions to note

**LIMITATIONS**
    No limitations to note
"""
# -----------------------------------------------

import unittest

import undated.utils as udu

# -----------------------------------------------


class TestFirstLastDays(unittest.TestCase):
    """ Tests the Tests first_day, last_day functions """

    def test_first_last(self):
        """ Testing against each month in the year, including leap and non leap years """

        for question, first_expected, last_expected in [
            (202001, 20200101, 20200131),
            (202002, 20200201, 20200229),
            (202003, 20200301, 20200331),
            (202004, 20200401, 20200430),
            (202005, 20200501, 20200531),
            (202006, 20200601, 20200630),
            (202007, 20200701, 20200731),
            (202008, 20200801, 20200831),
            (202009, 20200901, 20200930),
            (202010, 20201001, 20201031),
            (202011, 20201101, 20201130),
            (202012, 20201201, 20201231),
            (202102, 20210201, 20210228),
        ]:
            first_answer = udu.first_day(question)
            self.assertEqual(first_expected, first_answer, f'Unexpected first: {question}')
            last_answer = udu.last_day(question)
            self.assertEqual(last_expected, last_answer, f'Unexpected last: {question}')


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
