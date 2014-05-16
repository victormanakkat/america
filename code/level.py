#Levels
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *
from map import Map
from character import Character
from keyboard import Keyboard
from settings import Settings
from conversation import *

pygame.init()

class Levels():
    def __init__(self,surface):
        self.surface = surface
        self.coords = {'WilliamBradford':[10,10]}
        self.sound = True

    def Y1620(self,clock):
        #Setup objects
        self.layout = Map(self.surface)
        self.man = Character(self.surface)
        self.WilliamBradford = Character(self.surface)
        self.keyboard = Keyboard()
        self.settings = Settings(self.surface)
        self.chat = Conversation(self.surface)
        self.x = 12
        self.y = 12
        self.direction = 'S'
        self.time = [0,0,100]
        self.go = False
        self.firstSound = False
        pygame.mixer.music.load('data\\sound\\Godbless.mid')
        
        while True:
            self.layout.blackout(self.time)
            self.layout.drawMap()
            self.layout.sky()
            self.x, self.y, self.go = self.man.move(self.x,self.y,self.direction,self.time,self.go)
            self.WilliamBradford.move(self.coords['WilliamBradford'][0],self.coords['WilliamBradford'][1],'S',self.time,False,1)
            self.WilliamBradford.check_for_chat(self.time, self.x, self.y, self.coords['WilliamBradford'][0], self.coords['WilliamBradford'][1])
            self.end, self.sound, self.pause, self.help = self.settings.settings_button()
        
            for event in pygame.event.get():
                self.settings.settings_button(event)
                self.WilliamBradford.check_for_chat(self.time, self.x, self.y, self.coords['WilliamBradford'][0], self.coords['WilliamBradford'][1], event)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    self.go, self.direction = self.keyboard.player_input(event, self.go, self.direction)
            pygame.display.update()
            clock.tick()
        
            #Slow down movement
            if self.time[0] == 1:
                self.time[0] = 0
            if self.time[1] == 1:
                self.time[1] = 0
            if self.time[2] == 200:
                self.time[2] = 0
            self.time[0] += 1
            self.time[1] += 1
            self.time[2] += 1
            if self.end:
                break
            if self.sound == False:
                pygame.mixer.music.stop()
                self.firstSound = False
            if self.sound == True and self.firstSound == False:
                pygame.mixer.music.play(-1, 0.0)
                self.firstSound = True