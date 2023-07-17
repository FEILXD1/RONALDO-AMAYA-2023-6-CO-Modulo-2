import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, FONT_STYLE
class Spaceship(Sprite):
    refactory_x = 40
    refactory_y = 60
    coord_x = (SCREEN_WIDTH // 2)
    coord_y = 500
    speed = 10

    def __init__(self):
        self.font = pygame.font.SysFont(FONT_STYLE, 15)
        self.font = self.font.render("PLAYER1", True, (255, 0, 255))
        self.img = SPACESHIP
        self.img = pygame.transform.scale(self.img, (self.refactory_x, self.refactory_y))
        self.rect = self.img.get_rect()
        self.rect.x = self.coord_x
        self.rect.y = self.coord_y

    def update(self, moving):
        if moving[pygame.K_LEFT]:
            self.moving_left()
        elif moving[pygame.K_RIGHT]:
            self.moving_right()

    def moving_left(self):
        self.rect.x -= self.speed

    def moving_right(self):
        self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
        screen.blit(self.font, (self.rect.x, self.rect.y-(self.refactory_y//6)))


