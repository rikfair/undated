import os
import setuptools

import undated as ud

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name = "undated",
    version = ud.__version__,
    author = "rikfair",
    author_email = "mail4rik-pypi@yahoo.com",
    description = "For when dates aren't dates",
    long_description=read('README.rst'),
    long_description_content_type = "text/x-rst",
    url = "https://github.com/rikfair/undated",
    project_urls = {
        "Bug Tracker": "https://github.com/rikfair/undated/issues",
        "Documentation": "https://undated.readthedocs.io/"
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Database",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities"
    ],
    license = "MIT",
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src", exclude=["tests*", "timings*"]),
    python_requires = ">=3.7",
)
