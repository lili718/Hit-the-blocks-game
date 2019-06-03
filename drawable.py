#Lia Johnson
#Lej42
#CS 172 HW3
#5/17/19
# This file contains the drawable class (parent class to other classes)

import pygame
import abc

class drawable(metaclass = abc.ABCMeta):
    #init method
    def __init__(self,x ,y , visible=True):
        self.__x=x
        self.__y=y
        self.__visible = visible
    
    #get location
    def getLoc(self):
        return (self.__x, self.__y)
    
    #abstract draw method
    @abc.abstractmethod
    def draw(self,surface):
        pass
    
    #abstract get rectangle method
    @abc.abstractmethod
    def get_rect(self):
        pass
    
    #getter for x
    def get_x(self):
        return self.__x
    
    #getter for y
    def get_y(self):
        return self.__y
    
    #getter for visibility
    def get_vis(self):
        return self.__visible
    
    #setter for x
    def set_x(self,nx):
        self.__x = nx
    
    #setter for y
    def set_y(self, ny):
        self.__y = ny
    
    #setter for visibility
    def set_vis(self, nvis):
        self.__visible = nvis