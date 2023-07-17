import random
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, FONT_STYLE, ENEMY_2, ENEMY_1, SCREEN_HEIGHT

class Enemy2(Sprite):
    enemy_width = 40
    enemy_height = 60
    coord_y = 20
    coord_x = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    #mov_x = {0: 'left', 1: 'right'}
    img = {1: ENEMY_1, 2: ENEMY_2}
    mov_x_for = [10, 20]
    def __init__(self, speed_y):
        self.img = self.img[random.randint(1, 2)]
        self.img = pygame.transform.scale(self.img, (self.enemy_width, self.enemy_height))
        self.rect = self.img.get_rect()
        self.rect.y = self.coord_y
        self.rect.x = self.coord_x[random.randint(0, 10)]
        #self.speed_x = speed_x
        self.speed_y = speed_y
        #self.movement_x = self.mov_x[random.randint(0, 1)]
        self.move_x_for = random.randint(self.mov_x_for[0], self.mov_x_for[1])
        self.index = 0
        self.font = pygame.font.SysFont(FONT_STYLE, 15)
        self.font = self.font.render("ENEMY2", True, (255, 0, 255))



    def update(self):
        self.rect.y += self.speed_y
        self.index += 1
        self.rect.y += self.move_x_for
        if self.rect.x >= SCREEN_HEIGHT - self.enemy_width or self.rect.x <= 10:
            self.move_x_for -= self.move_x_for
            self.rect.y += 10


    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
        screen.blit(self.font, (self.rect.x, self.rect.y - (self.enemy_height // 6)))

