#Buildings
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *
from constants import *
pygame.init()

class Mayflower():
    def __init__(self, screen):
        self.screen = screen
        self.mayflower = pygame.image.load('data\\images\\buildings\\mayflower.png')
        self.mayflower_rect = self.mayflower.get_rect()

        self.mayflower_rect.centerx = WINDOW_WIDTH / 2
        self.mayflower_rect.centery = WINDOW_HEIGHT / 2 - 232

    def blit(self):
        self.screen.blit(self.mayflower, self.mayflower_rect)
