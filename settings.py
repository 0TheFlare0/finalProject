import pygame

class Settings():
    def __init__(self):
        #Screen Settings
        self.screen_width = 900
        self.screen_height = 504
        self.bg_image = "image\Background.png"
        self.bg_color = (0, 0, 0)
        #Ship settings
        self.ship_speed_factor = .8
        #Bullet Settings
        self.laser_speed_factor = 1
        self.laser_image = "image/Laser.png"
        self.laser_width = 21
        self.laser_height = 21