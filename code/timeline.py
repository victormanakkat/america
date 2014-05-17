#Timeline menu
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *

class Timeline():
    def __init__(self, screen, clock):
        self.screen  = screen
        self.clock = clock
        self.logo = pygame.image.load('data\\images\\menus\\logo.png')
        self.logoRect = self.logo.get_rect()
        self.logoRect.centerx = 400
        self.logoRect.centery = 100
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        
        self.font = pygame.font.Font('data\\fonts\\font1.ttf', 24)
        self.mess = self.font.render('YOUR PROGRESS', True, self.WHITE, self.BLACK)
        self.messRect = self.mess.get_rect()
        self.messRect.centerx = 400
        self.messRect.centery = 200
        self.hover = False
        self.start = False

        #Load timeline picture
        self.line = pygame.image.load('data\\images\\menus\\timeline.png')
        self.lineRect = self.line.get_rect()
        self.lineRect.centerx = 400
        self.lineRect.centery = 300

        #Create ballon image and text
        self.ballon = pygame.image.load('data\\images\\menus\\ballon.png')
        self.ballonRect = self.ballon.get_rect()
        self.ballonRect.x = 40
        self.ballonRect.y = 230
        self.font2 = pygame.font.Font('data\\fonts\\font1.ttf', 12)
        self.year = self.font2.render('1620', True, self.BLACK, self.WHITE)
        self.yearRect = self.year.get_rect()
        self.yearRect.x = 52
        self.yearRect.centery = 244


        self.continueButton = pygame.image.load('data\\images\\menus\\continue.png')
        self.continueButtonClicked = pygame.image.load('data\\images\\menus\\continueClicked.png')
        self.rect = self.continueButton.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 400
        
    def timeline(self):
        while True:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.logo, self.logoRect)
            self.screen.blit(self.mess, self.messRect)
            self.screen.blit(self.line, self.lineRect)
            self.screen.blit(self.ballon, self.ballonRect)
            self.screen.blit(self.year, self.yearRect)
            self.continue_button(None, self.start)
            for event in pygame.event.get():
                self.start = self.continue_button(event, self.start)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick()

            if self.start:
                break

    def continue_button(self, event, start):
        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] > 250 and event.pos[0] < 550 and event.pos[1] > 350 and event.pos[1] < 450:
                    self.hover = True
                else:
                    self.hover = False
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] > 250 and event.pos[0] < 550 and event.pos[1] > 350 and event.pos[1] < 450:
                    start = True

        if self.hover:
            self.screen.blit(self.continueButtonClicked, self.rect)
        else:
            self.screen.blit(self.continueButton, self.rect)
        return start
