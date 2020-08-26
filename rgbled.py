#!/usr/bin/env python
"""
Description : Change colours on an RGB LED
Author      : Russell
E-mail      : russellshome@gmail.com
Date        : 2020/08/26
Circuit     : https://crcit.net/c/8bc8330a72874a9d97dc4b0c0dcb0748

My RGB LED has a common anode
In this case 0 means on full and 1 is off
Other RGB LEDs have a common cathode
In that case 1 means on full and 0 is off
"""
from gpiozero import RGBLED
from time import sleep
from signal import pause
print(__doc__)
led = RGBLED(red=10, green=9, blue=11)
while True:
    led.color = (0,1,1)
    print ("red")
    sleep(5)
    led.color = (1,0,1)  # full green
    print("green")
    sleep(5)
    led.color = (1,1,0)
    print ("blue")
    sleep(5)
    led.color = (0, 1, 0)  # magenta
    print("magenta")
    sleep(5)
    led.color = (0, 0, 1)  # yellow
    print("yellow")
    sleep(5)
    led.color = (1, 0, 0)  # cyan
    print("cyan")
    sleep(5)
    led.color = (0,0,0)  # white
    print("white")
    sleep(5)

"""
# slowly decrease intensity of blue
for n in range(100):
    led.blue = n/100
    sleep(0.1)
"""