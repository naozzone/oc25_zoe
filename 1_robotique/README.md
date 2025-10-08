# Projet robotique

Option complémentaire en informatique du gymnase du Bugnon

## Description

Dans ce projet nous programmons le robot kitronik move

![Kitronikmove](images/robot.jpg)

![Kitronikmove](images/plan.jpg)

## Partie obligatoire
Dans ce mini projet le robot:

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
    >>b = (left - right)
  >  >
    >>b = b // 10
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
    >>d = time_pulse_us(echo, 1)/2e6*340*100 # *100 pour avoir en cm
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

## Programme final
    if prog == 1: 
        if button_b.is_pressed():
        # 1. Ouvrir la pince et démarrer le chronomètre
            robot.goToPosition(1, 160)
            sleep(300)
            t0 = time.ticks_ms()

        # 2. Suivre la ligne jusqu'à détecter un objet
            while distance() > 15:
                suivre_ligne()
            
        # 3. Arrêt + mesure du temps aller
            robot.move(0, 0)
            t1 = time.ticks_ms()
            dt = t1 - t0

        # 4. Demi-tour et fermeture de la pince
            tourner()
            robot.goToPosition(1, 20)
            sleep(500)

        # 5. Suivre la ligne pendant exactement le même temps qu'à l'aller
            t2 = time.ticks_ms()
            while time.ticks_diff(time.ticks_ms(), t2) < dt:
                suivre_ligne()

        # 6. Arrêter, déposer l'objet, danser
            robot.move(0, 0)
            robot.goToPosition(1, 160)
            sleep(500)
            danser()
            display.show(Image.HAPPY)
            sleep(500)

## Documentation

Toute la documentation se trouvve dans ce ficher README.md

Vous devez utiliser:

- 3 niveaux de titres
- liste avec puces et numéroté
- des exemples de code
- des formules mathématiques
- des images
- des hyperliens
