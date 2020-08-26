#!/usr/bin/env python
"""
Description : Press button to make LED flash
Author      : Russell
E-mail      : russellshome@gmail.com
Date        : 2020/08/26
Circuit     : https://crcit.net/c/6d7e54db10d4410b9e11d9e287187565
"""
from gpiozero import LED, Button
from time import sleep
from signal import pause

button = Button(2)
led = LED(17)

def toggleLed():
    if led._blink_thread == None:
        led.blink(0.2,0.2)
    else:
        led.off()

button.when_pressed = toggleLed

pause()
