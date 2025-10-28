###
### Gymnase du Bugnon
### Author: Zoé et Emmma
### Date: 08.10.25
### Version: 9
###
### Programme d'utilisation du robot Kitronik MOVE avec capteur ultrason et suivi de ligne
###

from microbit import *
import KitronikMOVEMotor
from machine import time_pulse_us 
import time

# Définition des constantes
MAX_PROGRAMS = 2
OPEN_PLIERS = 160
CLOSE_PLIERS = 20
SECURITY_DISTANCE = 20
SOUND_SPEED_MS = 340

# Vitesses des moteurs
SPEED_SLOW = 10
SPEED_NORMAL = 20
SPEED_TURN = 60
SPEED_BACKWARD = -60

# Temps de rotation (en millisecondes)
TURN_180_TIME = 1300
BACKWARD_TIME = 1000

# Initialisation du robot
robot = KitronikMOVEMotor.MOVEMotor()
robot.move(0, 0)
robot.goToPosition(1, OPEN_PLIERS)

# Variables globales
prog = 0
display.show(prog)

def follow_line(speed):
    ### Fonction pour suivre une ligne noire avec les capteurs
    left_sensor = pin1.read_analog()
    right_sensor = pin2.read_analog()

    # Calcul de la différence pour la correction
    difference = (left_sensor - right_sensor) // 10

    # Ajustement des vitesses des moteurs
    robot.move(speed - difference, speed + difference)

def measure_distance():
    ### Mesure la distance avec le capteur ultrasonique
    trigger = pin13
    echo = pin14

    # Envoi d'une impulsion
    trigger.write_digital(1)
    trigger.write_digital(0)

    # Calcul de la distance en centimètres
    duration = time_pulse_us(echo, 1)
    distance_cm = (duration / 2e6) * SOUND_SPEED_MS * 100

    return distance_cm

def program_line_following():
    ### Programme 0: Suivi de ligne simple
    while True:
        if button_a.was_pressed():
            robot.move(0, 0)
            return True  # Indique qu'il faut changer de programme

        follow_line(SPEED_NORMAL)

def program_obstacle_detection():
    ### Programme 1: Détection d'obstacles et récupération d'objets
    init_time = running_time()
    robot.goToPosition(1, OPEN_PLIERS)

    while True:
        # Vérification si on doit changer de programme
        if button_a.was_pressed():
            robot.move(0, 0)
            return True  # Indique qu'il faut changer de programme

        # Mesure de distance
        distance = measure_distance()

        if distance <= SECURITY_DISTANCE:
            # Récupération de l'objet
            robot.move(SPEED_TURN, -SPEED_TURN, TURN_180_TIME)  # Rotation 180°
            robot.move(SPEED_BACKWARD, SPEED_BACKWARD, BACKWARD_TIME)  # Reculer
            robot.goToPosition(1, CLOSE_PLIERS)  # Fermer la pince
            
            # Calculer le temps pour retourner au point de départ
            time_elapsed = running_time() - init_time

            # Retour au point de départ
            while True:
                new_time = running_time() - time_elapsed - init_time

                if time_elapsed <= new_time:
                    robot.move(0, 0)
                    robot.goToPosition(1, OPEN_PLIERS)  # Relâcher l'objet

                    while True:
                        if button_a.was_pressed():
                            return True  # Changer de programme
                    break
                else:
                    follow_line(SPEED_SLOW)
        else:
            follow_line(SPEED_NORMAL)

# Programme principal
while True:
    # Navigation entre les programmes avec le bouton A
    if button_a.was_pressed():
        robot.move(0, 0)
        prog = (prog + 1) % MAX_PROGRAMS
        display.show(prog)

    # Exécution du programme sélectionné
    if prog == 0:
        # Programme 0: Suivi de ligne
        if program_line_following():
            prog = (prog + 1) % MAX_PROGRAMS
            display.show(prog)

    elif prog == 1:
        # Programme 1: Détection d'obstacles
        if program_obstacle_detection():
            prog = (prog + 1) % MAX_PROGRAMS
            display.show(prog)