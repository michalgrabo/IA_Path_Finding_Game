from dataclasses import field

import pygame
import time
from settings import level_map_grid
import settings
from settings import tile_size
from node import Node




class Player (pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)
        self.rect_trial = self.rect
        self.pos = pos
        self.direction = pygame.math.Vector2(0, 0)
        #self.speed_fast = 6
        self.speed = 0.000001
        self.speed_counter = 0
        self.last_moved_time = 0
        self.delay = 0.1
        self.current_t = 0
        self.vis_field = settings.visibility_field(2, self.rect)
        #self.last_moved = clock.time.get_tick()

    def get_input(self):
        self.current_t = time.time()
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        self.direction.y = 0
        if self.current_t - self.last_moved_time > self.delay:
            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                #self.rect =
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
            elif keys[pygame.K_UP]:
                """
                time.sleep(1)
                self.x += tile_size
                """
                self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1

            """
            elif keys[pygame.K_f]:
                self.speed = self.speed_fast
            else:

                self.speed = 2
            """
            self.last_moved_time = self.current_t

    def boundary_collisions(self):
        #new_x = settings.convert_grid(self.rect.x + self.direction.x)
        #new_y = settings.convert_grid(self.rect.y + self.direction.y)
        #grid_pos_x = (settings.convert_grid(self.rect.x))
        #grid_pos_y = (settings.convert_grid(self.rect.y))

        grid_pos = self.get_grid_pos()
        #print(grid_pos_x)
        new_pos = (int(grid_pos[0] + self.direction.x), int(grid_pos[1] + self.direction.y))
        #new_x = int(grid_pos_x + self.direction.x)
        #new_y = int(grid_pos_y + self.direction.y)
        #print(new_x)
        #print(self.rect.x, self.rect.y)
        """
        if new_x < len(level_map_grid[0])-1 and new_x >= 1 and new_y  < len(level_map_grid)-1 and new_y >= 1:
            self.rect.x = new_x
            self.rect.y = new_y
        """
        if grid_pos != new_pos:
            #print(level_map_grid[new_pos[1]][new_pos[0]])
            if level_map_grid[new_pos[1]][new_pos[0]] == 0:
                self.rect.x += self.direction.x * tile_size
                self.rect.y += self.direction.y * tile_size
                #print(self.rect.x, self.rect.y)

    def get_grid_pos(self):
        grid_pos = (settings.convert_grid(self.rect.x), settings.convert_grid(self.rect.y))
        return grid_pos

    def calculate_field(self):
        self.vis_field = settings.visibility_field(2, self.rect)


    def update(self, tiles):
        self.get_input()
        #self.horizontal_movement_collision(tiles)
        #self.vertical_movement_collision(tiles)
        self.boundary_collisions()
        self.calculate_field()

"""
    def obstacle_collisons(self):
        new_x = settings.convert_grid(self.rect.x + self.direction.x)
        new_y = settings.convert_grid(self.rect.y + self.direction.y)
        if not level_map_grid[new_y][new_x] == 1:
            self.rect.x = new_x 
            self.rect.y = new_y 
"""



