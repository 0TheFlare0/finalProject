import sys
import pygame

#Code gotten from Python Crash Course
def check_events(ship):
    #Responds to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #Helps in moving the ship up (modified to use WASD)
        #https://www.pygame.org/docs/ref/key.html
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ship.moving_up = True
            elif event.key == pygame.K_s:
                ship.moving_down = True
            elif event.key == pygame.K_d:
                ship.moving_right = True
            elif event.key == pygame.K_a:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                ship.moving_up = False
            elif event.key == pygame.K_s:
                ship.moving_down = False
            elif event.key == pygame.K_d:
                ship.moving_right = False
            elif event.key == pygame.K_a:
                ship.moving_left = False

#This will update images on screen and flip to the new screen
def update_screen(ai_settings, screen, ship):
    #This will redraw the screen for each loop (which is the ship and later the boss and lasers)
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #Makes the most recently drawn screen visible
    pygame.display.flip()