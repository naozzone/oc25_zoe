"""
Zoé Pellaton
21 aout 2025
introduction au micro:bit

code démonstration avec 10 programmes
bouton a : incrémenter le programme
bouton b : executer 

0 - afficher un coeur
1 - défiler 'Hello'
2 - afficher un smiley
3 - joue le son TWINKLE
4 - dire 'Hi'
5 - afficher 'Hi'
6 - joue de la musique 
7 - afficher un papillon
8 - afficher un dessin
9 - défiler 'Goodbye'

"""

# Imports go at the top
from microbit import *
import speech
import music

# on commence le programme 0
p = 0

# Code in a 'while True:' loop repeats forever
while True:
    # choix du rpogramme avec bouton a 
    display.show(p)
    if button_a.was_pressed():
        p = p + 1
        if p == 10:
            p = 0

    # le bouton b execute le programme actuel (0..9)
    if button_b.is_pressed():        
        if p == 0:
            display.show(Image.HEART_SMALL)
            sleep(1000)
        elif p == 1:
            display.scroll('One...')
        elif p == 2:
            display.show(Image.HAPPY)
            sleep(1000)
        elif p == 3:
            audio.play(Sound.TWINKLE)
        elif p == 4:
            speech.say('Hi')
        elif p== 5:
            display.scroll('Hi')
        elif p == 6:
            music.play(music.WAWAWAWAA)
        elif p == 7:
            display.show(Image.BUTTERFLY)
            sleep(1000)
        elif p == 8:
            display.show(Image('99099:'
                               '93939:'
                               '95359:'
                               '97379:'
                               '99999'))
            sleep (2000)
        elif p == 9:
            display.scroll('Goodbye', 50)