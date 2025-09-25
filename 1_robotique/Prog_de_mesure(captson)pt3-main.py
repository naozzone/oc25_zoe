# Imports go at the top
from microbit import *
from machine import time_pulse_us
import KitronikMOVEMotor 
#import music
#import radio
#import time
#import neopixel
#import random

trigger = pin13
echo = pin14

trigger.write_digital(0)
echo.read_digital()

robot = KitronikMOVEMotor.MOVEMotor()
robot.move(0, 0)
robot.goToPosition(1, 90)

def avancer(d):
    # avancer ou reculer de d centimètres
    d0 = 10.3 # distance de calibration
    if d>0:
        robot.move(120, 120, 20)
        robot.move(60, 60, d/d0*1000)
    else:
        robot.move(-120, -120, 20)
        robot.move(-60, -60, -d/d0*1000)

while True:
    trigger.write_digital(1)
    trigger.write_digital(0)
    distance = time_pulse_us(echo, 1)/2e6*340*100 # *100 pour avoir en cm
    #print(distance)
    display.scroll(str(round(distance)))
    
# Programme autonome : aller à un objet, le ramasser, et revenir à A (sur circuit fermé)
    robot.goToPosition(1, 160) # pince ouverte (pour la refermer après pour attraper objet)
    sleep(500)

    # Suivre la ligne jusqu'à détecter un objet pendant un temps t
    #t0 = time.ticks_ms() # Temps jusqu'à l'objet pour déterminer position A
    left = pin1.read_analog()
    right = pin2.read_analog()
    d = (left - right)
    d = d // 10
    robot.move(5 - d, 5 + d)
            
    # Capteur ultrason : détection objet   
    if distance < 20: # Si à moins de 20 cm (obstacle/objet) alors...
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
        #t1 = time.ticks_ms() # Faire même temps au retour qu'à l'aller
        left = pin1.read_analog()
        right = pin2.read_analog()
        d = (left - right)
        d = d // 20
        robot.move(5 - d, 5 + d)
                
        robot.move(0, 0)
        sleep(500)
                
        # Déposer l'objet
        robot.goToPosition(1, 160)
        sleep(1000)
                
        # Libre
        for i in range(2): # petite dance
            robot.move(120, 0, 1000) # tourne
            robot.goToPosition(1, 160) # ouvre pince 
            robot.goToPosition(1, 20) # ferme pince
            robot.move(0, 120, 1000) # tourne autre sens
                