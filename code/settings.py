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

        self.exit = False
        self.sound = True
        self.pause = False
        self.help = False
        
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
        self.soundBlock = {'rect':pygame.Rect(-23, 583, 25, 25),'color':self.BLACK}
        self.soundImage = pygame.image.load('data\\images\\menus\\sound.png')
        self.soundRect = self.soundImage.get_rect()
        self.soundRect.y = 586
        self.soundRect.x = -21

        #Setup pause button
        self.pauseBlock = {'rect':pygame.Rect(-25, 583, 25, 25),'color':self.BLACK}
        self.pauseImage = pygame.image.load('data\\images\\menus\\pause.png')
        self.pauseRect = self.pauseImage.get_rect()
        self.pauseRect.y = 586
        self.pauseRect.x = -23

        #Setup help button
        self.helpBlock = {'rect':pygame.Rect(-25, 583, 25, 25),'color':self.BLACK}
        self.helpImage = pygame.image.load('data\\images\\menus\\help.png')
        self.helpRect = self.helpImage.get_rect()
        self.helpRect.y = 586
        self.helpRect.x = -23
        

    def settings_button(self, event=None):
        self.open_bar(self.open) 
        pygame.draw.rect(self.screen, self.settingsBlock['color'], self.settingsBlock['rect'])
        self.screen.blit(self.gearImage, self.gearRect)
        
        if event != None:
            self.exit_button(event)
            self.sound_button(event)
            self.pause_button(event)
            self.help_button(event)
            if event.type == MOUSEMOTION:
                if event.pos[0] < 25 and event.pos[1] > 583:
                    self.settingsBlock['color'] = self.RED
                    self.open = True
                else:
                    self.settingsBlock['color'] = self.BLACK
                    if event.pos[0] > 125 or event.pos[1] < 583:
                        self.open = False
        return self.exit, self.sound, self.pause, self.help
    
    def open_bar(self, open):
        if open:
            #Blit exit stuff
            pygame.draw.rect(self.screen, self.exitBlock['color'], self.exitBlock['rect'])
            self.screen.blit(self.exitImage, self.exitRect)
            #Blit sound stuff
            pygame.draw.rect(self.screen, self.soundBlock['color'], self.soundBlock['rect'])
            self.screen.blit(self.soundImage, self.soundRect)
            #Blit pause stuff
            pygame.draw.rect(self.screen, self.pauseBlock['color'], self.pauseBlock['rect'])
            self.screen.blit(self.pauseImage, self.pauseRect)
            #Blit help stuff
            pygame.draw.rect(self.screen, self.helpBlock['color'], self.helpBlock['rect'])
            self.screen.blit(self.helpImage, self.helpRect)
                       
            #Move blocks if needed
            if self.soundBlock['rect'][0] != 75:
                self.soundBlock['rect'][0] += 1
                self.soundRect.x += 1
            if self.exitBlock['rect'][0] != 100:
                self.exitBlock['rect'][0] += 1
                self.exitRect.x += 1
            if self.pauseBlock['rect'][0] != 50:
                self.pauseBlock['rect'][0] += 1
                self.pauseRect.x += 1
            if self.helpBlock['rect'][0] != 25:
                self.helpBlock['rect'][0] += 1
                self.helpRect.x += 1
                
        else:
            #Blit exit stuff
            pygame.draw.rect(self.screen, self.exitBlock['color'], self.exitBlock['rect'])
            self.screen.blit(self.exitImage, self.exitRect)
            #Blit sound stuff
            pygame.draw.rect(self.screen, self.soundBlock['color'], self.soundBlock['rect'])
            self.screen.blit(self.soundImage, self.soundRect)
            #Blit pause stuff
            pygame.draw.rect(self.screen, self.pauseBlock['color'], self.pauseBlock['rect'])
            self.screen.blit(self.pauseImage, self.pauseRect)
            #Blit help stuff
            pygame.draw.rect(self.screen, self.helpBlock['color'], self.helpBlock['rect'])
            self.screen.blit(self.helpImage, self.helpRect)

            #Move blocks back
            if self.soundBlock['rect'][0] != -25:
                self.soundBlock['rect'][0] -= 1
                self.soundRect.x -= 1
            if self.exitBlock['rect'][0] != 0:
                self.exitBlock['rect'][0] -= 1
                self.exitRect.x -= 1
            if self.pauseBlock['rect'][0] != -50:
                self.pauseBlock['rect'][0] -= 1
                self.pauseRect.x -= 1
            if self.helpBlock['rect'][0] != -75:
                self.helpBlock['rect'][0] -= 1
                self.helpRect.x -= 1        

    def sound_button(self, event):
        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] < 100 and event.pos[0] > 75 and event.pos[1] > 583:
                    self.soundBlock['color'] = self.RED
                else:
                    self.soundBlock['color'] = self.BLACK
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] < 100 and event.pos[0] > 75 and event.pos[1] > 583:
                    if self.sound:
                        self.sound = False
                    else:
                        self.sound = True
                else:
                    self.soundBlock['color'] = self.BLACK

    def exit_button(self, event):
        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] < 125 and event.pos[0] > 100 and event.pos[1] > 583:
                    self.exitBlock['color'] = self.RED
                else:
                    self.exitBlock['color'] = self.BLACK
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] < 125 and event.pos[0] > 100 and event.pos[1] > 583:
                    self.exit = True
                else:
                    self.exitBlock['color'] = self.BLACK

    def pause_button(self, event):
        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] < 75 and event.pos[0] > 50 and event.pos[1] > 583:
                    self.pauseBlock['color'] = self.RED
                else:
                    self.pauseBlock['color'] = self.BLACK
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] < 75 and event.pos[0] > 50 and event.pos[1] > 583:
                    self.pause = True
                else:
                    self.pauseBlock['color'] = self.BLACK

    def help_button(self, event):
        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] < 50 and event.pos[0] > 25 and event.pos[1] > 583:
                    self.helpBlock['color'] = self.RED
                else:
                    self.helpBlock['color'] = self.BLACK
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] < 50 and event.pos[0] > 25 and event.pos[1] > 583:
                    self.help = True
                else:
                    self.helpBlock['color'] = self.BLACK
        

