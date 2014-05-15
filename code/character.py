#Character
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *
from conversation import *

class Character():
    def __init__(self, surface):
        self.chat = [Conversation(surface)]
        self.surface = surface
        self.pixel = 0.03125
        self.step = 0
        self.slide = 0
        self.start = False
        self.num = 0
        
        #North
        self.manF = pygame.image.load('data\\images\\sprites\\0\\0b.png')
        self.manFr = pygame.image.load('data\\images\\sprites\\0\\0f.png')
        self.manN = [self.manF, self.manFr]

        #South
        self.manB = pygame.image.load('data\\images\\sprites\\0\\0a.png')
        self.manBr = pygame.image.load('data\\images\\sprites\\0\\0d.png')
        self.manS = [self.manB, self.manBr]
        
        #East
        self.manL = pygame.image.load('data\\images\\sprites\\0\\0c.png')
        self.manLr = pygame.image.load('data\\images\\sprites\\0\\0e.png')
        self.manE = [self.manL, self.manLr]

        #West
        self.manR = pygame.transform.flip(self.manL, True, False)
        self.manRl = pygame.transform.flip(self.manLr, True, False)
        self.manW = [self.manR, self.manRl]

        #Rectangle
        self.rect = self.manF.get_rect()

        #William Bradford
        self.c0 = pygame.image.load('data\\images\\sprites\\1\\1a.png')
    def convert_coords(self, x, y):
        x = x * 32
        y = y * 32
        return x, y

    def move(self, x, y, dir, time, go,NPC=False):
        if time[0] == 1:
            if go:
                self.slide += 1
                if dir == 'N':
                    y -= self.pixel 
                if dir == 'S':
                    y += self.pixel
                if dir == 'E':
                    x -= self.pixel
                if dir == 'W':
                    x += self.pixel
                self.step += self.pixel
                
        if self.step == 1:
            self.step = 0
            go = False
                
        self.blit(x,y,dir,self.slide,NPC)
        if self.slide == 1:
            self.slide = 0

        return x,y,go
        
        

    def blit(self, x, y, dir,slide,NPC):
        x, y = self.convert_coords(x, y)
        self.rect.y = y
        self.rect.x = x
        if NPC==False:
            if dir == 'S':
                self.surface.blit(self.manS[slide], self.rect)
            if dir == 'N':
                self.surface.blit(self.manN[slide], self.rect)
            if dir == 'E':
                self.surface.blit(self.manE[slide], self.rect)
            if dir == 'W':
                self.surface.blit(self.manW[slide], self.rect)
        elif NPC == 1:
            if dir == 'N':
                pass
            if dir == 'S':
                self.surface.blit(self.c0, self.rect)
            if dir == 'E':
                pass
            if dir == 'W':
                pass

    def check_for_chat(self, time, x, y, NPCx, NPCy, event=None):
        if event != None:
            if NPCx + 1 == x and NPCy == y or NPCx - 1 == x and NPCy == y or NPCy + 1 == y and NPCx == x or NPCy - 1 == y and NPCx == x:
                if event.type == KEYDOWN:
                    if event.key == 99:
                        self.start = True
                        self.num += 1
                        self.chat.append(Conversation(self.surface))
        if self.start:
            self.chat[self.num].chat(time,['',None,'',None,None],['Hello. My Name is William   Bradford.',
                                                          'Hello. I am lost. Do you    know where I am?',
                                                          'You are in Holland.',
                                                        'Thank you.'])
