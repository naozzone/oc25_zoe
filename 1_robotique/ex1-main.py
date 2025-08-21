# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.GHOST)
    sleep(1000)
    display.scroll('Boo', 50)
