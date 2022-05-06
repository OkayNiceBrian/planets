import sys
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

earth = SpaceObject(600, 200, 200, 1000)
meteor = FlyingObject(100, 150, 10, 1, 2, 0)

purpleBall = pygame.image.load("../assets/ball.png")
purpleBall = pygame.transform.scale(purpleBall, (meteor.radius * 2, meteor.radius * 2))
purpleBallRect = purpleBall.get_rect(topleft=(meteor.x, meteor.y))

earthBall = pygame.image.load("../assets/earth.png")
earthBall = pygame.transform.scale(earthBall, (earth.radius * 2, earth.radius * 2))
earthBallRect = earthBall.get_rect(topleft=(earth.x, earth.y))

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


    # Draw
    screen.fill(black)
    screen.blit(purpleBall, purpleBallRect)
    screen.blit(earthBall, earthBallRect)
    
    pygame.display.flip()
