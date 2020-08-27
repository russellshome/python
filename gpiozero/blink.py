#!/usr/bin/env python
"""
Description : Blink an LED
Author      : Russell
E-mail      : russellshome@gmail.com
Date        : 2020/08/26
Circuit     : https://crcit.net/c/98db0b1c4bcc420fbb3f02dd2a52553a
"""
from gpiozero import LED
from time import sleep
print(__doc__)
led = LED(17)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)