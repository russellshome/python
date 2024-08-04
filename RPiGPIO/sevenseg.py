#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   sevenseg.py
@Time    :   2024/08/01 22:57:40
@Author  :   Russell Mercer
@Version :   1.0
@Contact :   russellshome@gurudigital.nz
@License :   (C)Copyright Russell Mercer
@Desc    :   Ref: https://pypi.org/project/Pi7SegPy/

Circuit  :   https://crcit.net/c/25ecfad5e0274f6aaebe2bac931ac13d

Available characters 
0,1,2,3,4,5,6,7,8,9,A,b,C,c,d,E,F,H,h,L,n,I,O,o,P,S, (space)

VCC => Pin 4 (5V PWR)
GND => Pin 6 (GND)
DIO => Pin 11 (GPIO 17) Data
SCLK => Pin 13 (GPIO 27) Clock
RCLK => Pin 15 (GPIO 22) Latch

Run in separate process: sudo nohup python3 sevenseg.py &
'''

import Pi7SegPy as Pi7Seg
import time

data_pin = 17 
clock_pin = 27
latch_pin = 22
registers = 2 # 2 x 74HC595 shift registers
no_of_displays = 4 # 4 digits


Pi7Seg.init(data_pin,clock_pin,latch_pin,registers,no_of_displays) 

while True:
    for number in range(0, 9999):
        
        #convert number into an array of digits
        res = []
        num = number
        while num > 0:
            num, remainder = divmod(num, 10)
            res.insert(0,remainder)
        
        current_time = time.time() * 1000
        while time.time() * 1000 < current_time + 1000:
            # print(res)
            Pi7Seg.show(res.copy()) 
            # Show a copy of the array since this will alter the array
        

    # dots: for reasons unknown has to be 5-x where x is number of display
    