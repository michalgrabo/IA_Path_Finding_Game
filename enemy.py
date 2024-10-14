import random

import pygame



class Enemy (pygame.sprite.Sprite):
    def __init__(self, pos, map):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.game_map = map

    def horizontal_movement_collision(self, tiles):
        self.rect.x += random.randint(-5, 5)

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right
                elif self.direction.x > 0:
                    self.rect.right = tile.rect.left

    def vertical_movement_collision(self, tiles):
        self.rect.y += random.randint(-5, 5)

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.y < 0:
                    self.rect.top = tile.rect.bottom
                elif self.direction.y > 0:
                    self.rect.bottom = tile.rect.top

    def update(self, tiles):
        self.horizontal_movement_collision(tiles)
        self.vertical_movement_collision(tiles)



