import random
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, FONT_STYLE, SCREEN_HEIGHT


class Enemy(Sprite):

    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image_width = 40
        self.image_height = 60
        self.movement_speed = 5
        self.starting_x = (SCREEN_WIDTH//2) - self.image_width
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.image_width)
        self.rect.y = self.image_height


    def update(self):
        self.rect.y += self.movement_speed
        if self.rect.y > SCREEN_HEIGHT:
           self.rect.y = -self.image_height
           self.rect.x = random.randint(0, SCREEN_WIDTH - self.image_width)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        font = pygame.font.SysFont(FONT_STYLE, 20)
        label = font.render(self.name, True, (255, 255, 255))
        screen.blit(label, (self.rect.x, self.rect.y))




