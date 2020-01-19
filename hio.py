from microbit import *

def tmp112_read():
    raw_data = i2c.read(72, 2, repeat=False)
    return (raw_data[0] * 256 + raw_data[1]) / 16

def tmp112_init():
    i2c.write(72,b'\x01', b'\x60A0')
    return True