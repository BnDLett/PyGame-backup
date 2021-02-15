import pygame, sys
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()

a = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Run.")

class Player(object):
    def attributes():
        x = 0
        y = 0
        killed = False
    def movement():
        if killed == False:
            for event in pygame.event.get():
                if event.key in (K_UP, K_w):
                    y -= 10
                if event.key in (K_RIGHT, K_d):
                    x += 10
                if event.key in (K_DOWN, K_s):
                    y += 10
                if event.key in (K_LEFT, K_a):
                    x -= 10
    def collision():
        if x == 380:
            x = 380
        if x == 0:
            x = 0
        if y == 280:
            y = 280
        if y == 0:
            y = 0
    def draw():
        pygame.draw.rect(a, (0, 210, 0), ((x, y), (20, 20)))
class Enemy(object):
    def attributes():
        slain = False
        x1 = 380
        y1 = 280
    def movement():
        if x > x1:
            x1 += 5
        if x < x1:
            x1 -= 5
        if y > y1:
            y1 += 5
        if y < y1:
            y1 -= 5
    def kill():
        if x1 == x:
            if y1 == y:
                killed = True
    def draw():
        pygame.draw.rect(a, (255, 0, 0), ((x1, y1), (10, 10)))
    def slain():
        if used == True:
            if x == x1:
                if y == y1:
                    slain = True:
class enemyk(object):
    def attributes():
        b = random.ranint(0, 380)
        c = random.ranint(0, 280)
        x2 = round(b)
        y2 = round(c)
        used = False
    def grabbed():
        if x == x2:
            if y == y2:
                used = True

while True:
    Player.attributes()
    Player.collision()
    Player.movement()
    Player.draw()

    Enemy.attributes()
    Enemy.movement()
    Enemy.kill()
    Enemy.slain()
    Enemy.draw()

    enemyk.attributes()
    enemyk.grabbed()

    pygame.display.update()
    mainClock.tick(60)