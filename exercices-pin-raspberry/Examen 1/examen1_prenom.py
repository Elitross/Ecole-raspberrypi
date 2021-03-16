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
    GPIO.output(15,GPIO,HIGH)
    sleep(durationBeep)
    GPIO.output(15,GPIO,LOW)

while True:
    button.wait_for_press()

    if compteur < 10 and compteur >= 8:
        compteur += 1

        if compteur == 10:
            
            for i in range(1-3): # Valeur à mettre
                beeeeeeeeeep(1) # Valeur à mettre
                sleep(0.5)

            GPIO.output(25,GPIO.LOW)
            compteur = 0
        else:
            GPIO.output(8,GPIO.LOW)
            GPIO.output(25,GPIO.HIGH)

    elif compteur < 8 and compteur >= 4:
        compteur += 1
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
    elif compteur < 4 and compteur >= 1:
        compteur += 1
        GPIO.output(7,GPIO.HIGH)
    else:
        compteur += 1

    print(compteur)
    button.wait_for_release()