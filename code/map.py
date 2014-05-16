import pygame, sys, os
from pygame.locals import *

pygame.init()

SKY_BLUE = (0, 255, 255)
WHITE = (255, 255, 255)

class Map():
    def __init__(self, surface):
        self.screen = surface
        self.BLACK = (0,0,0, 255)
        self.num = 0
        self.num2 = 255
        self.dim = pygame.Surface((800,608))        
        self.dim.fill(self.BLACK)
        self.YELLOW = (255,255,0)
        self.WHITE = (255,255,255)
        self.font = pygame.font.Font('data\\fonts\\font1.ttf', 24)
        self.first = True


    def sky(self,sun):
        block = {'rect':pygame.Rect(0, 0, 800, 130),'color':SKY_BLUE}
        pygame.draw.rect(self.screen, block['color'], block['rect'])

        if sun == 8:
            self.coords = [600,100]
        elif sun == 7:
            self.coords = [550,75]
        elif sun == 6:
            self.coords = [500,50]
        elif sun == 5:
            self.coords = [450, 25]
        elif sun == 4:
            self.coords = [400, 0]
        elif sun == 3:
            self.coords = [350,25]
        elif sun == 2:
            self.coords = [300,50]
        elif sun == 1:
            self.coords = [250, 75]
        elif sun == 0:
            self.coords = [200,100]
        else:
            self.coords = [1000,1000]

        pygame.draw.circle(self.screen, self.YELLOW, self.coords, 40, 0)
        
    def drawMap(self, mapPath='data\\levels\\test.txt'):
        self.map = open(mapPath, 'r')
        
        #Load grass image
        self.grass = pygame.image.load('data\\images\\tiles\\0.png')
        #Load rock image
        self.rock = pygame.image.load('data\\images\\tiles\\1.png')
        #Create rect
        self.rect = self.grass.get_rect()

        x = 0
        y = 3
        for lines in range(0, 18):
            line = self.map.readline()
            for tile in line:
                self.rect.centerx = x * 32
                self.rect.centery = y * 32
                if tile == '0':
                    self.screen.blit(self.grass, self.rect)
                if tile == '1':
                    self.screen.blit(self.rock, self.rect)
                x += 1
            y += 1
            x = 0

    def blackout(self, time):
        self.num += .1
        self.dim.set_alpha(self.num)
        self.screen.blit(self.dim, (0,0))
        return self.num

    def begin(self, time, year,sun):
        if sun == -1:
            self.first = False
        if self.first:
            self.year = self.font.render(year, True, self.WHITE, self.BLACK)
            self.yearRect = self.year.get_rect()
            self.yearRect.centerx = 400
            self.yearRect.centery = 300
            self.screen.blit(self.dim, (0,0)) 
            self.screen.blit(self.year, self.yearRect)
            
        else:
            self.num2 -= 1
            self.dim.set_alpha(self.num2)
            self.screen.blit(self.dim, (0,0))

        
        
