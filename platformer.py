import pygame
import sys
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOW_SIZE = (750, 500)
GRAVITY = 0.7
MAX_VEL = 20

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Climb")


class Map(object):
    def __init__(self, path, tile_size):
        self.map_path = path

        self.tile_map = list()
        self.tile_size = tile_size

        self.true_scroll = [0, 0]
        self.scroll = self.true_scroll.copy()

    def load(self):
        image = pygame.image.load(self.map_path)
        for y in range(image.get_height()):
            self.tile_map.append([])
            for x in range(image.get_width()):
                if image.get_at((x, y)) == (0, 0, 0):
                    self.tile_map[y].append(pygame.rect.Rect((x * self.tile_size[0], y * self.tile_size[1]), self.tile_size))

    def update(self, player):
        self.true_scroll[0] += (player.rect.x - self.true_scroll[0] - WINDOW_SIZE[0]/2)/10
        self.true_scroll[1] += (player.rect.y - self.true_scroll[1] - WINDOW_SIZE[1]/2)/10
        self.scroll = [int(self.true_scroll[0]), int(self.true_scroll[1])]

    def draw(self, display):
        display.fill((0, 125, 255))
        for y, row in enumerate(self.tile_map):
            for x, tile in enumerate(row):
                if tile != 0:
                    pygame.draw.rect(display, (64, 255, 0), ((tile.x - self.scroll[0], tile.y - self.scroll[1]), tile.size))


class Jumper(object):
    def __init__(self, x, y, w, h, speed, jump_vel, colour):
        self.rect = pygame.rect.Rect(x, y, w, h)
        self.speed = speed
        self.jump_vel = jump_vel
        self.colour = colour

        self.vel = [0, 0]
        self.jumping = False

        self.movement = {"RIGHT": False, "LEFT": False, "JUMP": False}
        self.movement_reset = self.movement.copy()

    def collideTest(self, tile_map):
        collided_tiles = list()
        for row in tile_map:
            for tile in row:
                if tile.colliderect(self.rect): collided_tiles.append(tile)
        return collided_tiles

    def controller(self, controller_input):
        self.movement.update(controller_input)

        if self.movement["RIGHT"]:
            self.vel[0] += self.speed
        elif self.movement["LEFT"]:
            self.vel[0] -= self.speed

        if self.movement["JUMP"] and not self.jumping:
            self.vel[1] -= self.jump_vel
            self.jumping = True
            print('is jumping')

    def collisions(self, tile_map):
        self.vel[1] += GRAVITY
        self.vel[0] = min(MAX_VEL, self.vel[0]) if self.vel[0] > 0 else max(-MAX_VEL, self.vel[0])
        self.vel[1] = min(MAX_VEL, self.vel[1]) if self.vel[1] > 0 else max(-MAX_VEL, self.vel[1])

        self.rect.x = self.rect.x + self.vel[0]
        collided_tiles = self.collideTest(tile_map)
        for tile in collided_tiles:
            if self.vel[0] > 0:
                self.rect.right = tile.left
            elif self.vel[0] < 0:
                self.rect.left = tile.right

        self.rect.y = self.rect.y + self.vel[1]
        collided_tiles = self.collideTest(tile_map)
        for tile in collided_tiles:
            if self.vel[1] > 0:
                self.rect.bottom = tile.top
                self.jumping = False
                self.vel[1] = 0
            elif self.vel[1] < 0:
                self.rect.top = tile.bottom
                self.vel[1] = 0

        self.vel[0] = 0

    def draw(self, display, scroll):
        pygame.draw.rect(display, self.colour, ((self.rect.x - scroll[0], self.rect.y - scroll[1]), self.rect.size))


def keyboard_inputs():
    keys = pygame.key.get_pressed()
    movement = {"RIGHT": False, "LEFT": False, "JUMP": False}

    if keys[K_LEFT] or keys[K_a]:
        movement["LEFT"] = True
    if keys[K_RIGHT] or keys[K_d]:
        movement["RIGHT"] = True
    if keys[K_SPACE]:
        movement["JUMP"] = True

    return movement


Bloko = Map("D:\\HDD_Coding\\Snek\\Test\\01Map.png", [32, 32])
Bloko.load()
Nooblett = Jumper(0, 0, 32, 32, 8, 20, (255, 64, 0))


while True:
    Bloko.update(Nooblett)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Nooblett.controller(keyboard_inputs())
    Nooblett.collisions(Bloko.tile_map)

    Bloko.draw(window)
    Nooblett.draw(window, Bloko.scroll)

    pygame.display.update()
    mainClock.tick(60)
            