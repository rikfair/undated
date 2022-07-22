#!/usr/bin/python3
# -----------------------------------------------
"""
    DESCRIPTION:
        Functions for managing dates in unknown formats

    ASSUMPTIONS:
        fixme

    LIMITATIONS:
        fixme
"""
# -----------------------------------------------

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date
from typing import Tuple, Union

from . import _core as udc
from . import _data as udd

# -----------------------------------------------

THIS_YEAR = int(date.today().strftime('%Y'))
PIVOT_YEAR = THIS_YEAR - 80

# -----------------------------------------------
# Keys

YEAR = 'year'
MONTH = 'month'
DAY = 'day'

# ---
# Hints

Y2 = 101
YM = 102

# ---
# Params

HINTS = 201
LANGUAGES = 202
TIME_SEPARATOR = 203
YY_PIVOT = 204

# ---
# Steps

SEPARATORS = 301
TEXT_MONTH = 302
TIME_LOOP = 303
TIME_ONCE = 304
Y2_TO_Y4 = 305

# -----------------------------------------------


def _int_only_up_to_char(sdate, char):
    """  Returns ints up to to the specified character """

    sdate_char = ''.join(filter((lambda c: c.isdigit() or c == char), sdate))
    if sdate_char.count(char) == 1:
        sdate_split0 = sdate.split(char)[0]
        if len(sdate_split0) > 7:
            sdate_split0_digits = ''.join(filter((lambda c: c.isdigit()), sdate_split0))
            if len(sdate_split0_digits) < 9:
                return sdate_split0
    return None


# -----------------------------------------------


def _remove_time(sdate: str) -> str:
    """ Uses common format rules to remove the time element from the string """

    sdate_digits = ''.join(filter((lambda c: c.isdigit()), sdate))

    if len(sdate_digits) > 8:

        if sdate.count('T') == 1 and sdate.count(' ') == 0:
            sdate = _int_only_up_to_char(sdate, 'T')

        elif sdate.count(' ') == 1:
            sdate = _int_only_up_to_char(sdate, ' ')

        elif ' ' in sdate:
            sdate = sdate.rsplit(' ', 1)[0]
            _remove_time(sdate)

    return sdate


# -----------------------------------------------


def _split_int(value: int, split: Union[list, tuple], keys: Union[list, tuple]):
    """ Splits the int value into potential date parts  """

    results = []
    for i in reversed(split):
        factor = 10 ** i
        results.insert(0, value % factor)
        value = value // factor

    return dict(zip(keys, results))


# -----------------------------------------------


def _split_str(string: str) -> list:
    """ Splits a string based on the change from numbers to strings """

    last_char = string[:1].isdigit()
    new_string = ''
    for i in string:
        digit = i.isdigit()
        if last_char != digit:
            new_string += '\t'
        new_string += i
        last_char = digit
    return new_string.split('\t')


# -----------------------------------------------


def _separators(sdate):
    """ Standardises the separator to a tab character """

    for sep in [' ', '-', '/']:
        sdate = sdate.replace(sep, '\t')

    return sdate.strip('\t')


# -----------------------------------------------


def _standardise_text(sdate: str) -> str:
    """ Standardises the date string to get a better match """

    return sdate.upper().replace('Ä', 'A').replace('É', 'E').replace('Û', 'U')


# -----------------------------------------------


def _text_month(sdate: str, steps: dict) -> str:
    """ Processes the date if text is found within the date string """

    sdate = _standardise_text(sdate)
    step = steps[TEXT_MONTH]

    # ---

    if isinstance(step, tuple):  # (language, position, used_parts)
        parts = sdate.split('\t') if '\t' in sdate else _split_str(sdate)
        for i, month in enumerate(udd.MONTH_NAMES[step[0]]):
            if month == parts[step[1]]:
                parts[step[1]] = str(i + 1).zfill(2)
                break
        return '\t'.join([parts[i] for i in step[2]])

    # ---

    separators = SEPARATORS in steps

    if isinstance(step, list):
        langs = step
    elif isinstance(step, str):
        langs = [step]
    else:
        langs = list(udd.MONTH_NAMES)

    for lang in langs:
        for i, month in enumerate(udd.MONTH_NAMES[lang]):
            if separators:
                month = f'\t{month}\t'
            if month in sdate:
                return sdate.replace(month, str(i + 1).zfill(2))

    return sdate  # Month not found


# -----------------------------------------------


def _validated_yy_pivot(yy_pivot: int) -> int:
    """ Validates the yy_pivot parameter, returns the default if not specified """

    if yy_pivot is None:
        return PIVOT_YEAR
    if 1582 < yy_pivot < 9999:
        return yy_pivot
    raise ValueError(f'Invalid yy_pivot value: {yy_pivot}')


# -----------------------------------------------


def _y2_to_y4(year: int, yy_pivot: int) -> int:
    """ Converts two digit year to four digits """

    return year + (yy_pivot // 100) + (1 if year < (yy_pivot % 100) else 0)


# -----------------------------------------------


def as_iymd(
        idate: Union[datetime, date, float, int, str],
        fmt: str = 'Ymd',
        yy_pivot: Union[int, None] = None
) -> Union[int, None]:
    """
    Converts idate to its year, month, day parts
    :param idate: int, or other type, to allow flexibility with incoming data
    :param fmt: str, the date format
    :param yy_pivot: int, the year for two digit years to pivot at
    :return: tuple (year, month, day)
    """

    return udc.glue_parts(*as_parts(idate, fmt, yy_pivot))


# -----------------------------------------------


def as_parts(
        idate: Union[datetime, date, float, int, str],
        fmt: str = 'Ymd',
        yy_pivot: Union[int, None] = None
) -> Union[Tuple[int, int, int], None]:
    """
    Converts idate to its year, month, day parts
    :param idate: int, or other type, to allow flexibility with incoming data
    :param fmt: str, the date format
    :param yy_pivot: int, the year for two digit years to pivot at
    :return: tuple (year, month, day)
    """

    ymd_type = type(idate)
    if ymd_type == int:
        return udc.as_parts(idate, fmt=fmt, yy_pivot=yy_pivot)
    if ymd_type in [datetime, date]:
        return udc.as_parts(int(idate.strftime('%Y%m%d')), 'Ymd')
    if ymd_type == float or (ymd_type == str and idate.isdigit()):
        return udc.as_parts(int(idate), fmt=fmt, yy_pivot=yy_pivot)
    return None


# -----------------------------------------------


@dataclass
class UndatedFormat:
    """ x """
    split: list[int, int, int]
    keys: list[str, str, str]
    steps: dict
    valid: bool


# -----------------------------------------------


def convert_format(fmt: str) -> UndatedFormat:
    """
    Converts the basic string format into UndatedFormat
    :param fmt: The string format, EG Ymd, ymd, etc
    """

    split = []
    keys = []
    steps = {}

    if 'M' in fmt:
        steps[TEXT_MONTH] = None

    if '-' in fmt:
        steps[SEPARATORS] = None

    for i in fmt:
        if i == 'y':
            split.append(2)
            keys.append(YEAR)
        elif i == 'Y':
            split.append(4)
            keys.append(YEAR)
        elif i in ['m', 'M']:
            split.append(2)
            keys.append(MONTH)
        elif i == 'd':
            split.append(2)
            keys.append(DAY)

    return UndatedFormat(split, keys, steps, len(split) == 3)


# -----------------------------------------------


def convert_to_parts(sdate: Union[int, str], fmt: [str, UndatedFormat]) -> Union[tuple, None]:
    """
    Converts the sdate to year, month, day, based on the format
    :param sdate: the date as a str or int
    :param fmt: the date format, as either a basic format as a string, or a derived format
    """

    udfmt = convert_format(fmt) if isinstance(fmt, str) else fmt
    if not udfmt.valid:
        return None

    # ---

    if TIME_ONCE in udfmt.steps:
        sdate = _int_only_up_to_char(sdate, udfmt.steps[TIME_ONCE])

    if TIME_LOOP in udfmt.steps:
        sdate_digits = ''.join(filter((lambda c: c.isdigit()), sdate))
        while ' ' in sdate and len(sdate_digits) > 8:
            sdate = sdate.rsplit(' ', 1)[0]
            sdate_digits = ''.join(filter((lambda c: c.isdigit()), sdate))

    if SEPARATORS in udfmt.steps:
        sdate = _separators(sdate)

    if TEXT_MONTH in udfmt.steps and isinstance(sdate, str):
        sdate = _text_month(sdate, udfmt.steps)

    # ---

    if isinstance(sdate, str):
        if sdate.isdigit():
            sdate = int(sdate)
        else:
            sdate = int(''.join(filter((lambda c: c.isdigit()), sdate)))

    parts = _split_int(sdate, udfmt.split, udfmt.keys)

    # ---

    if parts[YEAR] < 100:
        parts[YEAR] = _y2_to_y4(parts[YEAR], _validated_yy_pivot(udfmt.get(Y2_TO_Y4)))

    # ---

    if udc.is_valid(**parts):
        return parts['year'], parts['month'], parts['day']
    return None


# -----------------------------------------------


class Deriver:
    """ Tries to derive the date format from the date data provided """

    def __init__(self):
        """
        Searches through date data to find a format that fits all.
        BIG assumption... is that all dates in the data are of the same format.
        """

        self.params = {
            HINTS: [],
            LANGUAGES: [],
            TIME_SEPARATOR: 'T',
            YY_PIVOT: PIVOT_YEAR
        }

    # ---
    # Private methods

    def _evolve_idate(self, idate: Union[list, int], split: tuple) -> dict:
        """ Common evolution steps """

        idate_split = (
            _split_int(idate, *split) if isinstance(idate, int)
            else dict(zip(split[1], [int(i) for i in idate]))
        )

        if idate_split[YEAR] < 100:
            idate_split[YEAR] = _y2_to_y4(idate_split[YEAR], self.params[YY_PIVOT])
        if DAY not in idate_split:
            idate_split[DAY] = 1

        return idate_split

    # ---

    def _expunge_time(self, sdate: str, steps: dict) -> str:
        """ Uses common format rules to remove the time element from the string """

        if self.params[TIME_SEPARATOR] is None:
            return sdate

        sdate_digits = ''.join(filter((lambda c: c.isdigit()), sdate))

        if len(sdate_digits) > 8:

            if sdate.count(self.params[TIME_SEPARATOR]) == 1 and sdate.count(' ') == 0:
                sdate = _int_only_up_to_char(sdate, self.params[TIME_SEPARATOR])
                steps[TIME_ONCE] = self.params[TIME_SEPARATOR]

            elif sdate.count(' ') == 1:
                sdate = _int_only_up_to_char(sdate, ' ')
                steps[TIME_ONCE] = ' '

            elif ' ' in sdate:
                while ' ' in sdate and len(sdate_digits) > 8:
                    sdate = sdate.rsplit(' ', 1)[0]
                    sdate_digits = ''.join(filter((lambda c: c.isdigit()), sdate))
                steps[TIME_LOOP] = None

        return sdate

    # ---

    def _only_digits(self, sdate: str, dlen: int) -> list[tuple]:
        """ Process the date if only digits exist """

        idate = int(sdate)
        results = []
        # ---
        splits = udd.SPLITS['6Y2' if dlen == 6 and Y2 in self.params[HINTS] else dlen]

        for split in splits:
            idate_split = self._evolve_idate(idate, split)
            if udc.is_valid(**idate_split):
                results.append(split)

        return results

    # ---

    def _separated_digits(self, sdate: str, dlen: int) -> list[tuple]:
        """ Process the date if only seperated digits exist """

        results = []
        parts = sdate.split('\t')
        len_parts = len(parts)
        splits = udd.SPLITS['6Y2' if dlen == 6 and Y2 in self.params[HINTS] else dlen]

        for split in splits:
            if len(split[1]) == len_parts:
                idate_split = self._evolve_idate(parts, split)
                if udc.is_valid(**idate_split):
                    results.append(split)

        return results

    # ---

    def _text_month(self, sdate: str) -> tuple[list[tuple], tuple]:
        """ Processes the date if text is found within the date string """

        results = []
        found = None
        stext = _standardise_text(sdate)
        orig_parts = stext.split('\t') if '\t' in stext else _split_str(stext)
        used_parts = []

        # ---

        for i, part in enumerate(orig_parts):
            if part.isdigit():
                used_parts.append(i)
            else:
                for lang, months in udd.MONTH_NAMES.items():
                    if not self.params[LANGUAGES] or lang in self.params[LANGUAGES]:
                        for imonth, smonth in enumerate(months):
                            if part == smonth:
                                if found:
                                    return [], tuple()
                                found = lang, i, len(used_parts), str(imonth + 1).zfill(2)
                                used_parts.append(i)
                                break

        # ---

        if not found:
            return [], tuple()

        # ---

        idate_parts = [found[3] if i == found[1] else orig_parts[i] for i in used_parts]
        dlen = len(''.join(idate_parts))
        len_parts = len(idate_parts)
        splits = udd.SPLITS['6Y2' if dlen == 6 and Y2 in self.params[HINTS] else dlen]

        for split in splits:
            if len(split[1]) == len_parts and split[1][found[2]] == MONTH:
                idate_split = self._evolve_idate(idate_parts, split)
                if udc.is_valid(**idate_split):
                    results.append(split)

        # ---

        return results, (found[0], found[1], used_parts)

    # ---
    # Public methods

    def search(self, dates: Union[list, str, tuple]) -> Union[UndatedFormat, None]:
        """
        Search through a list of dates to derive the date format
        :param dates: list or tuple of dates to search. Or str for one date
        :return: the derived UndatedFormat
        """

        if isinstance(dates, str):
            dates = [dates]

        # ---

        adjust_len = (2 if Y2 in self.params[HINTS] else 0) + (2 if YM in self.params[HINTS] else 0)
        expected_len = 8 - adjust_len

        # ---

        for sdate in dates:
            steps = {}
            if Y2 in self.params[HINTS]:
                steps[Y2_TO_Y4] = self.params[PIVOT_YEAR]
            if not sdate.isdigit():
                sdate = self._expunge_time(sdate, steps)
            if sdate.isdigit():
                if expected_len - 2 < len(sdate) <= expected_len:
                    # Checking one character shorter, as assume leading zero may be lost
                    formats = self._only_digits(sdate, expected_len)
                else:
                    formats = []
            else:
                sdate = _separators(sdate)
                no_seps = sdate.replace('\t', '')
                if sdate != no_seps:
                    steps[SEPARATORS] = None
                if no_seps.isdigit() and expected_len - 2 < len(no_seps) <= expected_len:
                    formats = self._separated_digits(sdate, expected_len)
                else:
                    formats, lang_pos = self._text_month(sdate)
                    if lang_pos:
                        steps[TEXT_MONTH] = lang_pos

            # ---

            if formats and len(formats) == 1:
                return UndatedFormat(formats[0][0], formats[0][1], steps, True)

        # ---

        return None

    # ---

    def set_parameters(self, params: dict):
        """
        Sets the optional parameters for the search
        :param params: possible parameters; hints, languages, yy_pivot
        """

        for k, v in params.items():
            if k in [HINTS, LANGUAGES] and isinstance(v, str):
                v = [v]
            elif k == YY_PIVOT:
                v = _validated_yy_pivot(v)
            # ---
            if k == LANGUAGES:  # Expand two character codes
                langs = []
                for lang in v:
                    if len(lang) == 2:
                        langs.extend([f'{lang}1', f'{lang}2'])
                    else:
                        langs.append(lang)
                self.params[k] = langs
            else:
                self.params[k] = v


# -----------------------------------------------
# End.
