import pygame
import sys
import random
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()

a = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Run.")

class Player(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.killed = False

    def collision(self):
        '''
        if x == 380:   # Please, use > and < because if your game glitches, your player will be OOB and will be confused
            x = 380    # With < and >, even if the player finds a bug that can teleport him at (9999, 9999), he will always stay in the screen.
        if x == 0:
            x = 0
        if y == 280:
            y = 280
        if y == 0:
            y = 0
        '''
        if self.x > 380:  # See, its simple
            self.x = 380
        if self.x < 0:
            self.x = 0
        if self.y > 280:
            self.y = 280
        if self.y < 0:
            self.y = 0

    def draw(self):
        pygame.draw.rect(a, (0, 210, 0), ((self.x, self.y), (20, 20)))

class Enemy(object):
    def __init__(self):
        self.x = 380
        self.y = 280
        self.slained = False

    def movement(self, player):
        if self.slained == False:
            if player.x > self.x:
                self.x += 1
            if player.x < self.x:
                self.x -= 1
            if player.y > self.y:
                self.y += 1
            if player.y < self.y:
                self.y -= 1

    def kill(self, player):
        if self.x == player.x and self.y == player.y and not self.slained:  # Use AND instead of chaining IF
            player.killed = True                                            # I also added NOT self.slained so the ennemy is unable to kill the player if he's killed first lol

    def draw(self):
        pygame.draw.rect(a, (255, 0, 0), ((self.x, self.y), (10, 10)))

    def slain(self, player, enemy_killer):  # Here, you used SLAIN as a class function and an attribute, if you do that, you'll overwrite the oldest one who use the name
        if enemy_killer.used == True:
            if player.x == self.x and player.y == self.y:  # Use AND instead of chaining IF
                    self.slained = True

class EnemyKiller(object):
    def __init__(self):
        '''
        x = round(random.randint(0, 380))  # Your player move every 10 blocs so if the enemy_killer is at (100, 265), you are fucked
        y = round(random.randint(0, 280))  # So lemme use a trick to make sure the enemy killer will be a multiple of 10.
        '''
        self.x = round(random.randint(0, 38) * 10) # Multiplying per 10 lol
        self.y = round(random.randint(0, 28) * 10)
        self.used = False

    def grabbed(self, player):
        if player.x == self.x:
            if player.y == self.y:
                self.used = True

    def draw(self):
        if self.used == False:  # Why keep drawing the enemy killer if its being used ?
            pygame.draw.rect(a, (255, 255, 255), ((self.x, self.y), (5, 5)))

Nooblett = Player()     # Creates the player by initialasing his attributes (__init__ is used when u create a new object from a class)
Goomba = Enemy()        # Same ^^
Sword = EnemyKiller()   # the way you coded it reminds me a sword so...
bk_colour = (0, 0, 0)   # The bk colour change if you are killed so I turned it int a var

while True:
    if Nooblett.killed == True:
        bk_colour = (0, 125, 255)
    a.fill(bk_colour)
    '''
    Player.attributes()   # If you call Player.attributes while running, you will constantly reset his values
    Player.collision()
    Player.movement()
    Player.draw()         # I told you to update the player in last so we always see him on top
    '''

    '''
    Enemy.attributes()    # Same for the enemy, call __init__ while loading the game, not during the game
    Enemy.movement()
    Enemy.kill()
    Enemy.slain()
    Enemy.draw()
    '''

    '''
    enemyk.attributes()   # I think u understood at this point :D
    enemyk.grabbed()
    '''
    for event in pygame.event.get():   # Avoid iterating through events multiple times, you might loose performances, thats why I moved player movement here
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if Nooblett.killed == False:
            if event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    Nooblett.y -= 10
                if event.key in (K_RIGHT, K_d):
                    Nooblett.x += 10
                if event.key in (K_DOWN, K_s):
                    Nooblett.y += 10
                if event.key in (K_LEFT, K_a):
                    Nooblett.x -= 10

    Sword.grabbed(Nooblett)
    Sword.draw()

    Goomba.movement(Nooblett)
    Goomba.slain(Nooblett, Sword)
    Goomba.kill(Nooblett)
    Goomba.draw()

    Nooblett.collision()
    Nooblett.draw()

    pygame.display.update()
    mainClock.tick(60)
