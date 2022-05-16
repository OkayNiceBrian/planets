from cmath import pi
from math import atan2
from re import A
import sys
from numpy import angle
import pygame
from SpaceObject import SpaceObject
from FlyingObject import FlyingObject
pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

leftPressed = False
rightPressed = False
spacePressed = False

planets = []
fliers = []

earthImage = "../assets/earth.png"
ballImage = "../assets/ball.png"

earth = SpaceObject(600, 400, 200, 10000, earthImage)
meteor = FlyingObject(500, 130, 10, 1, 6, 0, ballImage)

planets.append(earth)
fliers.append(meteor)

while 1:
    # Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftPressed = True
            if event.key == pygame.K_RIGHT:
                rightPressed = True
            if event.key == pygame.K_SPACE:
                spacePressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftPressed = False
            if event.key == pygame.K_RIGHT:
                rightPressed = False
            if event.key == pygame.K_SPACE:
                spacePressed = False

    # Update
    speedConstant = clock.tick(60)

    if leftPressed and rightPressed:
        True
    elif leftPressed:
        True
    elif rightPressed:
        True
    else:
        True

    if spacePressed:
        True

    for i in fliers:
        for j in fliers:
            if i != j:
                forceGrav = (1 * j.mass * i.mass) / (SpaceObject.distanceBetween(j, i))**2
                angleBetween = atan2(j.y - i.y, j.x - i.x)
                accelInDirection = forceGrav / i.mass
                accel = FlyingObject.determineVelocityVector(accelInDirection, angleBetween)
                i.velocity.x += accel.x
                i.velocity.y += accel.y
        for p in planets:
            forceGrav = (1 * p.mass * i.mass) / (SpaceObject.distanceBetween(p, i))**2
            angleBetween = atan2(p.y - i.y, p.x - i.x)
            accelInDirection = forceGrav / i.mass
            accel = FlyingObject.determineVelocityVector(accelInDirection, angleBetween)
            i.velocity.x += accel.x
            i.velocity.y += accel.y
    
    for f in fliers:
        f.update()

    # Draw
    screen.fill(black)
    
    for f in fliers:
        screen.blit(f.image, f.rect)
        
    for p in planets:
        screen.blit(p.image, p.rect)
    
    pygame.display.flip()
