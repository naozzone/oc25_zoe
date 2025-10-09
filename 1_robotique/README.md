# Projet robotique

Option complémentaire en informatique du gymnase du Bugnon

## Description

Dans ce projet nous programmons le robot kitronik move

![Kitronikmove](images/robot.jpg)

![Kitronikmove](images/plan.jpg)

## Partie obligatoire
Dans ce mini projet le robot:

- Définition des constantes :
>MAX_PROGRAMS = 2
>
>SECURITY_DISTANCE = 20
>

>SPEED_SLOW = 10
>
>SPEED_NORMAL = 20
>
>SPEED_TURN = 60
>
>SPEED_BACKWARD = -60
>

>prog = 0
>
>display.show(prog)
>

- Initialisation du robot :
>robot = KitronikMOVEMotor.MOVEMotor()
>
>robot.move(0, 0)
>
>robot.goToPosition(1, 160)
>

- Commence le parcours à une position A
- Temps entre la position A (début) et l'objet (même durée utilisé pour revenir à la position A) :
    >init_time = running_time()
    >
    >robot.goToPosition(1, 160)
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
  >def mesure_distance():
  >
    >>trigger = pin13
  >  >
    >>echo =pin14
  >  >
    >>trigger.write_digital(1)
  >  >
    >>time.sleep_us(10)
  >  >
    >>trigger.write_digital(0)
  >  >
    >>duration = time_pulse_us(echo, 1)
    >>distance_cm = (duration/2e6)*340*100 # *100 pour avoir en cm
  >  >
    >>return distance_cm
  >  >
  
- Va tourner de 180 degrée et attraper l'objet:
  >robot.move(SPEED_TURN, -SPEED_TURN, 1300)  # Rotation 180°
  >
  >robot.move(SPEED_BACKWARD, SPEED_BACKWARD, 1000)  # Reculer
  >
  >robot.goToPosition(1, 20)  # Fermer la pince
  >
  
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
