import time

_this_year = time.strftime("%Y")
__version__ = "0.2.2"
__author__ = "Maxwell Weinzierl"
__author_email__ = "maxwell.weinzierl@utdallas.edu"
__license__ = "Apache-2.0"
__copyright__ = f"Copyright (c) 2021-{_this_year}, {__author__}."
__homepage__ = "https://github.com/Supermaxman/elearning-grading"
__docs_url__ = "https://github.com/Supermaxman/elearning-grading"
# this has to be simple string, see: https://github.com/pypa/twine/issues/522
__docs__ = "Python utilities to help Teaching Assistants grade assignments with eLearning"
__long_docs__ = """
Python utilities to help Teaching Assistants grade assignments with eLearning
-------------
- https://github.com/Supermaxman/elearning-grading
"""

__all__ = ["__author__", "__author_email__", "__copyright__", "__docs__", "__homepage__", "__license__", "__version__"]
