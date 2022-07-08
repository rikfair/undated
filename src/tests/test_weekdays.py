#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Unit tests for the undated module.
        No similar function in datetime for benchmarking.
        Testing add_weekdays and weekdays_between

    ASSUMPTIONS:
        No assumptions to note

    ACCURACY:
        No accuracy issues to note
"""
# -----------------------------------------------

import unittest
from dataclasses import dataclass

import undated.utils as udu

# -----------------------------------------------


@dataclass
class TestData:
    """ Test data record """
    input_date: int
    weekdays: int
    answer: int
    comment: str


TEST_DATA = (
    TestData(2022_01_10, 4, 2022_01_14, 'Same week'),
    TestData(2022_01_10, 9, 2022_01_21, 'Span weekend'),
    TestData(2022_01_10, 11, 2022_01_25, 'Span two weekends'),
    TestData(2022_01_11, 40, 2022_03_08, 'Span months'),
    TestData(2022_01_11, 400, 2023_07_25, 'Span years'),
    TestData(2020_02_03, 28, 2020_03_12, 'Leap year'),
)

# -----------------------------------------------


class TestAddWeekdays(unittest.TestCase):
    """ Tests the weekdays functions """

    def test_add_weekdays(self):
        """ Tests the add weekdays function """

        for i in TEST_DATA:
            self.assertEqual(
                udu.add_weekdays(i.input_date, i.weekdays),
                i.answer,
                f'Unexpected answer: {i.input_date}; {i.comment}'
            )

    # ---

    def test_add_weekdays_minus(self):
        """ Tests the add weekdays function """

        for i in TEST_DATA:
            self.assertEqual(
                udu.add_weekdays(i.answer, i.weekdays * -1),
                i.input_date,
                f'Unexpected answer: {i.input_date}; {i.comment}'
            )

    # ---

    def test_weekdays_between(self):
        """ Tests the weekdays between function """

        for i in TEST_DATA:
            self.assertEqual(
                udu.weekdays_between(i.input_date, i.answer),
                i.weekdays,
                f'Unexpected answer: {i.input_date}; {i.comment}'
            )

    # ---

    def test_weekdays_between_reversed(self):
        """ Tests the weekdays between function """

        for i in TEST_DATA:
            self.assertEqual(
                udu.weekdays_between(i.answer, i.input_date),
                i.weekdays * -1,
                f'Unexpected answer: {i.input_date}; {i.comment}'
            )


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
