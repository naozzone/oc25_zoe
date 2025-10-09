# Projet robotique

Option complémentaire en informatique du gymnase du Bugnon

## Description

Dans ce projet nous programmons le robot kitronik move

![Kitronikmove](images/robot.jpg)

![Kitronikmove](images/plan.jpg)

## Partie obligatoire
Dans ce mini projet le robot:

- Définition des constantes :
```
MAX_PROGRAMS = 2

SECURITY_DISTANCE = 20


SPEED_SLOW = 10

SPEED_NORMAL = 20

SPEED_TURN = 60

SPEED_BACKWARD = -60


prog = 0

display.show(prog)


- Initialisation du robot :
robot = KitronikMOVEMotor.MOVEMotor()

robot.move(0, 0)

robot.goToPosition(1, 160)
```

- Commence le parcours à une position A
- Temps entre la position A (début) et l'objet (même durée utilisé pour revenir à la position A) :
```
  init_time = running_time()
    
  robot.goToPosition(1, 160)
    
  
- Va suivre une ligne (définition d'une fonction) :
```
    ### Fonction pour suivre une ligne noire avec les capteurs
    left = pin1.read_analog()
    right = pin2.read_analog()

    # Calcul de la différence pour la correction
    difference = (left - right) // 10
    
    # Ajustement des vitesses des moteurs
    robot.move(speed - difference, speed + difference)
```
```
def program_suivre_ligne():
    ### Programme 0: Suivi de ligne simple
    while True:
        if button_a.was_pressed():
            robot.move(0, 0)
            return True  # Indique qu'il faut changer de programme

        suivre_ligne(SPEED_NORMAL) 
```
   
- Va déteter un objet avec le capteur ultrason (position 0 variable):
```
def mesure_distance():
    ### Mesure la distance avec le capteur ultrasonique
    trigger = pin13
    echo = pin14

    # Envoi d'une impulsion
    trigger.write_digital(1)
    trigger.write_digital(0)

    # Calcul de la distance en centimètres
    duration = time_pulse_us(echo, 1)
    distance_cm = (duration / 2e6)*340*100
    # d = time_pulse_us(echo, 1)/2e6*340*100 # *100 pour avoir en cm
    return distance_cm
```
- Va tourner de 180 degrée et attraper l'objet:
```
        distance = mesure_distance()

        if distance <= 20:
            # Récupération de l'objet
            robot.move(SPEED_TURN, -SPEED_TURN, 1300)  # Rotation 180°
            robot.move(SPEED_BACKWARD, SPEED_BACKWARD, 1000)  # Reculer
            robot.goToPosition(1, 20)  # Fermer la pince
```
- Va amener l'objet à la position A et le relâcher :
            
            time_elapsed = running_time() - init_time # Calculer le temps pour retourner au point de départ

            # Retour au point de départ
            while True:
                new_time = running_time() - time_elapsed - init_time

                if time_elapsed <= new_time:
                    robot.move(0, 0)
                    robot.goToPosition(1, 20)  # Relâcher l'objet

## Partie libre

Une partie complétement libre où le robot pourra faire:

- Une danse (définition d'une fonction) :
 ```
def danser():
    robot.move(120, 0, 1000) # tourne
    robot.goToPosition(1, 160) # ouvre pince 
    robot.goToPosition(1, 20) # ferme pince
    robot.move(0, 120, 1000) # tourne autre sens
 ```

- Un dessin
- Un light-show
- Parler
- Faire de la musique

### Programme final
    while True:
    # Navigation entre les programmes avec le bouton A
    if button_a.was_pressed():
        robot.move(0, 0)
        prog = (prog + 1) % MAX_PROGRAMS
        display.show(prog)

    # Exécution du programme sélectionné
    if prog == 0:
        # Programme 0: Suivi de ligne
        if program_suivre_ligne():
            prog = (prog + 1) % MAX_PROGRAMS
            display.show(prog)

    elif prog == 1:
        # Programme 1: Détection d'obstacles
        if program_obstacle_detection():
            prog = (prog + 1) % MAX_PROGRAMS
            display.show(prog)

### Programme total
```
from microbit import *
import KitronikMOVEMotor
from machine import time_pulse_us 
import time

#Définition des constantes
MAX_PROGRAMS = 2
SECURITY_DISTANCE = 20

#Vitesses des moteurs
SPEED_SLOW = 10
SPEED_NORMAL = 20
SPEED_TURN = 60
SPEED_BACKWARD = -60

#Initialisation du robot
robot = KitronikMOVEMotor.MOVEMotor()
robot.move(0, 0)
robot.goToPosition(1, 160)

#Variables globales
prog = 0
display.show(prog)

def suivre_ligne(speed):
    # Fonction pour suivre une ligne noire avec les capteurs
    left = pin1.read_analog()
    right = pin2.read_analog()

    # Calcul de la différence pour la correction
    difference = (left - right) // 10
    
    # Ajustement des vitesses des moteurs
    robot.move(speed - difference, speed + difference)

def mesure_distance():
    # Mesure la distance avec le capteur ultrasonique
    trigger = pin13
    echo = pin14

    # Envoi d'une impulsion
    trigger.write_digital(1)
    trigger.write_digital(0)

    # Calcul de la distance en centimètres
    duration = time_pulse_us(echo, 1)
    distance_cm = (duration / 2e6)*340*100
    # d = time_pulse_us(echo, 1)/2e6*340*100 # *100 pour avoir en cm
    return distance_cm

def program_suivre_ligne():
    # Programme 0: Suivi de ligne simple
    while True:
        if button_a.was_pressed():
            robot.move(0, 0)
            return True  # Indique qu'il faut changer de programme

        suivre_ligne(SPEED_NORMAL) 

def danser():
    robot.move(120, 0, 1000) # tourne
    robot.goToPosition(1, 160) # ouvre pince 
    robot.goToPosition(1, 20) # ferme pince
    robot.move(0, 120, 1000) # tourne autre sens


def program_obstacle_detection():
    # Programme 1: Détection d'obstacles et récupération d'objets
    init_time = running_time()
    robot.goToPosition(1, 160)

    while True:
        # Vérification si on doit changer de programme
        if button_a.was_pressed():
            robot.move(0, 0)
            return True  # Indique qu'il faut changer de programme

        # Mesure de distance
        distance = mesure_distance()

        if distance <= 20:
            # Récupération de l'objet
            robot.move(SPEED_TURN, -SPEED_TURN, 1300)  # Rotation 180°
            robot.move(SPEED_BACKWARD, SPEED_BACKWARD, 1000)  # Reculer
            robot.goToPosition(1, 20)  # Fermer la pince
            
            # Calculer le temps pour retourner au point de départ
            time_elapsed = running_time() - init_time

            # Retour au point de départ
            while True:
                new_time = running_time() - time_elapsed - init_time

                if time_elapsed <= new_time:
                    robot.move(0, 0)
                    robot.goToPosition(1, 20)  # Relâcher l'objet


 #Programme principal
while True:
    # Navigation entre les programmes avec le bouton A
    if button_a.was_pressed():
        robot.move(0, 0)
        prog = (prog + 1) % MAX_PROGRAMS
        display.show(prog)

    # Exécution du programme sélectionné
    if prog == 0:
        # Programme 0: Suivi de ligne
        if program_suivre_ligne():
            prog = (prog + 1) % MAX_PROGRAMS
            display.show(prog)

    elif prog == 1:
        # Programme 1: Détection d'obstacles
        if program_obstacle_detection():
            prog = (prog + 1) % MAX_PROGRAMS
            display.show(prog)
```            
## Documentation

Toute la documentation se trouvve dans ce ficher README.md

Vous devez utiliser:

- 3 niveaux de titres
- liste avec puces et numéroté
- des exemples de code
- des formules mathématiques
- des images
- des hyperliens
