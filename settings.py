import pygame

class Settings():
    def __init__(self):
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = "image/Background.gif"
        #Ship settings
        self.ship_speed_factor = 2
        #Bullet Settings
        # self.laser_speed_factor = 1
        # self.laser_image = "image/Laser.gif"
        # self.laser_width = 3
        # self.laser_height = 15