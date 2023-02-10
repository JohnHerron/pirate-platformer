import pygame, sys
from settings import *
from tiles import Tile
from level import Level
from game_data import level_0

# set up pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pirate Platformer")
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100, 100), 200))
level = Level(level_0, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)