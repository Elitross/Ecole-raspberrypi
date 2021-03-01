from gpiozero import Button
from time import sleep

button = Button(21)

while True:
    if button.is_pressed:
        print("Hello")
        sleep(1)
    else:
        print("goodbye")
        sleep(1)