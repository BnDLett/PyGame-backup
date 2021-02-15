import pygame, sys
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
display_size = (500, 500)  # < look
a = pygame.display.set_mode(display_size)
pygame.display.set_caption("Hello World")


class Square(object):
    def __init__(self):
        self.x = 0    # pos_x
        self.y = 0    # pos_y
        self.w = 20   # width
        self.h = 20   # height

    def collisions(self):
        if self.x > display_size[0] - self.w:
            self.x = display_size[0] - self.w
        if self.x < 0:
            self.x = 0
        if self.y > display_size[1] - self.h:
            self.y = display_size[1] - self.h
        if self.y < 0:
            self.y = 0

    def draw(self):
        pygame.draw.rect(a, (255, 255, 0), ((self.x, self.y), (self.w, self.h)))


Bob = Square()

while True:
    a.fill((255, 0, 0))
    
    keys = pygame.key.get_pressed()

    if keys[K_LEFT or K_a]:
        Bob.x -= 20
    if keys[K_RIGHT or K_d]:
        Bob.x += 20
    if keys[K_DOWN or K_s]:
        Bob.y += 20
    if keys[K_UP or K_w]:
        Bob.y -= 20

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                

    Bob.collisions()
    Bob.draw()

    mainClock.tick(60)
    pygame.display.update()