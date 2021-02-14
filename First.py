import pygame, sys, random
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
a = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Run")
x = 0
y = 0
x1 = 380
y1 = 280
def blocc():
    c = random.randint(0, 380)
    b = random.randint(0, 280)
    print(c)
    print(b)
    x2 = round(c, -1)
    y2 = round(b, -1)
    print(x2)
    print(y2)
blocc()
killed = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if killed == False:
            if event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    if x > 0:
                        x -= 10
                if event.key in (K_RIGHT, K_d):
                    if x < 380:
                        x += 10
                if event.key in (K_DOWN, K_s):
                    if y < 280:
                        y += 10
                if event.key in (K_UP, K_w):
                    if y > 0:
                        y -= 10
                if x1 > x:
                    x1 -= 5
                else:
                    x1 += 5
                if y1 > y:
                    y1 -= 5
                else:
                    y1 += 5
            if x == x1:
                if y == y1:
                    a.fill((0, 0, 0))
                    killed = True
                else:
                    a.fill((0, 0, 255))
            else:
                a.fill((0, 0, 255))
        elif killed == True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    try:
        block = pygame.draw.rect(a, (255, 255, 255), ((x2, y2), (20, 20)))
        pygame.draw.rect(a, (0, 210, 0), ((x, y), (20, 20))) #player
        enemy = pygame.draw.rect(a, (255, 0, 0), ((x1, y1), (20, 20))) #enemy
        pygame.display.update()
        mainClock.tick(60)
    except:
        pygame.draw.rect(a, (0, 210, 0), ((x, y), (20, 20))) #player
        enemy = pygame.draw.rect(a, (255, 0, 0), ((x1, y1), (20, 20))) #enemy
        pygame.display.update()
        mainClock.tick(60)