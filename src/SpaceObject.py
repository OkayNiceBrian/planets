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
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    @staticmethod
    def distanceBetween(obj1, obj2):
        assert isinstance(obj1, SpaceObject)
        assert isinstance(obj2, SpaceObject)
        xdif = obj1.x - obj2.x
        ydif = obj1.y - obj2.y
        dist = sqrt(xdif**2 + ydif**2)
        return dist
