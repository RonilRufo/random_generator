#!/usr/bin/env python
from __future__ import print_function


def isfloat(str):
    try: 
        float(str)
    except ValueError: 
        return False
    return True


def reader():
    """
    Reads the generated file above and print to the console the object and its type.

    Sample output :

    youruasdifafasd - alphabetical strings
    127371237 - integer
    asdfka12348fas - alphanumeric
    13123.123 - real numbers
    asjdfklasdjfklaasf - alphabetical strings
    123192u3kjwekhf - alphanumeric

    """
    try:
        f = open("random.txt", "r")
        content = f.read()
        values = content.split(",")
        f.close()
        
        for value in values:
            value = value.replace("\n", "").replace(" ", "")
            if value:
                value_type = None
                if value.isalpha():
                    value_type = "Alphabetical String"
                elif value.isdigit():
                    value_type = "Integer"
                elif value.isalnum():
                    value_type = "Alphanumeric"
                elif isfloat(value):
                    value_type = "Real Numbers"
                print("%s - %s" % (value, value_type))
    except IOError:
        print('>>>>> ERROR: "random.txt" file was not found. Please run generator.py first.')

if __name__ == "__main__":
    reader()
