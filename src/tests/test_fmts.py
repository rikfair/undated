#!/usr/bin/python3
# -----------------------------------------------
"""
Unit tests for the undated.fmts module

**ASSUMPTIONS**
    No assumptions to note

**LIMITATIONS**
    No limitations to note
"""
# -----------------------------------------------

import unittest

import undated.fmts as udf

# -----------------------------------------------
# Allowing test data to exceed line length, so each group fits on one line
# pylint: disable=line-too-long

TEST_DATA = (
    (('20-mar-20', (2020, 3, 20)), ('21-apr-20', (2020, 4, 21)), ('22-may-20', (2020, 5, 22))),
    (('20mar20', (2020, 3, 20)), ('21apr20', (2020, 4, 21)), ('22may20', (2020, 5, 22))),
    (('11/25/2020 7:00PM Europe/Berlin', (2020, 11, 25)),),
    (('25.11.2020 7:00PM Europe/Berlin', (2020, 11, 25)),),
    (('Monday, 24 May 2021 05:50', (2021, 5, 24)), ('Monday, 27 June 2021 05:50', (2021, 6, 27))),
    (('Mon, 25 Jan 2021 05:50:06 GMT', (2021, 1, 25)), ('Mon, 27 Dec 2021 05:50:06 GMT', (2021, 12, 27))),
    (('Mon, 25 Jan 2021 05:50:06 GMT', (2021, 1, 25)), ('Mon, 27 Dec 2021 05:50:06 GMT', (2021, 12, 27))),
    (('Mon, 25 Ene 2021 05:50:06 CET', (2021, 1, 25)), ('Mon, 27 Dic 2021 05:50:06 CET', (2021, 12, 27))),
    (('12092022', (2022, 9, 12)), ('13092022', (2022, 9, 13))),
    (('2021-03-27T05:50:06.7199222-04:00', (2021, 3, 27)),),
    (('03/28/2021 05:50:06', (2021, 3, 28)),),
    (('29MAR2020', (2020, 3, 29)), ('01JAN2020', (2020, 1, 1))),
    (('Monday, 29 March 2021', (2021, 3, 29)),),
    (('Monday, 29 March 2021 05:50 AM', (2021, 3, 29)),),
    (('Monday, 29 March 2021 05:50:06', (2021, 3, 29)),),
)

# pylint: enable=line-too-long
# -----------------------------------------------


class TestAddMonths(unittest.TestCase):
    """ Tests the add_months function """

    def test_search(self):
        """ Tests valid parameters give expected answers """

        for test_dates in TEST_DATA:
            sdates = [i[0] for i in test_dates]
            answers = [i[1] for i in test_dates]
            fmt = udf.Deriver().search(sdates)
            for i, sdate in enumerate(sdates):
                ymd_parts = udf.as_parts(sdate, fmt)
                self.assertEqual(ymd_parts, answers[i], f'{sdate}, {ymd_parts}, {answers[i]}')


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
