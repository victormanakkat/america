#Character
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *
from map import Map
from character import Character
pygame.init()

WINDOWWIDTH = 800
WINDOWHIEGHT = 608
os.environ ['SDL_VIDEO_WINDOW_POS'] = 'center'
surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('America: Learn American History')
mainClock = pygame.time.Clock()

SKY_BLUE = (0, 255, 255)
WHITE = (255, 255, 255)

surface.fill(WHITE)

layout = Map(surface)
man = Character(surface)
x = 12
y = 12
direction = 'S'
while True:
    layout.drawMap()
    layout.sky()
    man.blit(x,y,direction)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == 273:
                y -= 1
                direction = 'N'
            if event.key == 274:
                y += 1
                direction = 'S'
            if event.key == 275:
                x += 1
                direction = 'W'
            if event.key == 276:
                x -= 1
                direction = 'E'
    pygame.display.update()
    mainClock.tick()
