import RPi.GPIO as GPIO
from gpiozero import Button, Buzzer, LED
from time import sleep

button = Button(21) # Valeur à mettre
lumiereRouge = LED(25) # Valeur à mettre
lumiereJaune = LED(8) # Valeur à mettre
lumiereVerte = LED(7) # Valeur à mettre
buzzer = Buzzer(15) # Valeur à mettre
compteur = 0

def beeeeeeeeeep(durationBeep):
    buzzer.on()
    sleep(durationBeep)
    buzzer.off()

while True:
    button.wait_for_press()

    if compteur < 10 and compteur >= 8:
        compteur += 1

        if compteur == 10:
            
            for i in range(3): # Valeur à mettre
                beeeeeeeeeep(1) # Valeur à mettre
                sleep(0.5)

            lumiereRouge.off()
            compteur = 0
        else:
            lumiereJaune.off()
            lumiereRouge.on()

    elif compteur < 8 and compteur >= 4:
        compteur += 1
        lumiereVerte.off()
        lumiereJaune.on()
    elif compteur < 4 and compteur >= 1:
        lumiereVerte.on()
        compteur += 1
        
    else:
        compteur += 1

    print(compteur)
    button.wait_for_release()