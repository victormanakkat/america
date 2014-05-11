#Character
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *

class Character():
    def __init__(self, surface):
        self.surface = surface
        self.manS = pygame.image.load('data\\images\\sprites\\0a.png')
        self.manN = pygame.image.load('data\\images\\sprites\\0b.png')
        self.manE = pygame.image.load('data\\images\\sprites\\0c.png')
        self.manW = pygame.transform.flip(self.manE, True, False)
        self.rect = self.manS.get_rect()
        
    def convert_coords(self, x, y):
        x = x * 32
        y = y * 32
        return x, y

    def move(self, dir):
        pass

    def blit(self, x, y, dir):
        x, y = self.convert_coords(x, y)
        self.rect.y = y
        self.rect.x = x
        if dir == 'S':
            self.surface.blit(self.manS, self.rect)
        if dir == 'N':
            self.surface.blit(self.manN, self.rect)
        if dir == 'E':
            self.surface.blit(self.manE, self.rect)
        if dir == 'W':
            self.surface.blit(self.manW, self.rect)
    
