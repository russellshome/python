from gpiozero import RGBLED
from time import sleep
from signal import pause

led = RGBLED(red=9, green=10, blue=11)
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