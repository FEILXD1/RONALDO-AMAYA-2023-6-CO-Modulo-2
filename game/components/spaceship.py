import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP
class Spaceship(Sprite):
    coord_x =(1100//2)
    coord_y =300
    speed=10
    def __init__(self):

        self.image = SPACESHIP
        self.rect = self.image.get_rect()
        self.rect.x = self.coord_x
        #self.rect.y = self.coord_y


    def update(self, moving):
        if moving [pygame.K_LEFT]:
            self.moving_left()
        elif moving [pygame.K_RIGHT]:
            self.moving_right()

    def moving_left(self):
        self.rect.x -=self.speed
    def moving_right(self):
        self.rect.x +=self.speed

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

