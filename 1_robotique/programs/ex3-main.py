"""
Zoé Pellaton
26 aout 2025

led1 = rouge
led2 = vert 
led3 = bleu

"""


# Imports go at the top
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin8, 60)
np[1] = (63,0,0)
np[2] = (0,63,0)
np[3] = (0,0,63)
np.show()




