# Projet robotique

Option complémentaire en informatique du gymnase du Bugnon

## Description

Dans ce projet nous programmons le robot kitronik move

![Kitronikmove](images/robot.jpg)

![Kitronikmove](images/plan.jpg)

## Partie obligatoire
Dans ce mini projet le robot:

- Définition des constantes :
  MAX_PROGRAMS = 2
SECURITY_DISTANCE = 20

SPEED_SLOW = 10
SPEED_NORMAL = 20
SPEED_TURN = 60
SPEED_BACKWARD = -60

- Commence le parcours à une position A
- Temps entre la position A (début) et l'objet (même durée utilisé pour revenir à la position A) :
    >t1 = time.ticks_ms()
    >
    >dt = t1 - t0 # durée jusqu'à l'objet
    >
    >t2 = time.ticks_ms()
    >
    >while time.ticks_diff(time.ticks_ms(), t2) < dt: # instant dans le futur ou il doit s'arreter
                suivre_ligne()  
    >
  
- Va suivre une ligne (définition d'une fonction) :
  >def suivre_ligne():
  >
    >>left = pin1.read_analog()
  >  >
    >>right = pin2.read_analog()
  >  >
    >>difference = (left - right)
  >  >
    >>difference = b // 10
  >  >
    >>robot.move(5 - b, 5 + b)
  >  >
  
- Va déteter un objet avec le capteur ultrason (position 0 variable):
  >def distance():
  >
    >>trigger.write_digital(1)
  >  >
    >>time.sleep_us(10)
  >  >
    >>trigger.write_digital(0)
  >  >
    >>duration = time_pulse_us(echo, 1)
    >>distance_cm = (duration/2e6)*340*100 # *100 pour avoir en cm
  >  >
    >>return round(d)
  >  >
  
- Va tourner de 180 degrée (définition d'une fonction) :
  >def tourner():
  >
    >>robot.move(70, -70, 1000)
  >  >
    >>robot.move(0, 0)
  >  >
    >>sleep(500)
  >  >
  
- Va attraper l'objet avec la pince :
  >robot.goToPosition(1, 20)
  >
  >sleep(1000)
  >
  
- Va amener l'objet à la position A

## Partie libre

Une partie complétement libre où le robot pourra faire:

- Une danse (définition d'une fonction) :
  >def danser():
  >
    >>robot.move(120, 0, 1000) # tourne
  >  >
    >>robot.goToPosition(1, 160) # ouvre pince
  >  >
    >>robot.goToPosition(1, 20) # ferme pince
  >  >
    >>robot.move(0, 120, 1000) # tourne autre sens
  >  >
  
- Un dessin
- Un light-show
- Parler
- Faire de la musique

### Programme final
    
## Documentation

Toute la documentation se trouvve dans ce ficher README.md

Vous devez utiliser:

- 3 niveaux de titres
- liste avec puces et numéroté
- des exemples de code
- des formules mathématiques
- des images
- des hyperliens
