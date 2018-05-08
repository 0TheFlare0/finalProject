import pygame

class Settings():
    def __init__(self):
        #Screen Settings
        self.screen_width = 900
        self.screen_height = 504
        self.bg_image = "Background.png"
        self.bg_color = (0, 0, 0)
        #Ship settings
        self.ship_speed_factor = 1
        #Bullet Settings
        self.laser_speed_factor = 6
        self.laser_image = "Laser.png"
        self.laser_width = 21
        self.laser_height = 21
        self.lasers_allowed = 8
        #Boss Settings
        self.boss_speed_factor = 3
        self.boss_drop_speed = 10
        self.boss_direction = 