#!/usr/bin/env python3
"""
This is a docstring

the first line allows the file to be run as a script
"""

class Test:
    """
    docstring for the class test

    more info
    """

    def __init__(self, name):
        self.name = name

print(__doc__)
print(Test.__doc__)