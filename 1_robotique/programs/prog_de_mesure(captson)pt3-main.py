# Imports go at the top
from microbit import *
from machine import time_pulse_us
import KitronikMOVEMotor 
import music
import radio
#import neopixel
#import random
import time 

trigger = pin13
echo = pin14

trigger.write_digital(0)
echo.read_digital()

robot = KitronikMOVEMotor.MOVEMotor()
robot.move(0, 0)
robot.goToPosition(1, 90)

# le group doit correspondre au kit (1..15)
g = 9
display.scroll(g)
radio.on()
radio.config(group=g)

prog = 0 # programme actuel (0..9)
display.show(prog)


while True:

    trigger.write_digital(1)
    trigger.write_digital(0)
    distance = time_pulse_us(echo, 1)/2e6*340*100 # *100 pour avoir en cm
    #print(distance)
    display.scroll(str(round(distance)))

    robot.goToPosition(1, 160) # pince ouverte (pour la refermer après pour attraper objet)
    
    # le bouton A incrémente les programmes (0..9)
    if button_a.was_pressed():
        robot.move(0, 0)
        prog = (prog + 1) % 10
        display.show(prog)
        music.pitch(440, 20)

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






# Programme autonome : aller à un objet, le ramasser, et revenir à A (sur circuit fermé)
    
    if prog == 1:
        msg = radio.receive()
        if msg:
            display.show(msg)
            if msg == 'u' :
                robot.goToPosition(1, 160)  # pince ouverte
                sleep(500)

                # Suivre la ligne jusqu'à détecter un objet pendant un temps T
            
                t0 = time.ticks_ms()  # le temps commence quand le robot commence à avancer 
                left = pin1.read_analog()
                right = pin2.read_analog()
                d = (left - right) 
                d= d // 10
                robot.move( 5 - d, 5 + d)
        
                # Capteur ultrason : détection objet
                
                if distance < 20:
                    robot.move(0, 0)
                    sleep(500)
        
                    # Demi-tour
                    robot.move(80, -80, 2000)
                    robot.move(0, 0)
                    sleep(500)
        
                    # Fermer la pince
                    robot.goToPosition(1, 20)
                    sleep(1000)
            
                    # Revenir à la position A en refaisant le même temps 
                
                    t1 = time.ticks_ms()  # Temps jusqu'à l'objet pour déterminer le temps entre point A et objet.
                    left = pin1.read_analog()
                    right = pin2.read_analog()  
                    d = (left - right) 
                    d = d // 10 
                    robot.move(40 - d, 40 + d)
                
            
                    robot.move(0, 0)
                    sleep(500)
            
                    # Déposer l'objet
                    robot.goToPosition(1, 160)
                    sleep(1000)
        
                    # libre (petite dance) il tourne sur lui même en fermant et ouvrant sa pince
                    for i in range (2): 
                        robot.move(120,0,1000) # tourne
                        robot.goToPosition(1,160)
                