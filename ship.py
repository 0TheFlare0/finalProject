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
        self.rect.midleft= self.screen_rect.midleft
    def blitme(self):
        #This code draws the ship at its current location on the screen
        self.screen.blit(self.image, self.rect)

    