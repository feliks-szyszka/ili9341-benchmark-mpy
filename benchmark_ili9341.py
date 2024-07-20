'''

Software Copyright Feliks Szyszka 2024.
Licenced under Creative Commons. (Attribution Non Commercial, Non Derivative)

'''

from machine import Pin, SPI, PWM
import ili9341
import time
import random

spi = SPI(1, baudrate=80000000, polarity=0, phase=0, sck=Pin(10), mosi=Pin(11), miso=Pin(8))

cs = Pin(14, Pin.OUT)
dc = Pin(13, Pin.OUT)
rst = Pin(12, Pin.OUT)
pwm = PWM(Pin(15))

pwm.freq(1000)
display = ili9341.ILI9341(spi, cs=cs, dc=dc, rst=rst, w=240, h=320, r=0)
display.set_color(ili9341.color565(255, 255, 255), ili9341.color565(0, 0, 0))
display.erase()
display.set_pos(40, 100)
display.write("ILI9341 SPI Benchmark")
time.sleep(2)
display.erase()
display.set_pos(60, 100)
display.write("By Feliks Szyszka")
time.sleep(2)
display.erase()
display.set_pos(150, 100)
display.write("3")
time.sleep(1)
display.erase()
display.set_pos(150, 100)
display.write("2")
time.sleep(1)
display.erase()
display.set_pos(150, 100)
display.write("1")
time.sleep(1)

start_time = time.time()

for i in range(400):
    display.fill_rectangle(random.randint(0, 300), random.randint(0, 240), random.randint(1, 100), random.randint(1, 100), random.randint(0, 10000000))

end_time = time.time()
elapsed_time = end_time - start_time

display.set_pos(30, 100)
display.write("Benchmark Time: " + str(round(elapsed_time, 1)) + " secs")

while True:
    pass
