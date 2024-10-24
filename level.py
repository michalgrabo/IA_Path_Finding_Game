import pygame
from settings import tile_size, screen_width, screen_height
from tile import Tile
from player import Player
from enemy import Enemy
import settings


class Level:

    def __init__(self, level_data, surface):

        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.GroupSingle()
        self.game_map = []
        self.setup_level(level_data)

        #self.world_shift_x = 0
        #self.world_shift_y = 0

    def setup_level(self, layout):

        for row_index, row in enumerate(layout):
            new_row = []
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                elif cell == "p":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                elif cell == "e":
                    enemy_sprite = Enemy((x,y), self.game_map)
                    self.enemy.add(enemy_sprite)
                if cell == "x":
                    new_row.append(0)
                else:
                    new_row.append(1)
            self.game_map.append(new_row)

    def get_player(self):
        return self.player.sprite

    def run(self):
        #self.tiles.update(self.world_shift_x, self.world_shift_y)
        self.tiles.draw(self.display_surface)
        #self.scrolly()
        #self.scroll_x()
        self.player.update()
        self.player.draw(self.display_surface)
        self.enemy.update(self.tiles, self.player.sprite)
        self.enemy.draw(self.display_surface)


