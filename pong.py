# Pong in pygame!

# Imports
import pygame
import time

# Setup
width, heigth = 500, 400
Win = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()

x = 20
y = 20

player1x = 0
player1y = 200

m = 20
z = 80

player2x = 480
player2y = 200

c = 3
d = 3

# Game loop
while True:
    clock.tick(60)
    Win.fill("black")
    pygame.draw.line(
        Win, (0, 255, 0), [width / 2, heigth], [width / 2, heigth - heigth], 5
    )

    ball = pygame.draw.rect(Win, (0, 0, 255), [x, y, 20, 20], 10)

    player1 = pygame.draw.rect(Win, (255, 255, 255), [player1x, player1y, m, z], 10)

    player2 = pygame.draw.rect(Win, (255, 255, 255), [player2x, player2y, 20, 80], 10)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1y -= 10
            if event.key == pygame.K_s:
                player1y += 10

            if event.key == pygame.K_UP:
                player2y -= 10
            if event.key == pygame.K_DOWN:
                player2y += 10

    x += c
    if x >= 510:
        x = width / 2
        y = heigth / 2
        c = c * -1
    if x <= -10:
        x = width / 2
        y = heigth / 2
        c = c * -1

    y += d

    if y >= 400:
        y = 400
        d = d * -1

    if y <= 0:
        y = 0
        d = d * -1

    collide = pygame.Rect.colliderect(ball, player1)
    collide2 = pygame.Rect.colliderect(ball, player2)

    if collide:
        x = 20
        c = c * -1

    if collide2:

        x = 460
        c = c * -1

    # Display
    pygame.display.update()
