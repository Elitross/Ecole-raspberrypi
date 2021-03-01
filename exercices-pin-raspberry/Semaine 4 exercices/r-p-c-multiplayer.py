#!/bin/python3
from microbit import *
import time
import radio

radio.config(group=69)
radio.on()

choix = ''

while True:
  if accelerometer.was_gesture('shake'):
      display.clear()
      radio.send('p')
      choix = 'p'
  elif button_a.is_pressed():
      display.clear()
      radio.send('f')
      choix = 'f'
  
  elif button_b.is_pressed():
      display.clear()
      radio.send('c')
      choix = 'c'

  message = radio.receive()
  time.sleep(3)
    
  if(choix == message):
    display.clear()  
    display.show('TIRAGE AU SORT!')
  elif(choix == 'p'and message == 'c'):  
      display.clear()
      display.show('Le joueur gagne!')
  elif(choix == 'p'and message == 'f'): 
      display.clear() 
      display.show("L'ordinateur gagne!")
  elif(choix == 'f'and message == 'p'):  
      display.clear()
      display.show('Le joueur gagne!')
  elif(choix == 'f'and message == 'c'):  
      display.clear()
      display.show("L'ordinateur gagne!")
  elif(choix == 'c'and message == 'f'):  
      display.clear()
      display.show('Le joueur gagne!')
  elif(choix == 'c'and message == 'p'):  
      display.clear()
      display.show("L'ordinateur gagne!")