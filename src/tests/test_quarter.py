#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Unit tests for the undated module.
        No similar function in datetime for benchmarking.

    ASSUMPTIONS:
        No assumptions to note

    ACCURACY:
        No accuracy issues to note
"""
# -----------------------------------------------

import unittest
from dataclasses import dataclass
from typing import Union

import undated.utils as udu

# -----------------------------------------------


@dataclass
class TestData:
    """ Test data record """
    input_date: int
    to_str: bool
    answer: Union[int, str]
    comment: str


TEST_DATA = (
    TestData(2022_01_15, False, 202203, 'Ymd quarter end test for 01'),
    TestData(2022_02_15, False, 202203, 'Ymd quarter end test for 02'),
    TestData(2022_03_15, False, 202203, 'Ymd quarter end test for 03'),
    TestData(2022_04_15, False, 202206, 'Ymd quarter end test for 04'),
    TestData(2022_05_15, False, 202206, 'Ymd quarter end test for 05'),
    TestData(2022_06_15, False, 202206, 'Ymd quarter end test for 06'),
    TestData(2022_07_15, False, 202209, 'Ymd quarter end test for 07'),
    TestData(2022_08_15, False, 202209, 'Ymd quarter end test for 08'),
    TestData(2022_09_15, False, 202209, 'Ymd quarter end test for 09'),
    TestData(2022_10_15, False, 202212, 'Ymd quarter end test for 10'),
    TestData(2022_11_15, False, 202212, 'Ymd quarter end test for 11'),
    TestData(2022_12_15, False, 202212, 'Ymd quarter end test for 12'),
    # ---
    TestData(2022_01_15, True, '2022Q1', 'Ymd quarter number test for 01'),
    TestData(2022_02_15, True, '2022Q1', 'Ymd quarter number test for 02'),
    TestData(2022_03_15, True, '2022Q1', 'Ymd quarter number test for 03'),
    TestData(2022_04_15, True, '2022Q2', 'Ymd quarter number test for 04'),
    TestData(2022_05_15, True, '2022Q2', 'Ymd quarter number test for 05'),
    TestData(2022_06_15, True, '2022Q2', 'Ymd quarter number test for 06'),
    TestData(2022_07_15, True, '2022Q3', 'Ymd quarter number test for 07'),
    TestData(2022_08_15, True, '2022Q3', 'Ymd quarter number test for 08'),
    TestData(2022_09_15, True, '2022Q3', 'Ymd quarter number test for 09'),
    TestData(2022_10_15, True, '2022Q4', 'Ymd quarter number test for 10'),
    TestData(2022_11_15, True, '2022Q4', 'Ymd quarter number test for 11'),
    TestData(2022_12_15, True, '2022Q4', 'Ymd quarter number test for 12'),
    # ---
    TestData(2022_01, False, 202203, 'Ym quarter end test for 01'),
    TestData(2022_02, False, 202203, 'Ym quarter end test for 02'),
    TestData(2022_03, False, 202203, 'Ym quarter end test for 03'),
    TestData(2022_04, False, 202206, 'Ym quarter end test for 04'),
    TestData(2022_05, False, 202206, 'Ym quarter end test for 05'),
    TestData(2022_06, False, 202206, 'Ym quarter end test for 06'),
    TestData(2022_07, False, 202209, 'Ym quarter end test for 07'),
    TestData(2022_08, False, 202209, 'Ym quarter end test for 08'),
    TestData(2022_09, False, 202209, 'Ym quarter end test for 09'),
    TestData(2022_10, False, 202212, 'Ym quarter end test for 10'),
    TestData(2022_11, False, 202212, 'Ym quarter end test for 11'),
    TestData(2022_12, False, 202212, 'Ym quarter end test for 12'),
    # ---
    TestData(2022_01, True, '2022Q1', 'Ym quarter number test for 01'),
    TestData(2022_02, True, '2022Q1', 'Ym quarter number test for 02'),
    TestData(2022_03, True, '2022Q1', 'Ym quarter number test for 03'),
    TestData(2022_04, True, '2022Q2', 'Ym quarter number test for 04'),
    TestData(2022_05, True, '2022Q2', 'Ym quarter number test for 05'),
    TestData(2022_06, True, '2022Q2', 'Ym quarter number test for 06'),
    TestData(2022_07, True, '2022Q3', 'Ym quarter number test for 07'),
    TestData(2022_08, True, '2022Q3', 'Ym quarter number test for 08'),
    TestData(2022_09, True, '2022Q3', 'Ym quarter number test for 09'),
    TestData(2022_10, True, '2022Q4', 'Ym quarter number test for 10'),
    TestData(2022_11, True, '2022Q4', 'Ym quarter number test for 11'),
    TestData(2022_12, True, '2022Q4', 'Ym quarter number test for 12'),
)

# -----------------------------------------------


class TestAddMonths(unittest.TestCase):
    """ Tests the add_months function """

    def test_int(self):
        """ Tests the datetime and date types """

        for i in TEST_DATA:
            self.assertEqual(
                udu.quarter(i.input_date, i.to_str),
                i.answer,
                f'Unexpected answer: {i.input_date}; {i.comment}'
            )


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
