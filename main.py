# Add your Python code here. E.g.
import struct
from microbit import *

DELAY_BOOT = 2000

class Display:
    def __init__(self):
        pass

    def set_all(self, value):
        for x in range(0, 5):
            for y in range(0, 5):
                display.set_pixel(x, y, value)

    def clear(self):
        display.clear()

    def blink(self, times, delay_ms):
        for x in range (0, times):
            if x % 2 == 0:
                self.set_all(9)
                sleep(delay_ms)
            else:
                self.set_all(0)
                sleep(delay_ms)

        display.clear()

class Tmp112:
    def __init__(self):
        pass

    def read_celsius(self):
        i2c.write(72,b'\x01\x80')
        i2c.write(72,b'\x00')
        temp = i2c.read(72,2)
        tmp112=temp[0]+(temp[1]/100)
        return tmp112


display_microbit = Display()
tag_temperature = Tmp112()

print('APP: BOOT')
display_microbit.set_all(9)
sleep(DELAY_BOOT)
display_microbit.clear()

compare_with = tag_temperature.read_celsius()
print('APP: Start data {}'.format(compare_with))

while True:
    now = tag_temperature.read_celsius()
    print('APP: Actual - {} compare with {}'.format(now, compare_with))
    if (now / compare_with) > 1.2:
        print('APP: Oh! Temperature raised!')
        display_microbit.blink(10, 300)
        sleep(1000)

    sleep(100)