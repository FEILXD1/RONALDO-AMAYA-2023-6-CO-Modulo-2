import random
import pygame
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, FONT_STYLE


class Enemy(Sprite):
    enemy_width = 40
    enemy_height = 60
    coord_y = 20
    coord_x = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    mov_x = {0: 'left', 1: 'right'}
    img = {1: ENEMY_1, 2: ENEMY_2}
    mov_x_for = [30, 100]
    def __init__(self, speed_x, speed_y):
        self.img = self.img[random.randint(1, 2)]
        self.img = pygame.transform.scale(self.img, (self.enemy_width, self.enemy_height))
        self.rect = self.img.get_rect()
        self.rect.y = self.coord_y
        self.rect.x = self.coord_x[random.randint(0, 10)]
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.movement_x = self.mov_x[random.randint(0, 1)]
        self.move_x_for = random.randint(self.mov_x_for[0], self.mov_x_for[1])
        self.index = 0
        self.font = pygame.font.SysFont(FONT_STYLE, 15)
        self.font = self.font.render("ENEMY1", True, (255, 0, 255))



    def update(self, ships):
        self.rect.y += self.speed_y
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement_x()


    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
        screen.blit(self.font, (self.rect.x, self.rect.y - (self.enemy_height // 6)))

    def change_movement_x(self):
        self.index += 1  # Se aumenta el índice del enemigo en 1
        # Se comprueba si el enemigo ha llegado al límite de movimiento horizontal o al borde de la pantalla
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (
                self.rect.x >= SCREEN_WIDTH - self.enemy_width):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0


