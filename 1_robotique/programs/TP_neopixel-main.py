"""
TP Neopixel

Nom: Pellaton Zoé
Classe: 3M07
Date: 28 août 2025

Dans ce TP vous aller apprendre
- comment analyser et documenter un programme
- comment représenter des couleurs en format RGB
- comment programmer des LED avec le module neopixel
- comment utiliser modulo (%) pour limiter une plage
- comment utiliser les boutons et les sons
"""

from microbit import *
import neopixel
import music
import random

# définir toutes les valeurs RGB de chaques couleurs

red = (10, 0, 0)
green = (0, 10, 0)
blue = (0, 0, 10)

yellow = (10, 10, 0)
magenta = (10, 0, 10)
cyan = (0, 10, 10)
orange = (10, 5, 0)

black = (0, 0, 0)
gray = (5, 5, 5)
white = (10, 10, 10)

colors = (red, orange, yellow, green, cyan, blue, magenta)
color = red #définit la couleur de base en rouge

np = neopixel.NeoPixel(pin8, 60)

# définir les indices de programme [prog] ainsi que ceux des LEDs [i] et des couleurs [j]

prog = 0 # programme actuel (0..9)
i = 0    # indice de LED (0..59)
j = 0    # indice de couleur (0..6)

compass_on = False
display.show(prog) #lance le programme

while True:
    if button_a.was_pressed():
        prog = (prog + 1) % 10
        display.show(prog)
        np.clear()
        music.pitch(440, 20)

    if pin_logo.is_touched():   # Quand on touche le logo la couleur change
        j = (j + 1) % len(colors)
        music.pitch(540, 20)
        sleep(100)

    if i == 0:     # à chaque retour à 0, il un bip qui se lance 
        np.clear()
        music.pitch(880, 10)

    if prog == 0:
        np[i] = colors[j]
        np.show()
        sleep(20)
        i = (i + 1) % 60
    
    if prog == 1:
        np.clear()
        np[i] = colors[j]
        np.show()
        sleep(20)
        i = (i + 1) % 60

    if prog == 2:
        j = i % len(colors)
        np[i] = colors[j]
        i = (i + 1) % 60
        sleep(50)
        np.show()

    if prog == 3:
        if button_b.is_pressed():
            i = i - 1
        else:
            i = i + 1
        i = i % 30
        np.clear()
        np[i] = colors[j]
        np.show()
        sleep(20)
        
    if prog == 4:
        if button_b.is_pressed():
            i = (i + 1) % 59
            np[i] = colors[j]
            np.show()
            sleep(20)

    if prog == 5:
        np[i] = (i, 0, i)
        i = (i + 1) % 30
        np.show()
        sleep(20)
     
    if prog == 6:
        i = (i+1) % 20
        np[i] = (20-i, i, 0)
        np[i+20] = (0, 20-i, i)
        np[i+40] = (i, 0, 20-i)
        sleep(50)
        np.show()

    if prog == 7:
        np.clear()
        i = random.randint(0, 59)
        np[i] = [10*i for i in colors[j]]
        np.show()
        sleep (50)

    if prog == 8:
        t = running_time()
        i = (t % 1000) // 17
        i2 = (t//1000) % 60
        np.clear()
        np[i] = red
        np[i2] = green
        np.show()

    if prog == 9:
        if button_b.is_pressed():
            compass_on = True
        if compass_on:
            i = 59 - compass.heading() // 6
            np.clear()
            np[i] = red
            np[(i+30)%60] = blue
            np.show()
            sleep(20)