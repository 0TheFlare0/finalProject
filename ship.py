import pygame
from settings import Settings

#This is adapted from Python Crash Course
class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        
        #This will load the ship sprite and get its rect (or rectangle)
        self.image = pygame.image.load('image/Ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
       
        #This will tell where to start the each new ship
        self.rect.midleft = self.screen_rect.midleft

        #This will store the decimal values for the ship's centerx and centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #This is the movement flag that will help the ship to move by making it so that it is first false so that
        #will not move, but then moves when there is a key press event in game functions
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #This will update the ship's position based on the movement flag
        #This will also now update so that it will limit the ship rect to the screen
        #Used this link to help find out what to type to make it so the ship is limited on the bottom and top of the screen as well
            #https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        
        #Updates rect (rectangle) object from self.center x and y
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        #This code draws the ship at its current location on the screen
        self.screen.blit(self.image, self.rect)

    