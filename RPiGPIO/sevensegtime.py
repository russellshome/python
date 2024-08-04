#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   sevensegtime.py
@Time    :   2024/08/04 14:26:53
@Author  :   Russell Mercer
@Version :   1.0
@Contact :   russellshome@gurudigital.nz
@License :   (C)Copyright Russell Mercer
@Desc    :   Show current time on 7 seg display

Circuit  :   https://crcit.net/c/25ecfad5e0274f6aaebe2bac931ac13d

Available characters 
0,1,2,3,4,5,6,7,8,9,A,b,C,c,d,E,F,H,h,L,n,I,O,o,P,S, (space)

VCC => Pin 4 (5V PWR)
GND => Pin 6 (GND)
DIO => Pin 11 (GPIO 17) Data
SCLK => Pin 13 (GPIO 27) Clock
RCLK => Pin 15 (GPIO 22) Latch

Run in separate process: sudo nohup python3 sevensegtime.py &

'''
import Pi7SegPy as Pi7Seg
import time
import datetime

data_pin = 17 
clock_pin = 27
latch_pin = 22
registers = 2 # 2 x 74HC595 shift registers
no_of_displays = 4 # 4 digits


Pi7Seg.init(data_pin,clock_pin,latch_pin,registers,no_of_displays) 

while True:
    res = []
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    if hour > 12:
        hour -= 12
    elif hour == 0:
        hour = 12
    d1 = " "
    if (hour >= 10):
        d1 = 1
    num, d2 = divmod(hour, 10)
    res.append(d1)
    res.append(d2)
    d3, d4 = divmod(minute, 10)
    res.append(d3)
    res.append(d4)

    current_time = time.time() * 1000
    while time.time() * 1000 < current_time + 1000:
        Pi7Seg.show(res.copy()) 

