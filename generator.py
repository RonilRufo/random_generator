#!/usr/bin/env python
from __future__ import print_function

import os
import random
import string
import sys


def random_integer():
    """
    Returns random Integer.
    """
    return random.randint(0, sys.maxint)


def random_real_number():
    """
    Returns random real number.
    """
    return random.uniform(0, sys.maxint)


def generate_random_str(string_type, length=24):
    """
    Generates a random string based on the given 'string_type' parameter.

    The alphanumerics should contain a random number of spaces before and after
    it (not exceeding 10 spaces).
    """
    value = ""
    if string_type == "alphabetical":
        charset = string.ascii_lowercase
        value = ''.join(random.choice(charset) for x in range(length))
    elif string_type == "alphanumerics":
        charset = string.ascii_lowercase + string.digits
        value = ''.join(random.choice(charset) for x in range(length))

        # Prepend random number of spaces to value
        for space in range(random.randint(0, 10)):
            value = " " + value

        # Append random number of spaces to value
        for space in range(random.randint(0, 10)):
            value += " "

    return value


def generator():
    """
    Generates four(4) types of printable random objects and store them in a single file.
    each object will be separated by a ",".  These are the 4 objects: 
        - alphabetical strings
        - real numbers
        - integers
        - alphanumerics

    The output should be 10MB in size.
    """
    printable_types = ["real_numbers", "integer", "alphabetical", "alphanumerics"]
    
    counter = 1

    f = open("random.txt", "w")

    print(">>>>> Generating Random Objects <<<<<")
    while os.stat("random.txt").st_size < 10000000:
        f = open("random.txt", "a")
        type_lookup = {
            "real_numbers": random_real_number(),
            "integer": random_integer(),
            "alphabetical": generate_random_str("alphabetical"),
            "alphanumerics": generate_random_str("alphanumerics")
        }
        value = type_lookup[random.choice(printable_types)]
        delimiter = ",\n" if counter % 4 == 0 else ","  # split lines by 4 values per line

        file_value = str(value) + delimiter
        f.seek(0)
        f.write(file_value)
        counter += 1
    f.close()
    print(">>>>> Successfully Generated Random Objects <<<<<")


if __name__ == "__main__":
    generator()
