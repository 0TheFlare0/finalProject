<<<<<<< HEAD

=======
>>>>>>> 493aa6a820c6abe2b517b9e230a3054da0729afe
#Import libraries
import pygame
from pygame.sprite import Group
import game_functions as gf
from ship import Ship
from settings import Settings
from laser import Laser
from boss import Boss

'''
Code gotten and adapted from Eric Matthes Python Crash Course
This code was typed my Michael Davis
'''
#That runs the actual screen for the game
def run_game():
    #Creates a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Codetastrophe")
    #Make the ship
    ship = Ship(ai_settings, screen)    
    #Make a group to store lasers in
    lasers = Group()
    #b_lasers = Group()
    #Make a group to store boss
    boss = Boss(ai_settings, screen)
    #This will load the background image for the game
    #Instead of just a simple color background, we want to use an image. I learned this line of code from...
        #http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound
    pygame.image.load(ai_settings.bg_image)

    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, boss, lasers)
        ship.update()
        boss.update()
        gf.update_lasers(lasers)
        gf.update_boss(ai_settings, boss)
        gf.update_screen(ai_settings, screen, ship, boss, lasers)

run_game() 
