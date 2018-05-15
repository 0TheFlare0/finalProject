<<<<<<< HEAD
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
displaying by using the pygame.image.load() line of code. We then started on making it so the ship can actually
move

Week14: We were successful in making the ship actually move and now it can also move with WASD instead of the
arrow keys. We also made it so the ship now has boarders so that it can not move outside the boarder.

Week15: We were successful in making the ship shoot a limited ammount of bullets as well as started to figure
out how to put in the boss into the already almost done code files like main and game_functions. Stil working
on getting the background to work with us 

Week16: We are currently implimenting the boss into the game. We have the boss appear on screen as well as move,
but it currently has now borders, so it just flys of screen

Week17: The boss now blits on screen as well as now moves up and down on screen by itself. The only issue is that
now the the pygame.display.flip is not updating the screen properly, so it is making a streak of past blited images
, like a paint brush
'''

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
