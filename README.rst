Undated - *"For when dates aren't dates"*
=========================================

.. image:: https://www.codefactor.io/repository/github/rikfair/undated/badge/main
   :target: https://www.codefactor.io/repository/github/rikfair/undated/overview/main
   :alt: CodeFactor

.. image:: https://github.com/rikfair/undated/actions/workflows/codeql-analysis.yml/badge.svg
   :target: https://github.com/rikfair/undated/actions/workflows/codeql-analysis.yml
   :alt: CodeQL

.. image:: https://github.com/rikfair/undated/actions/workflows/pylint.yml/badge.svg
   :target: https://github.com/rikfair/undated/actions/workflows/pylint.yml
   :alt: pylint

.. image:: https://github.com/rikfair/undated/actions/workflows/unittest.yml/badge.svg
   :target: https://github.com/rikfair/undated/actions/workflows/unittest.yml
   :alt: unittest
   
.. image:: https://readthedocs.org/projects/undated/badge/?version=latest
   :target: https://undated.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
   
*undated* is a Python package that simplifies the process of working with dates that are stored as numbers or strings.

Whilst datatypes should fit their purpose, date types do not always transport well and are converted to a number or string,
such as `ISO 8601 <https://iso.org/iso-8601-date-and-time-format.html>`_, for transportation in text based files like json or csv.

*undated* provides:
 - Functionality to handle dates that are stored in number formats
 - Ability to derive the date format from provided data
 - Direct manipulation to avoid costly type conversions

.. note::

   Although *undated* is whizzy with dates, operating with time elements is out of its scope. 

Inception
=========

*undated* came about due to the need to process large amounts of data from various sources. These were received as csv files
where the format of the date was dependant on either the country of origin, source system, or which ever way the wind blew.
One solution was required to enable big data to be processed regardless of its date formatting... *undated*.

Concept
=======

*undated* is a lightweight performance tuned package envisaged to be used either:
 - when processing data from various sources where the date format is unknown but consistent throughout the data
 - or when dates have been stored as integers in the ``Ymd`` format and performance is a consideration.

For other scenarios consider using a feature rich package such as `dateutils <https://pypi.org/project/python-dateutil/>`_

Supported Versions
==================

Supported on Python 3.7, 3.8, 3.9 and 3.10

Installation
============

The package can be found on `GitHub <https://github.com/rikfair/undated>`_ and `PyPI <https://pypi.org/project/undated/>`_,
so naturally it can be installed with `pip`

.. code-block::

   pip install undated

Requirements
============

The ``undated`` package itself has no requirements.

To use the unittests and timings modules ``dateutils`` is required.

.. code-block::

   pip install python-dateutil>=2.8.2

To generate the Sphinx documentation, Sphinx and the RTD template are required.

.. code-block::

   pip install Sphinx>=5.0.2
   pip install sphinx-rtd-theme>=1.0.0

Licence
=======

This software is released under the MIT licence
