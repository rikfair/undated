Undated - *"For when dates aren't dates"*
=========================================

*undated* is a Python package that simplifies the process of working with dates that are stored as numbers or strings.

Whilst datatypes should fit their purpose, date types do not always transport well and are converted to a number or string,
such as `ISO 8601 <https://iso.org/iso-8601-date-and-time-format.html>`_, for transportation in text based files like json or csv.

*undated* provides:
 - Functionality to handle dates that are stored in number formats
 - Ability to derive the date format from provided data
 - Direct manipulation to avoid costly type conversions

.. note::

   Although *undated* is wizzy with dates, operating with time elements is out of its scope. 

Inception
=========

*undated* came about due to the need to process large amounts of data from various sources,
where the format of the date was dependant on either the country of origin, source system, or which ever way the wind blew.
One solution was required to enable big data to be processed regardless of its date formatting, *undated*.

Supported Versions
==================

Supported on Python 3.7, 3.8, 3.9 and 3.10

Installation
============

The package can be found on `GitHub <https://github.com/rikfair/undated>`_ and `PyPI <https://pypi.org/project/undated/>`_,
so the easiest way to install it is with `pip``

.. code-block::

   pip install undated

Licence
=======

This software is released under the MIT licence
