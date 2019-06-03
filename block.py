#Lia Johnson
#Lej42
#CS 172 HW3
#5/17/19
# This file contains the block class, subclass of drawable

import pygame
from drawable import *

class block(drawable):
    #init method
    def __init__(self, x, y, visible):
       super().__init__(x,y,visible)
       
    #draw 2 rectangles, one that solid and one thats clear with black border
    def draw(self, surface):
        self.__x,self.__y = self.getLoc()
        pygame.draw.rect(surface, (160,32,240), pygame.Rect(int(self.__x), int(self.__y), 20, 20))
        pygame.draw.rect(surface, (0,0,0), pygame.Rect(int(self.__x), int(self.__y), 20, 20),2)
    
    #get bounding rectangle
    def get_rect(self):
        self.__x, self.__y = self.getLoc()
        return pygame.Rect(int(self.__x), int(self.__y), 20,20)
    
        