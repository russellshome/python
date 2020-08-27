#!/usr/bin/env python
"""
Description : Daisy chained ShiftRegister (74HC595) 
Author      : Russell
E-mail      : russellshome@gmail.com
Date        : 2020/08/27
Circuit     : https://crcit.net/c/189571354f7f4065b1c88aab3b7ff630
"""
from time import sleep
from signal import pause
from collections import OrderedDict
from gpiozero import OutputDevice
print(__doc__)
data_device =  OutputDevice(6, pin_factory=None)
latch_device =  OutputDevice(13, initial_value=True, pin_factory=None)
clock_device = OutputDevice(19, pin_factory=None)

def shift_out(value1,value2):
    latch_device.off()
    for x in range(8):
        data_device.value = (value1 >> x) & 1
        clock_device.on()
        clock_device.off()
    for x in range(8):
        data_device.value = (value2 >> x) & 1
        clock_device.on()
        clock_device.off()
    latch_device.on()

one = int("10000000", 2)
two = int("01000000", 2)
three = int("00100000", 2)
four = int("00010000", 2)
five = int("00001000", 2)
six = int("00000100", 2)
seven = int("00000010", 2)
eight = int("00000001", 2)

sleep_amt = 0.05

while True:
    shift_out(two, 0)
    sleep(sleep_amt)
    shift_out(one, 0)
    sleep(sleep_amt)
    shift_out(0, eight)
    sleep(sleep_amt)
    shift_out(0, seven)
    sleep(sleep_amt)
    shift_out(0, six)
    sleep(sleep_amt)
    shift_out(0, five)
    sleep(sleep_amt)
    shift_out(0, four)
    sleep(sleep_amt)
    shift_out(0, three)
    sleep(sleep_amt)
    shift_out(0, two)
    sleep(sleep_amt)
    shift_out(0, one)
    sleep(sleep_amt)

    shift_out(0, two)
    sleep(sleep_amt)
    shift_out(0, three)
    sleep(sleep_amt)
    shift_out(0, four)
    sleep(sleep_amt)
    shift_out(0, five)
    sleep(sleep_amt)
    shift_out(0, six)
    sleep(sleep_amt)
    shift_out(0, seven)
    sleep(sleep_amt)
    shift_out(0, eight)
    sleep(sleep_amt)
    shift_out(one, 0)
    sleep(sleep_amt)
