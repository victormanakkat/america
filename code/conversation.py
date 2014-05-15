#Conversation
#By Tyler Spadgenske

import pygame, sys, os, time
from pygame.locals import *

class Blit():
    def __init__(self, screen):
        self.screen = screen

        #Setup text lines
        self.raw_ln1 = ''
        self.raw_ln2 = ''
        self.raw_ln3 = ''
        self.first = True

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.font = pygame.font.Font('data\\fonts\\font1.ttf', 10)

        #Setup bubble images and rect
        self.lchat = pygame.image.load('data\\images\\menus\\lchat.png')
        self.rchat = pygame.image.load('data\\images\\menus\\rchat.png')
        self.rect = self.lchat.get_rect()
        self.rect.x = 500

        #Setup profile pictures
        self.c0 = pygame.image.load('data\\images\\sprites\\0\\0g.png')
        self.c1 = pygame.image.load('data\\images\\sprites\\1\\1g.png')
        self.sprite_rect = self.c0.get_rect()        
        
    def blit(self,text,loc,speaker=None):
        if self.first:
            for i in range(0, len(text)):
                if i < 28:
                    self.raw_ln1 = self.raw_ln1 + text[i]
                elif i < 56:
                    self.raw_ln2 = self.raw_ln2 + text[i]
                else:
                    self.raw_ln3 = self.raw_ln3 + text[i]
            self.first = False
        self.rect.y = loc * 100
        self.ln1 = self.font.render(self.raw_ln1, True, self.BLACK, self.WHITE)
        self.ln2 = self.font.render(self.raw_ln2, True, self.BLACK, self.WHITE)
        self.ln1r = self.ln1.get_rect()
        self.ln2r = self.ln2.get_rect()
        self.ln3 = self.font.render(self.raw_ln3, True, self.BLACK, self.WHITE)
        self.ln3r = self.ln3.get_rect()

        #Add text to right height
        if speaker == None:
            self.ln1r.x = 570
            self.ln2r.x = 570
            self.ln3r.x = 570
            self.sprite_rect.x = 511
        else:
            self.ln1r.x = 515
            self.ln2r.x = 515
            self.ln3r.x = 515
            self.sprite_rect.x = 739
            
        if loc == 0:
            self.ln1r.y = 20
            self.ln2r.y = 38
            self.ln3r.y = 56
            self.sprite_rect.y = 10
        elif loc == 1:
            self.ln1r.y = 120
            self.ln2r.y = 138
            self.ln3r.y = 156
            self.sprite_rect.y = 110
        elif loc == 2:
            self.ln1r.y = 220
            self.ln2r.y = 238
            self.ln3r.y = 256
            self.sprite_rect.y = 210
        elif loc == 3:
            self.ln1r.y = 320
            self.ln2r.y = 338
            self.ln3r.y = 356
            self.sprite_rect.y = 310
        elif loc == 4:
            self.ln1r.y = 420
            self.ln2r.y = 438
            self.ln3r.y = 456
            self.sprite_rect.y = 0
        else:
            self.ln1r.y = 1000
            self.ln2r.y = 1000
            self.ln3r.y = 1000
            self.sprite_rect.y = 1000
            
        #Blit red box
        if speaker == None:
            self.screen.blit(self.lchat, self.rect)
            self.screen.blit(self.c0, self.sprite_rect)
        #Blit blue box
        else:
            self.screen.blit(self.rchat, self.rect)
            self.screen.blit(self.c1, self.sprite_rect)
        self.screen.blit(self.ln1, self.ln1r)
        self.screen.blit(self.ln2, self.ln2r)
        self.screen.blit(self.ln3,self.ln3r)
        
class Conversation():
    def __init__(self, screen):
        self.screen = screen

        self.loc = []
        self.block = []
        
    def chat(self,time,speakers,conversation):
        if time[2] == 200:
            if len(conversation) != len(self.loc):
                self.loc.append(4)
                self.block.append(Blit(self.screen))
            for i in range(0,len(self.loc)):
                self.loc[i] -= 1
                
        self.num = 0
        for i in self.block:
            i.blit(conversation[self.num], self.loc[self.num],speakers[self.num])
            self.num += 1
