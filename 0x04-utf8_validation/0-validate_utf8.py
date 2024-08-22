#!/usr/bin/python3
"""
This method checks a data set to determine if
it is a valid data set

"""


def validUTF8(data):
    """
    function that checks the utf-8 validity of
    a dataset, which is passed as an argument.
    This function returns true if the data is a
    valid utf-8 encoding, else it returns false.

    """

    try:
        bytes(data).decode('utf-8')
        return True
    except (ValueError, UnicodeDecodeError):
        return False