from gpiozero import RGBLED
from time import sleep
from signal import pause

led = RGBLED(red=9, green=10, blue=11)
#led.color = (0,0.1569,1)

for red in range(10):
    for green in range(10):
        for blue in range(10):
            led.color = (red/10.0,green/10.0,blue/10.0)
            sleep(0.2)

pause()