from cmath import sqrt
import pygame
import sys

class SpaceObject:

    def __init__(self, x, y, radius, mass, imageLink):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        
        self.image = pygame.image.load(imageLink)
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        
    @staticmethod
    def distanceBetween(obj1, obj2):
        assert isinstance(obj1, SpaceObject)
        assert isinstance(obj2, SpaceObject)
        xdif = obj1.getX() - obj2.getX()
        ydif = obj1.getY() - obj2.getY()
        dist = sqrt(xdif**2 + ydif**2)
        return dist

    def getX(self):
        offsetX = self.image.get_width() / 2
        return self.x + offsetX
    
    def getY(self):
        offsetY = self.image.get_height() / 2
        return self.y + offsetY