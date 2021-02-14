import pygame, sys
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
a = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World")
x = 20
y = 20
while True:
    a.fill((255, 0, 0))
    pygame.draw.rect(a, (255, 255, 0), ((x, y), (20, 20)))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key in (K_LEFT, K_a):
                if x > 0:
                    x -= 20
            if event.key in (K_RIGHT, K_d):
                if x < 380:
                    x += 20
            if event.key in (K_DOWN, K_s):
                if y < 280:
                    y += 20
            if event.key in (K_UP, K_w):
                if y > 0:
                    y -= 20
    pygame.display.update()
    mainClock.tick(60)