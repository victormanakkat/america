#Character
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *
from map import Map
from character import Character
from keyboard import Keyboard
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
keyboard = Keyboard()
x = 12
y = 12
direction = 'S'
time = [0,0]
go = False
while True:
    layout.drawMap()
    layout.sky()
    x, y, go = man.move(x,y,direction,time,go)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            go, direction = keyboard.player_input(event, go, direction)
    pygame.display.update()
    mainClock.tick()
    
    #Slow down movement
    if time[0] == 1:
        time[0] = 0
    time[0] += 1
    if time[1] == 1:
        time[1] = 0
    time[1] += 1

