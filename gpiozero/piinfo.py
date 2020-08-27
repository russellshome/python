#!/usr/bin/env python
"""
Description : Display information about Pi
Author      : Russell
E-mail      : russellshome@gmail.com
Date        : 2020/08/26
"""
from gpiozero import pi_info
print(__doc__)
print('{0}'.format(pi_info()))
print('{0:full}'.format(pi_info()))
print('{0:board}'.format(pi_info()))
print('{0:specs}'.format(pi_info()))
print('{0:headers}'.format(pi_info()))