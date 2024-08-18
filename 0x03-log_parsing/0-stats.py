#!/usr/bin/python3
"""
This module parses logs which are read line by line
from the stdin, and prints out the file size and the
status codes from each line in stdin

"""

import sys


def print_metrics(status_codes, file_size):
    """ function that prints metrics """

    print("File size: {}".format(file_size))
    for status_code in sorted(status_codes):
        if status_codes[status_code] != 0:
            print("{}: {}".format(status_code, status_codes[status_code]))


if __name__ == '__main__':
    count = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            line_elements = line.split()
            count += 1

            if len(line_elements) >= 2 and len(line_elements) <= 9:
                if line_elements[-1].isdigit():
                    file_size += int(line_elements[-1])
                if line_elements[-2] in status_codes:
                    status_codes[line_elements[-2]] += 1
            if count % 10 == 0:
                print_metrics(status_codes, file_size)
        print_metrics(status_codes, file_size)
    except KeyboardInterrupt:
        print_metrics(status_codes, file_size)
        raise