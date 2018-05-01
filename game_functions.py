import sys
import pygame
from laser import Laser

#Code gotten from Python Crash Course

#Helps in moving the ship up (modified to use WASD)
#It also helps in dectecting if the kay is pressed or not for WASD or the space bar
    #https://www.pygame.org/docs/ref/key.html
def check_keydown_event(event, ai_settings, screen, ship, laser):
    if event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Create a new bullet and add it to the bullet group
        new_laser = Laser(ai_settings, screen, ship)
        laser.add(new_laser)

def check_keyup_event(event, ship):
    if event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False
    elif event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, laser):
    #Responds to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event (event, ai_settings, screen, ship, laser)
        elif event.type == pygame.KEYUP:
            check_keyup_event (event, ship)

#This will update images on screen and flip to the new screen
def update_screen(ai_settings, screen, ship, laser):
    #This will redraw the screen for each loop (which is the ship and later the boss and lasers)
    screen.fill(ai_settings.bg_color)
    #Redraw all lasers behind ship and boss
    for laser in laser.sprites():
        laser.blitme()

    ship.blitme()
    
    #Makes the most recently drawn screen visible
    pygame.display.flip()