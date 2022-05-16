from argparse import MetavarTypeHelpFormatter
from cmath import pi, sqrt, sin, cos
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
viewXOffset = 0
viewYOffset = 0

leftPressed = False
rightPressed = False
upPressed = False
downPressed = False
spacePressed = False
leftMousePressed = False
middleMousePressed = False
rightMousePressed = False

entities = []
planets = []
fliers = []

earthImage = "../assets/earth.png"
ballImage = "../assets/ball.png"

earth = SpaceObject(600, 400, 200, 5000, earthImage)
meteor = FlyingObject(500, 130, 10, 1, 6, 0, ballImage)

entities.append(earth)
entities.append(meteor)
planets.append(earth)
fliers.append(meteor)

gameplayPaused = True
drawingDirectionalLine = gameplayPaused
MAX_SHOT_POWER = 400
SHOT_POWER_DIVISOR = 50
shotPower = 0

def calculateGravity(flier, spaceObject):
    forceGrav = (1 * spaceObject.mass * flier.mass) / (SpaceObject.distanceBetween(spaceObject, flier))**2
    angleBetween = atan2(spaceObject.getY() - flier.getY(), spaceObject.getX() - flier.getX())
    accelInDirection = forceGrav / flier.mass
    accel = FlyingObject.determineVelocityVector(accelInDirection, angleBetween)
    return accel

def distanceBetween(x1, y1, x2, y2):
    xdif = x1 - x2
    ydif = y1 - y2
    dist = sqrt(xdif**2 + ydif**2)
    return dist

def calculateShotPower():
    assert(fliers.__len__() > 0)
    mousePosTuple = pygame.mouse.get_pos()
    mousePos = {
        'x': mousePosTuple[0],
        'y': mousePosTuple[1]
    }
    dist = distanceBetween(mousePos['x'], mousePos['y'], fliers[0].getX() + viewXOffset, fliers[0].getY() + viewYOffset).real
    _shotPower = 0
    if dist < MAX_SHOT_POWER:
        _shotPower = dist
    else:
        _shotPower = MAX_SHOT_POWER
    return _shotPower

def drawDirectionalLine(screen):
    assert(fliers.__len__() > 0)
    dotNum = 10
    mousePosTuple = pygame.mouse.get_pos()
    mousePos = {
        'x': mousePosTuple[0],
        'y': mousePosTuple[1]
    }
    dist = shotPower
    distBetweenDots = dist / (dotNum + 1)
    angleBetween = atan2(mousePos['y'] - (fliers[0].getY() + viewYOffset), mousePos['x'] - (fliers[0].getX() + viewXOffset))
    xdist = (distBetweenDots * cos(angleBetween)).real
    ydist = (distBetweenDots * sin(angleBetween)).real
    for i in range(dotNum):
        pygame.draw.circle(screen, (200, 200, 50, 50), ((fliers[0].getX() + viewXOffset) + xdist + (xdist * i), (fliers[0].getY() + viewYOffset) + ydist + (ydist * i)), 1)

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
            if event.key == pygame.K_UP:
                upPressed = True
            if event.key == pygame.K_DOWN:
                downPressed = True
            if event.key == pygame.K_SPACE:
                spacePressed = True
                gameplayPaused = not gameplayPaused
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftPressed = False
            if event.key == pygame.K_RIGHT:
                rightPressed = False
            if event.key == pygame.K_UP:
                upPressed = False
            if event.key == pygame.K_DOWN:
                downPressed = False
            if event.key == pygame.K_SPACE:
                spacePressed = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed = pygame.mouse.get_pressed()
            if mousePressed[0]:
                leftMousePressed = True
                print("left mouse pressed")
            if mousePressed[1]:
                middleMousePressed = True
                print("middle mouse pressed")
            if mousePressed[2]:
                rightMousePressed = True
                print("right mouse pressed")
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed()[0]:
                leftMousePressed = False
                print("left mouse released")
            if pygame.mouse.get_pressed()[1]:
                middleMousePressed = False
                print("middle mouse released")
            if pygame.mouse.get_pressed()[2]:
                rightMousePressed = False
                print("right mouse released")

    # Update
    speedConstant = clock.tick(60)

    if leftPressed and rightPressed:
        True
    elif leftPressed:
        viewXOffset += 2
    elif rightPressed:
        viewXOffset -= 2
    elif upPressed:
        viewYOffset += 2
    elif downPressed:
        viewYOffset -= 2
    else:
        True

    if spacePressed:
        True

    if gameplayPaused:
        shotPower = calculateShotPower()
        drawingDirectionalLine = True
        
        #Shoot the ball!
        if leftMousePressed:
            assert(fliers.__len__() > 0)
            mousePosTuple = pygame.mouse.get_pos()
            mousePos = {
                'x': mousePosTuple[0],
                'y': mousePosTuple[1]
            }   
            angleBetween = atan2((fliers[0].getY() + viewYOffset) - mousePos['y'], (fliers[0].getX() + viewXOffset) - mousePos['x'])
            fliers[0].setSpeedAndHeading(shotPower / SHOT_POWER_DIVISOR, angleBetween)
            gameplayPaused = not gameplayPaused

    if not gameplayPaused:
        shotPower = 0
        drawingDirectionalLine = False
        
        # Calculate the gravitational forces acting on the flier
        for i in fliers:
            for j in fliers:
                if i != j:
                    accel = calculateGravity(i, j)
                    i.velocity.x += accel.x
                    i.velocity.y += accel.y
            for p in planets:
                accel = calculateGravity(i, p)
                i.velocity.x += accel.x
                i.velocity.y += accel.y
        
        # for p in planets: 
        #     p.update()
        # for f in fliers:
        #     f.update()
        
        for e in entities:
            e.update()
            
    leftMousePressed = False
    middleMousePressed = False
    rightMousePressed = False    

    # Draw
    screen.fill(black)
    
    # for f in fliers:
    #     f.rect.x = f.rect.x + viewXOffset
    #     f.rect.y = f.rect.y + viewYOffset
    #     screen.blit(f.image, f.rect)
        
    # for p in planets:
    #     p.rect.x = p.rect.x + viewXOffset
    #     p.rect.y = p.rect.y + viewYOffset
    #     screen.blit(p.image, p.rect)
    
    for e in entities:
        e.rect.x = e.x + viewXOffset
        e.rect.y = e.y + viewYOffset
        screen.blit(e.image, e.rect)
        
    if drawingDirectionalLine:
        drawDirectionalLine(screen)
    
    pygame.display.flip()
    

