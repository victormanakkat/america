#Levels
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *
from map import Map
from character import Character
from keyboard import Keyboard
from settings import Settings
from conversation import *
from inventory import *
from buildings import *

pygame.init()

class Levels():
    def __init__(self,surface):
        self.surface = surface
        self.coords = {'WilliamBradford':[10,10]}
        self.sound = True

        self.banned = []
        self.run = True
        self.talk = False
        self.coming = ''
        #Blocks allowed to move in
        self.allowedPaths = {'main':'data\\levels\\1620\\allowed.txt'}
        self.cant_talk_box = Conversation(self.surface)

    def cant_talk(self, time):
        if self.talk:
            #Can't talk message
            self.cant_talk_box.chat(time, [None], 'data\\cant_talk.txt', 1)
            
    def stay_on_screen(self, x, y):
        self.allowed = open(self.allowedPaths['main'], 'r')
        x2 = 0
        y2 = 1
        if self.run:
            self.run = False
            for lines in range(0, 18):
                line = self.allowed.readline()
                for tile in line:
                    if tile == 'Y':
                        pass #Do Nothing. You can walk on this tile.
                    if tile == 'N':
                        self.banned.append([x2,y2])
                    x2 += 1
                x2 = 0
                y2 += 1

        for coord in self.banned:
            if y + 1 == coord[1] and x == coord[0]:
                self.coming = 'top'
            elif y - 1 == coord[1] and x == coord[0]:
                self.coming = 'bottom'
            elif x + 1 == coord[0] and y == coord[1]:
                self.coming = 'left'
            elif x - 1 == coord[0] and y == coord[1]:
                self.coming = 'right'
                
            if x == coord[0] and y == coord[1]:
                if self.coming == 'left':
                    x = x - 1
                if self.coming == 'right':
                    x = x + 1
                if self.coming == 'top':
                    y = y - 1
                if self.coming == 'bottom':
                    y = y + 1
                self.coming = ''
                self.talk = True
                self.cant_talk_box = Conversation(self.surface)
                    
        return x,y
    
    def Y1620(self,clock):
        #Setup objects
        self.layout = Map(self.surface)
        self.man = Character(self.surface)
        self.WilliamBradford = Character(self.surface)
        self.keyboard = Keyboard()
        self.settings = Settings(self.surface)
        self.inventory =  Inventory(self.surface)
        self.chat = Conversation(self.surface)
        self.mayflower = Mayflower(self.surface)
        
        self.x = 15
        self.y = 15
        self.direction = 'S'
        self.time = [0,0,100]
        self.go = False
        self.sun = -2
        self.firstSound = False
        pygame.mixer.music.load('data\\sound\\Godbless.mid')
        self.quit = 0
        while True:
            if self.sun > 8:
                pass #self.quit = self.layout.blackout(time)
            if self.sun < 0:
                self.layout.begin(time,'1620',self.sun)
            self.layout.sky(self.sun)
            self.x, self.y = self.stay_on_screen(self.x,self.y)
            self.layout.drawMap()
            self.x, self.y, self.go = self.man.move(self.x,self.y,self.direction,self.time,self.go)
            self.WilliamBradford.move(self.coords['WilliamBradford'][0],self.coords['WilliamBradford'][1],'S',self.time,False,1)
            self.WilliamBradford.check_for_chat(self.time, self.x, self.y, self.coords['WilliamBradford'][0], self.coords['WilliamBradford'][1])
            self.end, self.sound, self.pause, self.help = self.settings.settings_button()
            self.inventory.inventory_button()

            self.cant_talk(self.time)
            
            #Blit Mayflower
            self.mayflower.blit()
            
            if self.sun > 8:
                pass #self.quit = self.layout.blackout(time)
            if self.sun < 0:
                self.layout.begin(time, '1620',self.sun)

            if self.quit > 254:
                break
                
            for event in pygame.event.get():
                self.settings.settings_button(event)
                self.inventory.inventory_button(event)
                self.WilliamBradford.check_for_chat(self.time, self.x, self.y, self.coords['WilliamBradford'][0], self.coords['WilliamBradford'][1], event)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    self.go, self.direction = self.keyboard.player_input(event, self.go, self.direction)
                    if event.key == K_SPACE:
                        print self.x, self.y
            pygame.display.update()
            clock.tick()
        
            #Slow down movement
            if self.time[0] == 1:
                self.time[0] = 0
            if self.time[1] == 1:
                self.time[1] = 0
            if self.time[2] == 200:
                self.time[2] = 0
                self.sun += 1
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
