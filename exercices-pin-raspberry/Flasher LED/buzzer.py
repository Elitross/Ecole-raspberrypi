from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(15)

while True:
    """
    buzzer.beep()
    sleep(1)
    """
    buzzer.off