#Inventory
#By Tyler Spadgenske

import pygame, sys, os
from pygame.locals import *

class Inventory():
    def __init__(self, screen):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.screen = screen
        self.open = False

        self.exit_hover = False
        self.exit_clicked = False
        self.block_selected = [None, None]
        self.give_hover = False
        self.use_hover = False

        #Setup inventory button
        self.inventoryBlock = {'rect':pygame.Rect(0, 558, 25, 25),'color':self.BLACK}
        self.caseImage = pygame.image.load('data\\images\\menus\\briefcase.png')
        self.caseRect = self.caseImage.get_rect()
        self.caseRect.y = 561
        self.caseRect.x = 2

        #Setup exit inventory button
        self.exit_button_image = pygame.image.load('data\\images\\menus\\exit-inventory.png')
        self.clicked_exit_button_image = pygame.image.load('data\\images\\menus\\clicked-exit-inventory.png')
        self.exit_button_rect = self.exit_button_image.get_rect()
        self.exit_button_rect.y = 350
        self.exit_button_rect.x = 620

        #Setup give inventory button
        self.cant_give_button_image = pygame.image.load('data\\images\\menus\\cant-give-inventory.png')
        self.give_button_image = pygame.image.load('data\\images\\menus\\give-inventory.png')
        self.clicked_give_button_image = pygame.image.load('data\\images\\menus\\clicked-give-inventory.png')
        self.cant_give_button_rect = self.cant_give_button_image.get_rect()
        self.cant_give_button_rect.y = 275
        self.cant_give_button_rect.x = 620

        #Setup use inventory button
        self.cant_use_button_image = pygame.image.load('data\\images\\menus\\cant-use-inventory.png')
        self.use_button_image = pygame.image.load('data\\images\\menus\\use-inventory.png')
        self.clicked_use_button_image = pygame.image.load('data\\images\\menus\\clicked-use-inventory.png')
        self.cant_use_button_rect = self.cant_use_button_image.get_rect()
        self.cant_use_button_rect.y = 200
        self.cant_use_button_rect.x = 620

    def inventory_button(self, event=None):
        self.open = self.open_inventory(self.open) 
        pygame.draw.rect(self.screen, self.inventoryBlock['color'], self.inventoryBlock['rect'])
        self.screen.blit(self.caseImage, self.caseRect)
        
        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] < 25 and event.pos[1] > 558 and event.pos[1] < 583:
                    self.inventoryBlock['color'] = self.RED
                else:
                    self.inventoryBlock['color'] = self.BLACK

            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] < 25 and event.pos[1] > 558 and event.pos[1] < 583:
                    self.open = True

    def open_inventory(self, open):
        if open:
            open = False
            self.screen.fill(self.BLACK)
            self.exit_clicked = False
            self.block_selected = [None,None]
            while True:
                self.exit_button()
                self.give_button()
                self.use_button()
                for row in range(0, 4):
                    for column in range(0, 4):
                        if self.block_selected[0] == row and self.block_selected[1] == column:
                            pygame.draw.rect(self.screen, self.RED, pygame.Rect(row * 150 + 25, column * 150 + 25, 100, 100))
                            pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(row * 150 + 27, column * 150 + 27, 96, 96))
                        else:
                            pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(row * 150 + 25, column * 150 + 25, 100, 100))
                            
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        
                    self.exit_button(event)
                    self.give_button(event)
                    self.use_button(event)
                    
                    self.get_square(event)

                pygame.display.update()

                #Check for exit button click
                if self.exit_clicked:
                    break

    def exit_button(self, event=None):
        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] > 620 and event.pos[0] < 770 and event.pos[1] > 350 and event.pos[1] < 387:
                    self.exit_hover = True
                else:
                    self.exit_hover = False

            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] > 620 and event.pos[0] < 770 and event.pos[1] > 350 and event.pos[1] < 387:
                    self.exit_clicked = True

        if self.exit_hover:
            self.screen.blit(self.clicked_exit_button_image, self.exit_button_rect)
        else:
            self.screen.blit(self.exit_button_image, self.exit_button_rect)
    
    def give_button(self, event=None):
        if self.block_selected == [None,None]:
            self.screen.blit(self.cant_give_button_image, self.cant_give_button_rect)
        else:
            if self.give_hover:
                self.screen.blit(self.clicked_give_button_image, self.cant_give_button_rect)
            else:
                self.screen.blit(self.give_button_image, self.cant_give_button_rect)

        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] > 620 and event.pos[0] < 770 and event.pos[1] > 275 and event.pos[1] < 312:
                    self.give_hover = True
                else:
                    self.give_hover = False
            
        
                    
        return open
    
    def use_button(self, event=None):
        if self.block_selected == [None,None]:
            self.screen.blit(self.cant_use_button_image, self.cant_use_button_rect)
        else:
            if self.use_hover:
                self.screen.blit(self.clicked_use_button_image, self.cant_use_button_rect)
            else:
                self.screen.blit(self.use_button_image, self.cant_use_button_rect)

        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] > 620 and event.pos[0] < 770 and event.pos[1] > 200 and event.pos[1] < 237:
                    self.use_hover = True
                else:
                    self.use_hover = False
            
                    
        return open

    def get_square(self, event):
        if event.type == MOUSEBUTTONDOWN:
            #Top row
            if event.pos[0] > 25 and event.pos[0] < 125 and event.pos[1] > 25 and event.pos[1] < 125:
                self.block_selected = [0,0]
            if event.pos[0] > 175 and event.pos[0] < 275 and event.pos[1] > 25 and event.pos[1] < 125:
                self.block_selected = [1,0]
            if event.pos[0] > 325 and event.pos[0] < 425 and event.pos[1] > 25 and event.pos[1] < 125:
                self.block_selected = [2,0]
            if event.pos[0] > 475 and event.pos[0] < 575 and event.pos[1] > 25 and event.pos[1] < 125:
                self.block_selected = [3,0]
            #Second row
            if event.pos[0] > 25 and event.pos[0] < 125 and event.pos[1] > 175 and event.pos[1] < 275:
                self.block_selected = [0,1]
            if event.pos[0] > 175 and event.pos[0] < 275 and event.pos[1] > 175 and event.pos[1] < 275:
                self.block_selected = [1,1]
            if event.pos[0] > 325 and event.pos[0] < 425 and event.pos[1] > 175 and event.pos[1] < 275:
                self.block_selected = [2,1]
            if event.pos[0] > 475 and event.pos[0] < 575 and event.pos[1] > 175 and event.pos[1] < 275:
                self.block_selected = [3,1]
            #third row
            if event.pos[0] > 25 and event.pos[0] < 125 and event.pos[1] > 325 and event.pos[1] < 425:
                self.block_selected = [0,2]
            if event.pos[0] > 175 and event.pos[0] < 275 and event.pos[1] > 325 and event.pos[1] < 425:
                self.block_selected = [1,2]
            if event.pos[0] > 325 and event.pos[0] < 425 and event.pos[1] > 325 and event.pos[1] < 425:
                self.block_selected = [2,2]
            if event.pos[0] > 475 and event.pos[0] < 575 and event.pos[1] > 325 and event.pos[1] < 425:
                self.block_selected = [3,2]
            #bottom row
            if event.pos[0] > 25 and event.pos[0] < 125 and event.pos[1] > 475 and event.pos[1] < 575:
                self.block_selected = [0,3]
            if event.pos[0] > 175 and event.pos[0] < 275 and event.pos[1] > 475 and event.pos[1] < 575:
                self.block_selected = [1,3]
            if event.pos[0] > 325 and event.pos[0] < 425 and event.pos[1] > 475 and event.pos[1] < 575:
                self.block_selected = [2,3]
            if event.pos[0] > 475 and event.pos[0] < 575 and event.pos[1] > 475 and event.pos[1] < 575:
                self.block_selected = [3,3]
        

    
