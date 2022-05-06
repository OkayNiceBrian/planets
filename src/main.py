from cmath import pi
from math import atan2
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

earthImage = "../assets/earth.png"
ballImage = "../assets/ball.png"

earth = SpaceObject(600, 400, 200, 1000, earthImage)
meteor = FlyingObject(100, 150, 10, 1, 1, 0, ballImage)

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

    # Calculate gravitational forces and things
    forceGrav = (1 * earth.mass * meteor.mass) / (SpaceObject.distanceBetween(earth, meteor))**2
    angleBetween = atan2(earth.y - meteor.y, earth.x - meteor.x)
    accelInDirection = forceGrav / meteor.mass
    accel = FlyingObject.determineVelocityVector(accelInDirection, angleBetween)
    meteor.velocity.x += accel.x
    meteor.velocity.y += accel.y

    meteor.update()

    # Draw
    screen.fill(black)
    screen.blit(meteor.image, meteor.rect)
    screen.blit(earth.image, earth.rect)
    
    pygame.display.flip()
