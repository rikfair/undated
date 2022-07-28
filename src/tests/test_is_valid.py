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

import undated._core as udc      # noqa

# -----------------------------------------------


class TestIsValid(unittest.TestCase):
    """ Tests the is_valid function """

    def test_valid(self):
        """ Tests valid parameters give expected answers, benchmarking against datetime """

        for iyr in range(1890, 2890):
            for imn in range(0, 15):
                for idy in range(0, 35):
                    # ---
                    try:
                        datetime.datetime(iyr, imn, idy)
                    except ValueError:
                        dt_valid = False
                    else:
                        dt_valid = True
                    # ---
                    ud_valid = udc.is_valid(iyr, imn, idy)
                    self.assertEqual(dt_valid, ud_valid, f'Unexpected date: {iyr}_{imn}_{idy}')


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()

# -----------------------------------------------
# End
