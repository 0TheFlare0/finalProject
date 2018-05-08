#adapted from cozort
import pygame
from pygame.sprite import Sprite
from settings import Settings

# a class to represent an enemy ship
class Boss():
    def __init__(self, ai_settings, screen):
        # init the alien and set its starting pos
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the enemy image and set its rect attribute
        self.image = pygame.image.load('Boss.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each enemy at the middle right screen
        self.rect.midright = self.screen_rect.midright

        # store aliens exact position
        self.y = float(self.rect.y)
        self.centery = float(self.rect.centery)


    def update(self):
        # move alien up/down
        self.y += (self.ai_settings.boss_speed_factor * self.ai_settings.boss_direction)
        self.rect.y = self.y


        # Taken from https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame written by Ashish Nitin Patil

        def __init__(self, y):  # initial position
            self.y = y

        def move(self, speed=5):  # chase movement
            # Movement along y direction
            if self.y < py:
                self.y += speed
            elif self.y > py:
                self.y -= speed

    def check_edges(self):
        # return true if boss is at top/bottom of screen
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.top:
            return True
        elif self.rect.bottom <= 0:
            return True

    def blitme(self):
        # draw alien at its current location
        self.screen.blit(self.image, self.rect)