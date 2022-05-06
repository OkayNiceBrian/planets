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
