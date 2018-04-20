#Me and Aaron will be working on making a side scroller shooter boss fight with a ship shooting lasers and maybe power ups
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
Week12: We added the sprites that we made into the the settings.py as well as 
ship.py. We also added fixed some miss understandings of Python Crash Course 
with the code that is in ship.py as well as settings.py. We also tried figuring out how GitHub works
and how to have it so files will sync between Visual Studio Code and GitHub

Week13: We added more sprites into the image folder and converted them into PNG images. We also found out and
succesfully found out how to sync Visual Studio Code with so that when we update the code within Visual Studio
Code, it automatically updates in GitHub. We also tried to fixe the problem with the screen and images not
displaying by using the pygame.image.load() line of code
'''

#Import libraries
import pygame
import game_functions as gf
from ship import Ship
from settings import Settings

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
    pygame.display.set_caption("Space Shooter")

    #Make the ship
    ship = Ship(screen)
    #This will load the background image for the game
    #Instead of just a simple color background, we want to use an image. I learned this line of code from...
        #http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound
    pygame.image.load(ai_settings.bg_image)

    #Start the main loop for the game
    while True:
        gf.check_events()

        
        #This will redraw the screen for each loop (which is the ship and later the boss and lasers)
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Makes the most recently drawn screen visible
        pygame.display.flip()

run_game()