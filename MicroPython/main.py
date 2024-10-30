"""
Created by: Mr. Coxall
Created on: Sep 2020
This module simulates a 6 sided dice
"""
#test
from microbit import *
import random

# our variable for a random number
random_number = 0

display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        random_number = random.randint(1, 6)
        display.show(str(random_number))
