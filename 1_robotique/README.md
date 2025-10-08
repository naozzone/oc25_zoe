# Projet robotique

Option complémentaire en informatique du gymnase du Bugnon

## Description

Dans ce projet nous programmons le robot kitronik move

![Kitronikmove](images/robot.jpg)

## Partie obligatoire

Dans ce mini projet le robot:

- Commence le parcours à une position A
- Temps entre la position A (début) et l'objet (même durée utilisé pour revenir à la position A) :
    >t1 = time.ticks_ms()
    >dt = t1 - t0 # durée jusqu'à l'objet
    >t2 = time.ticks_ms() + dt   # instant dans le futur ou il doit s'arreter
  
- Va suivre une ligne :
  def suivre_ligne():
    left = pin1.read_analog()
    right = pin2.read_analog()
    d = (left - right)
    d = d // 10
    robot.move(5 - d, 5 + d)
  
- Va déteter un objet avec le capteur ultrason (position 0 variable):
  def distance():
    trigger.write_digital(1)
    time.sleep_us(10)
    trigger.write_digital(0)
    d = time_pulse_us(echo, 1)/2e6*340*100 # *100 pour avoir en cm
    return round(d)
  
- Va tourner de 180 degrée :
  def tourner():
    robot.move(70, -70, 1000)
    robot.move(0, 0)
    sleep(500)
  
- Va attraper l'objet avec la pince :
              # Fermer la pince
            robot.goToPosition(1, 20)
            sleep(1000)
  
- Va amener l'objet à la position A

## Partie libre

Une partie complétement libre où le robot pourra faire:

- Une danse :
  def danser():
    robot.move(120, 0, 1000) # tourne
    robot.goToPosition(1, 160) # ouvre pince 
    robot.goToPosition(1, 20) # ferme pince
    robot.move(0, 120, 1000) # tourne autre sens
  
- Un dessin
- Un light-show
- Parler
- Faire de la musique

    ...

## Documentation

Toute la documentation se trouvve dans ce ficher README.md

Vous devez utiliser:

- 3 niveaux de titres
- liste avec puces et numéroté
- des exemples de code
- des formules mathématiques
- des images
- des hyperliens
