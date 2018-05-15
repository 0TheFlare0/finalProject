## Chaos In Space
___________
## Overview
> Traveling through the dark galaxy, scavenging for rare Obsilatal DiHidralate. While searching on the outer layer of planet Obenite, home of Mystic Watcher, a disturbance took place on the final dive, awakening the beast from his sleep. Find a way out, or face the same fate that so many have gone through.

## Introduction
> Creating an interactive game that lets you go up against an AI. Challenges the mind to strategize and plan ahead in real world scenarios. This game provides a fun and easy way to both play a side scroll shooter game and easily learn about all the different aspects of what goes into a PyGame.

## Code Samples
 #Helps in moving the ship up (modified to use WASD)
    #https://www.pygame.org/docs/ref/key.html
def check_keydown_event(event, ship):
    if event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True

## Contributors
> Michael Davis-the creator of the main charecter and its shooting charecteristics.
> Aaron Ballard- The artistic designer for all sprites and backgrounds, designer and creator of the boss and all its AI functions.
> Mr. Cozort- His face for the boss as well as his generous help at guiding us through this project.

## Installation
> To run the game, first make sure you are running Python 3.6. You should also have PyGame installed on your computer before running. From there, open up "Main.py" and click run. The game should load up, and let you play!

## Progress week 1-7
> Week 1- gathering similar project ideas to look at and use as guidelines.
>         creating sprites for the boss, background, ship, bullets, and laser.
>
> Week 2- Reading over Pygame crash course for similar project guidelines.
>         adjusting sizes of sprites.
>         putting in firt lines of code.
>
> Week 3- Getting git hub to work and allow pulling from the application.
>         Getting py-game to work on a mac.
>         laying out all aspects of what will be going into the game.
>
> Week 4- Getting Main ship to load onto screen with hit boxes.
>         Gettign boss to load onto the screen.
>
> Week 5- Allowing Main ship to move on screen with W-A-S-D Keys.
>         Allowing Main ship to fire around.
>         Making ship shoot to the right.
>         Allowing boss to follow main charecter in y axis.
>
> Week 6- Making the Main ship and Boss have broders to not let them go off the screen.
>         Firing sprites instead of lines.
>         Making the bullets dissapear after fired.
>         Making boss shoot out the eyes.
>         Changing boss to go just up and down.
>         Getting boss its hit markers.
>
> Week 7- Removing all un-necessary lines of code that slow game  down.
>         Move all sprites to one to add background.
>         Working out background to be able to run.
>         testing out score keeper/ lives/ timer/ increasing speed/ increasing power

## In Depth Breakdown
> Week12: We added the sprites that we made into the the settings.py as well as 
> ship.py. We also added fixed some miss understandings of Python Crash Course 
> with the code that is in ship.py as well as settings.py. We also tried figuring out how GitHub works
> and how to have it so files will sync between Visual Studio Code and GitHub

> Week13: We added more sprites into the image folder and converted them into PNG images. We also found out and
> succesfully found out how to sync Visual Studio Code with so that when we update the code within Visual Studio
> Code, it automatically updates in GitHub. We also tried to fixe the problem with the screen and images not
> displaying by using the pygame.image.load() line of code. We then started on making it so the ship can actually
> move

> Week14: We were successful in making the ship actually move and now it can also move with WASD instead of the
> arrow keys. We also made it so the ship now has boarders so that it can not move outside the boarder.

> Week15: We were successful in making the ship shoot a limited ammount of bullets as well as started to figure
> out how to put in the boss into the already almost done code files like main and game_functions. Stil working
> on getting the background to work with us 

> Week16: We are currently implimenting the boss into the game. We have the boss appear on screen as well as move,
> but it currently has now borders, so it just flys of screen
>    Now the Boss.png does not even load on screen
> '''

## Sources
> https://www.pygame.org/docs/ref/key.html
> http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound
> https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/Documents/Forms/All.aspx?slrid=c4d2659e-a009-5000-c17b-e7436e6e6a4c&RootFolder=%2Fpersonal%2Fccozort_bcp_org%2FDocuments%2F02_Computer%20Science%2FIntro%20to%20Programming%2Fcozort_chris&FolderCTID=0x0120008A1882DAC829A044BA12245B991DC6B8
> https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame written by Ashish Nitin Patil
> https://Facebook.com
> Pygame crash course
> http://kidscancode.org/
