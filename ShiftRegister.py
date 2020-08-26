"""
Description : Dirty simple ShiftRegister (74HC595) implementation with gpiozero
Author      : Thiago Hummel Moreira
Date        : Apr 16, 2019
"""
from collections import OrderedDict
from gpiozero import CompositeDevice, SourceMixin, GPIOPinMissing, OutputDevice
class ShiftRegister(SourceMixin, CompositeDevice):
    def __init__(self, data=None, latch=None, clock=None, initial_value=None, bit_count=8, pin_factory=None):
        if not all(p is not None for p in [data, latch, clock]):
            raise GPIOPinMissing('data, latch, and clock pins must be provided')
        devices = OrderedDict((
            ('data_device', OutputDevice(data, pin_factory=pin_factory)),
            ('latch_device', OutputDevice(latch, initial_value=True, pin_factory=pin_factory)),
            ('clock_device', OutputDevice(clock, pin_factory=pin_factory)),
        ))
        self._bit_count = bit_count
        super().__init__(_order=devices.keys(), **devices)

        if initial_value is None:
            initial_value = int('0' * self.bit_count, 2)
        self.value = initial_value

    @property
    def bit_count(self):
        return self._bit_count

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._shift_out(value)
        self._value = value

    def on(self, bit):
        self.value |= 1 << bit

    def off(self, bit):
        self.value &= ~(1 << bit)

    def toggle(self, bit):
        self.value ^= 1 << bit

    def _shift_out(self, value):
        self.latch_device.off()
        for x in range(self.bit_count):
            self.data_device.value = (value >> x) & 1
            self.clock_device.on()
            self.clock_device.off()
        self.latch_device.on()
        self.data_device.off()