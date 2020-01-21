from microbit import *
DELAY = 200

class Display:
    def __init__(self):
        pass

    def _set_all(self, value):
        for x in range(0, 5):
            for y in range(0, 5):
                display.set_pixel(x, y, value)

    def blink(self, times, delay_ms):
        state = True
        for _ in range (0, times):
            print('loop')
            if state == True:
                print('State on')
                self._set_all(9)
                state = False
                sleep(delay_ms)
            else:
                self._set_all(0)
                print('State off')
                state = True
                sleep(delay_ms)

        self._set_all(0)

while True:
    d = Display()
    d.blink(5, DELAY)
    sleep(DELAY)