import pygame
from pygame.sprite import Sprite
from boss import Boss
#This code was typed by Aaron and Mike
#Laser is subclass and Sprite is a superclass (Code from Python Crash Course)
class BossLaser(Sprite):
    # class to manage lasers(or bullets)
    def __init__ (self, ai_settings, screen, boss):
        #Create a laser object at the ship's current postion
        super(BossLaser, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("Red_laser.png")

        #Create a bullet rect at (0,0) and then set the current postion
        #self.rect = pygame.Rect(0, 0, ai_settings.laser_width,
        #    ai_settings.laser_height)
        self.rect = self.image.get_rect()
        self.rect.centerx = boss.rect.centerx
        self.rect.centery = boss.rect.centery
        self.rect.left = boss.rect.left

        #Store the laser's postion as a decimal value
        self.x =float(self.rect.x)
        self.y = float(self.rect.y)

        #self.image = ai_settings.laser_image
        self.speed_factor = ai_settings.laser_speed_factor

    def update(self):
        #Move bullet through the screen
        #Update the decimal postion of the laser
        self.x += self.speed_factor
        #Update the rect postion
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        #Draw the bullet to the screen (replace self.color with self.image since we are using an image an not just a color)
        #Thanks to help from Mr. Cozart in helping making it so that it can load an image instead of loading a color
        #pygame.draw.rect(self.screen, self.image, self.rect)
        self.screen.blit(self.image, self.rect)
