from gpiozero import LED, Button
from time import sleep
from signal import pause

led =LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
"""
while True: 
    button.wait_for_press()
    led.toggle()
    sleep(0.5)
"""
    