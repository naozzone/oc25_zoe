from microbit import *
from machine import time_pulse_us
import KitronikMOVEMotor 
#import music
import radio
#import neopixel 
#import random

trigger = pin13
echo = pin14

trigger.write_digital (0)
echo.read_digital()

robot = KitronikMOVEMotor.MOVEMotor ()
robot.move(0, 0)

prog = 0 # programme actuel (0..9)
display.show(prog)



    
while True :
    trigger.write_digital(1)
    trigger.write_digital(0)
    distance = time_pulse_us(echo, 1) /2e6*340*100  # pour avoir en cm = *100
    display.scroll(str(round(distance)))

     # faire bouger le robot avec les 4 touches de direction
    # L/R pour pivoter, U/D pour avancer et reculer
    # F1: ouvrir la pince, F2: fermer la pince
    if prog == 0:
        msg = radio.receive()
        if msg:
            display.show(msg)
            if msg == '0':
                robot.move(0, 0)
            elif msg == 'u':
                robot.move(-80, -80)
            elif msg == 'r':
                robot.move(80, -80)
            elif msg == 'l':
                robot.move(-80, 80)
            elif msg == 'd':
                robot.move(80, 80)
            elif msg == '2':
                robot.goToPosition(1, 20)
            elif msg == '1':
                robot.goToPosition(1, 160)

    
# 1. commence le parcours à la position A

# 2. suivre une ligne 
    
    if prog ==2 :  
        left = pin1.read_analog()
        right = pin2.read_analog()
        d = (left - right)
        d = d // 10
        robot.move(10 - d, 10 + d)

# 3. détecter un objet
# code du détecter le bord de la table 

if prog == 3 :    
    left = pin1.read_analog()
    right = pin2.read_analog()
    if left < 100 or right < 100:
        robot.move(0, 0)

# 4. tourner 180 degré

