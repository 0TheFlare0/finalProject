import pygame

#This is adapted from Python Crash Course
class Ship():
    def __init__(self, screen):
        self.screen = screen
        
        #This will load the ship sprite and get its rect (or rectangle)
        self.image = pygame.image.load('image/Ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
       
        #This will tell where to start the each new ship
        self.rect.midleft = self.screen_rect.midleft
        
        #THis is the movement flag that will help the ship to move
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #This will update the ship's position based on the movement flag
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        #This code draws the ship at its current location on the screen
        self.screen.blit(self.image, self.rect)

    