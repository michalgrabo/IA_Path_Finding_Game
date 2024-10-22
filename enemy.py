import random
import search #from re import search
import settings
import pygame
import node
from settings import tile_size


class Enemy (pygame.sprite.Sprite):
    def __init__(self, pos, map):
        super().__init__()
        self.image = pygame.Surface((tile_size,tile_size))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.game_map = map
        self.hearing_field = settings.visibility_field(3, self.rect)
        self.goal_reached = False

    def move(self):#need to review
        goal = self.generate_x_y()
        path = search.a_search(node.Node(goal[0], goal[1],), node.Node(self.get_grid_pos()[0], self.get_grid_pos()[1]))
        while goal[0] != self.get_grid_pos()[0] and goal[1] != self.get_grid_pos()[1]:
            for item in path:
                x_change = item[0]- self.get_grid_pos()[0]
                y_change = item[1] - self.get_grid_pos()[1]
                self.rect += x_change *tile_size
                self.rect += y_change * tile_size

    def get_grid_pos(self):
        grid_pos = (settings.convert_grid(self.rect.x), settings.convert_grid(self.rect.y))
        return grid_pos

    def generate_x_y(self):
        correct = False
        while not correct:
            x_goal = random.randint(1, len(settings.level_map_grid[0]) -1)
            y_goal = random.randint(1, len(settings.level_map_grid) - 1)
            coordinate_goal = (x_goal, y_goal)
            if settings.level_map_grid[y_goal][x_goal] != 1 and coordinate_goal != self.get_grid_pos():
                correct = True
        return coordinate_goal


    def calculate_field(self):
        self.hearing_field = settings.visibility_field(2, self.rect)

    def update(self, tiles):
        self.calculate_field()



