#Me and Aaron will be working on making a side scroller shooter boss fight with a ship shooting lasers and maybe power ups
    #A very simple vision of what our game will look like (but in space with other different things)
        #https://www.youtube.com/watch?v=UxcCoDlnqr4
#Our first major milestone would be to make a working ship that can move and shoot the laser
#I will need to learn how to use pygame's formating and library with what know on classes to make the code
#My project might to ambitious in that the power ups might take more time then expected to make and the boss might be too difficult to make intresting and fun
#I don't see that there are many parts to this project that are not ambitious enough
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Import libraries
import pygame
import sys
from ship import Ship
from settings import Settings

'''
Week12: We added the sprites that we made into the the settings.py as well as 
ship.py. We also added fixed some miss understandings of Python Crash Course 
with the code that is in ship.py as well as settings.py. We alsp tried figuring out how GitHub works
and how to have it so files will sync between Visual Studio Code and GitHub
'''

#Code gotten from Python Crash Course that runs the actual screen for the game
def run_game():
    #Creates a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Shooter")

    #Make the ship
    ship = Ship(screen)

    #Start the main loop for the game
    while True:
        screen.fill(ai_settings.bg_image)

        #This code makes it watch for keyboard presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #This will redraw the screen for each loop
        screen.fill(ai_settings.bg_image)
        ship.blitme()

        #Makes the most recently drawn screen visible
        pygame.display.flip()

run_game()