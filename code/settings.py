#Settings Menu
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *

class Settings():
    def __init__(self, screen):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.screen = screen
        self.open = False

        #Setup settings button
        self.settingsBlock = {'rect':pygame.Rect(0, 583, 25, 25),'color':self.BLACK}
        self.gearImage = pygame.image.load('data\\images\\menus\\gear.png')
        self.gearRect = self.gearImage.get_rect()
        self.gearRect.y = 586
        self.gearRect.x = 2

        #Setup exit button
        self.exitBlock = {'rect':pygame.Rect(0, 583, 25, 25),'color':self.BLACK}
        self.exitImage = pygame.image.load('data\\images\\menus\\exit.png')
        self.exitRect = self.exitImage.get_rect()
        self.exitRect.y = 586
        self.exitRect.x = 2

        #Setup sound button
        self.soundBlock = {'rect':pygame.Rect(-25, 583, 25, 25),'color':self.BLACK}
        self.soundImage = pygame.image.load('data\\images\\menus\\sound.png')
        self.soundRect = self.soundImage.get_rect()
        self.soundRect.y = 586
        self.soundRect.x = -23
        

    def settings_button(self, event=None):
        self.open_bar(self.open) 
        pygame.draw.rect(self.screen, self.settingsBlock['color'], self.settingsBlock['rect'])
        self.screen.blit(self.gearImage, self.gearRect)
        
        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] < 50 and event.pos[1] > 583:
                    self.settingsBlock['color'] = self.RED
                    self.open = True
                else:
                    self.settingsBlock['color'] = self.BLACK
                    self.open = False

    def open_bar(self, open):
        if open:
            #Blit exit stuff
            pygame.draw.rect(self.screen, self.exitBlock['color'], self.exitBlock['rect'])
            self.screen.blit(self.exitImage, self.exitRect)
            #Blit sound stuff
            pygame.draw.rect(self.screen, self.soundBlock['color'], self.soundBlock['rect'])
            self.screen.blit(self.soundImage, self.soundRect)
            
            #Move blocks if needed
            if self.soundBlock['rect'][0] != 25:
                self.soundBlock['rect'][0] += 1
                self.soundRect.x += 1
            if self.exitBlock['rect'][0] != 50:
                self.exitBlock['rect'][0] += 1
                self.exitRect.x += 1
        else:
            #Blit exit stuff
            pygame.draw.rect(self.screen, self.exitBlock['color'], self.exitBlock['rect'])
            self.screen.blit(self.exitImage, self.exitRect)
            #Blit sound stuff
            pygame.draw.rect(self.screen, self.soundBlock['color'], self.soundBlock['rect'])
            self.screen.blit(self.soundImage, self.soundRect)

            #Move blocks back
            if self.soundBlock['rect'][0] != -25:
                self.soundBlock['rect'][0] -= 1
                self.soundRect.x -= 1
            if self.exitBlock['rect'][0] != 0:
                self.exitBlock['rect'][0] -= 1
                self.exitRect.x -= 1
            
        

    def sound_button(self):
        pass

    def exit_button(self):
        pass

    def pause_button(self):
        pass

    def balloon(self):
        pass

    def add_bar(self):
        pass