#keyboard: All interactions with the keyboard
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *

class Keyboard():
    def player_input(self, event, go, direction):
        if event.key == 273:
            if go == False:
                go = True
                direction = 'N'
        if event.key == 274:
            if go == False:
                go = True
                direction = 'S'
        if event.key == 275:
            if go == False:
                go = True
                direction = 'W'
        if event.key == 276:
            if go == False:
                go = True
                direction = 'E'
        return go, direction
        
