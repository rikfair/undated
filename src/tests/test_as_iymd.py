#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Unit tests for the undated module

    ASSUMPTIONS:
        No assumptions to note

    LIMITATIONS:
        No limitations to note
"""
# -----------------------------------------------

import unittest
from dataclasses import dataclass
from typing import Optional

import undated.utils as udu

# -----------------------------------------------


@dataclass
class TestData:
    """ Test data record """
    iymd: int
    fmt: str
    yy_pivot: Optional[str]
    answer: Optional[int]
    comment: str


TEST_DATA = (
    TestData(2022_01_01, 'Ymd', None, 2022_01_01, 'Initial Ymd test'),
    TestData(2022_01, 'Ym', None, 2022_01_01, 'No day'),
    TestData(2022_01, 'Yd', None, 2022_01_01, 'No month'),
    TestData(2022, 'Y', None, 2022_01_01, 'Year only'),
    TestData(11_02_2022, 'dmY', None, 2022_02_11, 'dmY format'),
    TestData(1_02_2022, 'dmY', None, 2022_02_01, 'dmY format, missing leading zero'),
    TestData(11_02_2022, 'mdY', None, 2022_11_02, 'mdY format'),
    TestData(2_01_2022, 'mdY', None, 2022_02_01, 'mdY format, missing leading zero'),
    TestData(14_01_2022, 'mdY', None, None, 'Invalid date'),
    TestData(12_01_22, 'mdy', None, 2022_12_01, 'Two digit year'),
)


# -----------------------------------------------


class TestAsInt(unittest.TestCase):
    """ Tests the as_ymd function """

    def test_valid(self):
        """ Tests valid parameters give expected answers """

        for i in TEST_DATA:
            self.assertEqual(
                udu.as_iymd(i.iymd, i.fmt, i.yy_pivot),
                i.answer,
                f'Unexpected answer: {i.iymd} - {i.fmt}; {i.comment}'
            )


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
