import sys
import pygame
from laser import Laser
from boss_laser import BossLaser

#Code gotten from Python Crash Course

#Helps in moving the ship up (modified to use WASD)
#It also helps in dectecting if the kay is pressed or not for WASD or the space bar
    #https://www.pygame.org/docs/ref/key.html
def check_keydown_event(event, ai_settings, screen, ship, boss, lasers):
    if event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_laser(ai_settings, screen, ship, lasers)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def fire_laser(ai_settings, screen, ship, lasers):
    #Fires lasers if limit not reached yet
    #Create a new bullet and add it to the bullet group
    if len(lasers) < ai_settings.lasers_allowed:
        new_laser = Laser(ai_settings, screen, ship)
        lasers.add(new_laser)

def fire_boss_laser(ai_settings, screen, boss, b_lasers):
    if len(b_lasers) < ai_settings.b_laser_allowed:
        new_b_laser = BossLaser(ai_settings, screen, boss)
        b_lasers.add(new_b_laser)


def check_keyup_event(event, ship, boss):
    if event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False
    elif event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        boss.moving_up = False
    elif event.key == pygame.K_s:
        boss.moving_down = False

def check_events(ai_settings, screen, ship, boss, lasers, b_lasers):
    #Responds to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event (event, ai_settings, screen, ship, boss, lasers)
        elif event.type == pygame.KEYUP:
            check_keyup_event (event, ship, boss)

#This will update images on screen and flip to the new screen
def update_screen(ai_settings, screen, ship, boss, lasers, b_lasers):
    #This will redraw the screen for each loop (which is the ship and later the boss and lasers)
    screen.fill(ai_settings.bg_color)
    #screen.blit(ai_settings.bg_image)
    #Redraw all lasers behind ship and boss
    for laser in lasers.sprites():
        laser.blitme()

    ship.blitme()

    boss.blitme()
    
    #Makes the most recently drawn screen visible
    pygame.display.flip()

def update_lasers(lasers):
    #Updates the bullet postion and gets rid of the old bullets off screen
    lasers.update()

    #Get rid of lasers that have disappeared
    for laser in lasers.copy():
        if laser.rect.left >= 900:
            lasers.remove(laser)
    #print(len(lasers))

def update_b_lasers(b_lasers):
    b_lasers.update()

    for b_laser in b_lasers.copy():
        if b_laser.rect.right <= 0:
            b_lasers.remove(b_laser)