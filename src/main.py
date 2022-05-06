import sys
import pygame
pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

leftPressed = False
rightPressed = False
spacePressed = False

# ball = pygame.image.load("../assets/buddha.png")
# ballrect = ball.get_rect(topleft=(jumper.x, jumper.y))

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
    # screen.blit(ball, ballrect)
    pygame.display.flip()
