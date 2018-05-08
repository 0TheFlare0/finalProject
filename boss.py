#adapted from cozort
import pygame
from pygame.sprite import Sprite
from settings import Settings

# a class to represent an enemy ship
class Boss(Sprite):
    def __init__(self, ai_settings, screen):
        # init the alien and set its starting pos
        super(Boss, self).__init__()
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

        #This is the movement flag that will help the ship to move by making it so that it is first false so that
        #will not move, but then moves when there is a key press event in game functions
        self.moving_up = False
        self.moving_down = False


    def update(self):
        # move alien up/down
        #self.y += (self.ai_settings.enemy_speed_factor * self.ai_settings.boss_direction)
        #self.rect.y = self.y
        
        #This will update the ship's position based on the movement flag
        #This will also now update so that it will limit the ship rect to the screen
        #Used this link to help find out what to type to make it so the ship is limited on the bottom and top of the screen as well
            #https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor


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