#Main Menu
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *

class MainMenu():
    def __init__(self, surface):
        self.screen = surface
        self.SKY_BLUE = (0, 255, 255)
        self.startButton = pygame.image.load('data\\images\\menus\\start.png')
        self.startButtonClicked = pygame.image.load('data\\images\\menus\\startClicked.png')
        self.logo = pygame.image.load('data\\images\\menus\\logo.png')
        self.logoRect = self.logo.get_rect()
        self.logoRect.centerx = 400
        self.logoRect.centery = 150
        self.rect = self.startButton.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 300
        self.hover = False

    def start_button(self, event, start):
        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] > 250 and event.pos[0] < 550 and event.pos[1] > 250 and event.pos[1] < 350:
                    self.hover = True
                else:
                    self.hover = False
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] > 250 and event.pos[0] < 550 and event.pos[1] > 250 and event.pos[1] < 350:
                    start = True

        if self.hover:
            self.screen.blit(self.startButtonClicked, self.rect)
        else:
            self.screen.blit(self.startButton, self.rect)
        return start
    
    def blit(self, start, event=None):
        self.screen.fill(self.SKY_BLUE)
        self.screen.blit(self.logo, self.logoRect)
        start = self.start_button(event, start)
        return start
