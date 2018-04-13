import pygame
from pygame.sprites import Sprite

#Laser is subclass and Sprite is a superclass (Code from Python Crash Course)
class Laser(Sprite):
    # class to manage lasers(or bullets)
    def __init__ (self, ai_settings, screen, ship):
        #Create a laser object at the ship's current postion
        super(Laser, self).__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) and then set the current postion
        self.rect = pygame.Rect(0, 0, ai_settings.laser_width,
            ai_settings.laser_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.right = ship.rect.right

        #Store the laser's postion as a decimal value
        self.y =float(self.rect.y)

        self.image = ai_settings.laser.image
        self.speed_factor = ai_settings.laser_speed_factor

def update(self):
    #Move bullet through the screen
    #Update the decimal postion of the laser
    self.y -= self.speed_factor
    #Update the rect postion
    self.rect.y = self.y

def draw_bullet(self):
    #Draw the bullet to the screen (replace self.color with self.image since we are using an image an not just a color)
    pygame.draw.rect(self.screen, self.image, self.rect)


