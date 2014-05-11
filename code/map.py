import pygame, sys, os
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1184
WINDOWHIEGHT = 640
os.environ ['SDL_VIDEO_WINDOW_POS'] = 'center'
surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Test')
mainClock = pygame.time.Clock()

SKY_BLUE = (0, 255, 255)
WHITE = (255, 255, 255)

surface.fill(WHITE)

class Map():
    def __init__(self, surface):
        pass

    def sky(self):
        block = {'rect':pygame.Rect(0, 0, 800, 130),'color':SKY_BLUE}
        pygame.draw.rect(surface, block['color'], block['rect'])
        
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
                    surface.blit(self.grass, self.rect)
                if tile == '1':
                    surface.blit(self.rock, self.rect)
                x += 1
            y += 1
            x = 0

if __name__ == '__main__':
    pygame.init()
    
    WINDOWWIDTH = 1184
    WINDOWHIEGHT = 640
    os.environ ['SDL_VIDEO_WINDOW_POS'] = 'center'
    surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
    pygame.display.set_caption('Test')
    mainClock = pygame.time.Clock()

    SKY_BLUE = (0, 255, 255)
    WHITE = (255, 255, 255)

    surface.fill(WHITE)
    obj = Map(surface)
    obj.drawMap()
    obj.sky()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        mainClock.tick()

  
