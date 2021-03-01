from microbit import *
import radio
radio.config(group=80)
radio.on()

while True:
    message = radio.receive()
    if message:
        display.show(message)
    if button_a.is_pressed():
        display.clear()
        radio.send('1+1=13')