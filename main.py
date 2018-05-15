#Aaron & I will be working on making a side scroller shooter boss fight with a ship shooting lasers and maybe power ups
    #A very simple vision of what our game will look like (but in space with other different things)
        #https://www.youtube.com/watch?v=UxcCoDlnqr4
#Our first major milestone would be to make a working ship that can move and shoot the laser
#I will need to learn how to use pygame's formating and library with what know on classes to make the code
#My project might to ambitious in that the power ups might take more time then expected to make and the boss might be too difficult to make intresting and fun
#I don't see that there are many parts to this project that are not ambitious enough
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Link to the Github
    #https://github.com/0TheFlare0/finalProject.git

'''

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

    #Start the main loop for the game'
    while True:
        gf.check_events(ai_settings, screen, ship, boss, lasers)
        ship.update()
        boss.update()
        gf.update_lasers(lasers)
        gf.update_boss(ai_settings, boss)

        gf.update_screen(ai_settings, screen, ship, boss, lasers)

run_game() 
