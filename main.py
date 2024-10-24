import pygame, sys
from settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map_2, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            level = Level(level_map, screen)

    screen.fill("black")
    level.run()

    pygame.display.update()
    clock.tick(fps)


