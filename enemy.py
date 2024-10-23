import random
import search #from re import search
import pygame
from node import Node
import time
import settings
from settings import tile_size, level_map_grid


class Enemy (pygame.sprite.Sprite):
    def __init__(self, pos, map):
        super().__init__()
        self.image = pygame.Surface((tile_size,tile_size))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.game_map = map
        self.hearing_field = settings.visibility_field(3, self.rect)
        self.random_movement = False
        self.last_moved_time = 0
        self.delay = 0.8
        self.current_t = 0
        self.heard_far = False
        self.heard_close = False
        self.path_to_goal = []
        self.goal = ()
        self.last_goal = (0,0)

    def get_grid_pos(self):
        grid_pos = (int(settings.convert_grid(self.rect.x)), int(settings.convert_grid(self.rect.y)))
        return grid_pos

    def move(self):#need to review

        if self.heard_far == False and self.heard_close == False and self.random_movement == False:
        #if self.random_movement == True:
            goal = self.generate_x_y()
            #print(self.goal)
            start = Node(self.get_grid_pos()[0], self.get_grid_pos()[1])
            target = Node(goal[0], goal[1])
            path = search.a_search(start, target, level_map_grid)
            while path == None:
                goal = self.generate_x_y()
                start = Node(self.get_grid_pos()[0], self.get_grid_pos()[1])
                target = Node(goal[0], goal[1])
                path = search.a_search(start, target, level_map_grid)
            self.goal = goal
            self.path_to_goal = path
            #print(self.path_to_goal)
            self.random_movement = True
            #print(self.path_to_goal)
            #print("hello")
        if self.heard_far == False and self.heard_close == False and self.random_movement == True:
            #for p in self.path_to_goal: print(p, end=", ")
            if self.goal[0] != self.get_grid_pos()[0] and self.goal[1] != self.get_grid_pos()[1]:
                self.current_t = time.time()
                if self.current_t - self.last_moved_time > self.delay:
                    print("Works")
                    item = self.path_to_goal.pop(0)
                    #self.path_to_goal.remove(item)
                    x_change = int(Node.get_x(item)) - int(self.get_grid_pos()[0])
                    y_change = int(Node.get_y(item)) - int(self.get_grid_pos()[1])
                    self.rect.x += x_change * tile_size
                    self.rect.y += y_change * tile_size
                    self.last_moved_time = self.current_t
            self.random_movement = False

    def generate_x_y(self):
        correct = False
        while not correct:
            #print(len(settings.level_map_grid[0]))
            x_goal = random.randint(1, len(settings.level_map_grid[0]) -2)
            y_goal = random.randint(1, len(settings.level_map_grid) - 2)
            coordinate_goal = (x_goal, y_goal)
            if settings.level_map_grid[y_goal][x_goal] != 1 and coordinate_goal != self.get_grid_pos() and abs(x_goal - self.last_goal[0]) > 2 and abs(y_goal - self.last_goal[1]) > 2:
                self.last_goal = coordinate_goal
                correct = True
        return coordinate_goal

    def calculate_field(self):
        self.hearing_field = settings.visibility_field(2, self.rect)

    def update(self, tiles):
        self.move()
        self.calculate_field()




