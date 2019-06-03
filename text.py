#Lia Johnson
#Lej42
#CS 172 HW3
#5/17/19
# This file contains the text class subclass of drawable

from drawable import *
import pygame

class text(drawable):
    #init method
    def __init__(self, x, y, visible, text):
       super().__init__(x,y, visible)
       self.__text = text
    
    #set font type to arial
    #display text on surface
    def draw(self, surface):
        self.__x,self.__y = self.getLoc()
        fType = pygame.font.Font(pygame.font.match_font("arial"), 20)
        score = fType.render(self.__text, True, [0,0,0])
        surface.blit(score, [self.__x,self.__y])
        
    #get bounding rectangle
    def get_rect(self):
        self.__x, self.__y = self.getLoc()
        return pygame.Rect(self.__x, self.__y, 20,20)
    