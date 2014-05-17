#Main
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *
from map import Map
from character import Character
from keyboard import Keyboard
from settings import Settings
from conversation import *
from mainmenu import MainMenu
from level import *
from timeline import *

pygame.init()

#Setup screen, clock, and colors
WINDOWWIDTH = 800
WINDOWHIEGHT = 608
os.environ ['SDL_VIDEO_WINDOW_POS'] = 'center'
surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('America: Learn American History')
mainClock = pygame.time.Clock()

SKY_BLUE = (0, 255, 255)
WHITE = (255, 255, 255)

surface.fill(WHITE)

sound = True

def main():
    while True:
        #Setup objects
        mainMenu = MainMenu(surface)
        game = Levels(surface)
        timeline = Timeline(surface, mainClock)

        #Load music and play it if sound is on
        pygame.mixer.music.load('data\\sound\\Godbless.mid')
        if sound:
            pygame.mixer.music.play(-1, 0.0)

        #Display main menu
        mainMenu.menu(mainClock)
        #Select level
        timeline.timeline()
        #Run level 1620
        game.Y1620(mainClock)

if __name__ == '__main__':
    main()
    
