import pygame
from pygame.locals import *

import sys
import random

mainClock = pygame.time.Clock()
display_size = (500, 500)

pygame.init()
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("Testing gud stuff lol")


# Use a frickin class please
class Square(object):
    def __init__(self, x, y, speed, colour):
        self.x = x    # pos_x
        self.y = y    # pos_y
        self.w = 20   # width
        self.h = 20   # height
        self.colour = colour  # I added a colour field so you'll be able to distinguish the entities
        self.killed = False   # We'll use it later lol

        self.speed = speed    # We will have fun
        self.movement = {"UP": False, "DOWN": False, "RIGHT": False, "LEFT": False}  # Advanced technique, using booleans for movement
        self.movement_reset = self.movement.copy() # If you do self.movement_reset = self.movement, they will share their values so
                                                   # use copy() with list or dicts to make sure they are independant

    def collisions(self):
        # Call this function to make sure the square won't go full OOB (Out of Bounds)
        if self.x > display_size[0] - self.w:
            self.x = display_size[0] - self.w
        if self.x < 0:
            self.x = 0
        if self.y > display_size[1] - self.h:
            self.y = display_size[1] - self.h
        if self.y < 0:
            self.y = 0

    def controller(self, input):
        '''
        Here, we are using a dictionary containing booleans for controlling the movement of the entity,
        dictionnaries are simple, instead of using a list that can change the order of its items and completly
        messs up our program, dicts give us the useful fonctionnality of giving names to our values, the names are
        called key. Controller takes a parameter "input" that will update the dictionnary and define where to move...
        '''
        self.movement.update(input)

        if self.movement["UP"]:
            self.y -= self.speed
        if self.movement["DOWN"]:
            self.y += self.speed
        if self.movement["LEFT"]:
            self.x -= self.speed
        if self.movement["RIGHT"]:
            self.x += self.speed

        self.movement = self.movement_reset  # Here I reset the dict so it wont keep moving

    def draw(self, display):
        # A good habit is to make the display a parameter
        pygame.draw.rect(display, self.colour, ((self.x, self.y), (self.w, self.h)))


def keyboard_inputs():
    keys = pygame.key.get_pressed()
    movement = {"UP": False, "DOWN": False, "RIGHT": False, "LEFT": False}

    if keys[K_LEFT] or keys[K_a]:
        movement["LEFT"] = True
    if keys[K_RIGHT] or keys[K_d]:
        movement["RIGHT"] = True
    if keys[K_DOWN] or keys[K_s]:
        movement["DOWN"] = True
    if keys[K_UP] or keys[K_w]:
        movement["UP"] = True

    return movement

def reverse_AI():
    # This function reverse the values of the dict
    movement = keyboard_inputs()
    for key in movement.keys():
        movement[key] = not movement[key] # NOT inverts the booleans False => True and True => False
    return movement

def follow_AI(ennemy, player):
    '''
    This function compares the position of an ennemy and a player and tell
    to the ennemy where to move to reach the player
    '''
    movement = {"UP": False, "DOWN": False, "RIGHT": False, "LEFT": False}

    if ennemy.x > player.x:
        movement["LEFT"] = True
    if ennemy.x < player.x:
        movement["RIGHT"] = True
    if ennemy.y > player.y:
        movement["UP"] = True
    if ennemy.y < player.y:
        movement["DOWN"] = True

    return movement

Bob = Square(0, 0, 10, (255, 125, 125)) # Player
Henry = Square(400, 400, 10, (0, 255, 125)) # Enemy1
Michelle = Square(0, 400, 1, (0, 0, 255)) # Enemy2

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Enemy1
    Henry.controller(reverse_AI())
    Henry.collisions()
    Henry.draw(screen)

    # Enemy2
    Michelle.controller(follow_AI(Michelle, Bob))
    Michelle.collisions()
    Michelle.draw(screen)

    # Player (Make sure the player is updated the last so the guy who plays always see his player on the top)
    Bob.controller(keyboard_inputs())
    Bob.collisions()
    Bob.draw(screen)
   
    pygame.display.update()
    mainClock.tick(60)