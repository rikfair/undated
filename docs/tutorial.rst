Tutorial
========

The Three Modules
-----------------

*undated* consists of three main modules, ``undated``, ``undated.fmts`` and ``undated.utils``.
These are distinctly seperated for performance, to limit import overhead.

**undated** 

The undated module, is the main module for manipulating dates...... 

**undated.fmts**

fmts, short for formatings, is the module for evaluating and deriving unknown date formats.......

**undated.utils**

The utils module is tuned for performance. It has little to no validation on the parameters
and works solely with dates stored as integers in the ``Ymd`` format

.. important::
   The examples assume that the `undated`, `undated.fmts`, and `undated.utils` packages have been imported as `ud`, `udf` and `udu` respectfully.

   .. code-block::

      import undated as ud
      import undated.fmts as udf
      import undated.utils as udu

ud.YMD class
------------

The class ``ud.YMD`` is the go to tool, when manipulation of the dates is required during processing.

.. code-block::

   import undated as ud
   ymd = ud.YMD(2022_07_04)
   print('ymd', ymd)
   print('plus 7 days', ymd + 7)
   print('minus 7 days', ymd - 7)
   print('add 2 months', ymd.add_months(2))
   print('minus 2 months', ymd.add_months(-2))
   print('add 10 weekdays', ymd.add_weekdays(10))
   print('minus 10 weekdays', ymd.add_weekdays(-10))
   print('add 3 years', ymd.add_years(3))
   print('minus 3 years', ymd.add_years(-3))
   print('day of the week', ymd.day_of_week())
   print('is leap year', ymd.is_leap_year())
   print('is weekday', ymd.is_weekday())
   print('the day, month and year', ymd.day, ymd.month, ymd.year)

gives the results

.. code-block::

   ymd 20220704
   plus 7 days 20220711
   minus 7 days 20220627
   add 2 months 20220904
   minus 2 months 20220504
   add 10 weekdays 20220718
   minus 10 weekdays 20220620
   add 3 years 20250704
   minus 3 years 20190704
   day of the week 1
   is leap year False
   is weekday True
   the day, month and year 4 7 2022

