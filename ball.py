#Lia Johnson
#Lej42
#CS 172 HW3
#5/17/19
# This file contains the ball class, subclass of drawable

from drawable import *
import pygame

class ball(drawable):
    #init method
    def __init__(self, x, y, visible):
       super().__init__(x,y,visible)
       
    #draw circle
    def draw(self, surface):
        self.__x,self.__y = self.getLoc()
        pygame.draw.circle(surface, [255,0,0], [int(self.__x), int(self.__y)],10)
        
    #get  bounding rectangle
    def get_rect(self):
        self.__x,self.__y = self.getLoc()
        return pygame.Rect(self.__x,self.__y,10,10)