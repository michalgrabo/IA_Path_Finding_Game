import random
import search #from re import search
import pygame
from node import Node
import time
import settings
from settings import tile_size, level_map_grid
import player
from player import Player


class Enemy (pygame.sprite.Sprite):
    def __init__(self, pos, map):
        super().__init__()
        self.image = pygame.Surface((tile_size,tile_size))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.game_map = map
        self.hearing_field = settings.visibility_field(6, self.rect, level_map_grid)
        self.need_new_x_y = True
        self.last_moved_time = 0
        self.delay = 0.2
        self.current_t = 0
        self.heard_far = False
        self.heard_close = False
        self.path_to_goal = []
        self.goal = (0,0)
        self.last_goal = (0,0)
        self.player_last_pos = (0, 0)

    def get_grid_pos(self):
        grid_pos = (int(settings.convert_grid(self.rect.x)), int(settings.convert_grid(self.rect.y)))
        return grid_pos

    def check_if_heard(self, player):
        for item in self.hearing_field:
            for item_2 in Player.get_vis_field(player):
                if item == item_2:
                    print("heard")
                    return True
        return False



    def move_type(self, player):#need to review
        if self.check_if_heard(player) and self.player_last_pos != Player.get_grid_pos(player):
            self.need_new_x_y = False
            self.generate_till_rigth("detected", player)
            #self.random_movement = False
        if self.heard_close == False and self.need_new_x_y == True:
            #print("hello")
            self.generate_till_rigth("random", player)
            self.need_new_x_y = False
        self.move()


    def generate_till_rigth(self, type, player):
        if type == "random":
            path = None
            while path == None:
                goal = self.generate_x_y("random", None)
                start = Node(self.get_grid_pos()[0], self.get_grid_pos()[1]) #possibly could deleat
                target = Node(goal[0], goal[1])
                path = search.a_search(start, target, level_map_grid)
            self.goal = goal
            self.path_to_goal = path
        if type == "detected":
            path = None
            while path == None:
                goal = self.generate_x_y("detected", player)
                start = Node(self.get_grid_pos()[0], self.get_grid_pos()[1]) #possibly could deleat
                target = Node(goal[0], goal[1])
                path = search.a_search(start, target, level_map_grid)
            self.goal = goal
            self.path_to_goal = path

    def move(self):
        #print("works")
        if self.goal[0] == self.get_grid_pos()[0] and self.goal[1] == self.get_grid_pos()[1]:
            self.need_new_x_y = True
        else:
            self.current_t = time.time()
            if self.current_t - self.last_moved_time > self.delay:
                #print("Works")
                item = self.path_to_goal.pop(0)
                # self.path_to_goal.remove(item)
                x_change = int(Node.get_x(item)) - int(self.get_grid_pos()[0])
                y_change = int(Node.get_y(item)) - int(self.get_grid_pos()[1])
                self.rect.x += x_change * tile_size
                self.rect.y += y_change * tile_size
                self.last_moved_time = self.current_t


    def generate_x_y(self, type, player):
        correct = False
        if type == "random":
            while not correct:
                #print(len(settings.level_map_grid[0]))
                x_goal = random.randint(1, len(settings.level_map_grid[0]) -2)
                y_goal = random.randint(1, len(settings.level_map_grid) - 2)
                coordinate_goal = (x_goal, y_goal)
                #print(coordinate_goal)
                if settings.level_map_grid[y_goal][x_goal] != 1 and coordinate_goal != self.get_grid_pos() and abs(x_goal - self.last_goal[0]) > 2 and abs(y_goal - self.last_goal[1]) > 2:
                    self.last_goal = coordinate_goal
                    correct = True
            return coordinate_goal
        elif type == "detected":
            player_field = Player.get_vis_field(player)
            while not correct:
                print("here")
                print("here")
                coordinate_goal = player_field[random.randint(0, len(player_field)-1)]
                if coordinate_goal != Player.get_grid_pos(player) and settings.level_map_grid[coordinate_goal[1]][coordinate_goal[0]] != 1:
                    correct = True
            self.player_last_pos = Player.get_grid_pos(player)
            #print(coordinate_goal)
            #print(Player.get_grid_pos(player))
            return coordinate_goal


    def calculate_field(self):
        self.hearing_field = settings.visibility_field(2, self.rect, level_map_grid)
        #print(self.hearing_field)

    def update(self, tiles, player):
        self.move_type(player)
        self.calculate_field()




