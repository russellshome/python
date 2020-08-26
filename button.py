#!/usr/bin/env python3
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
