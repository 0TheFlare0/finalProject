import pygame
from pygame.sprite import Sprite

#This code is stolen for Mr.Cozart on how to actually load the background
class Background(Sprite):
    def __init__(self, image_file, location):
        super(Background, self).__init__()
        self.image = pygame.image.load("Background.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location