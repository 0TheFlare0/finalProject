import pygame

class Boss():
  
  

#--------------------------


import sys, random, pygame
from pygame.locals import *
pygame.init()

WIDTH = 1200 #game window width
HEIGHT = 800 #game window height
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set the game window


#comes from cozort canvas
#bos dictionary
 player1 = {
'name': 'Boss',
'hitPoints': 300,
'alive':True
}

#https://stackoverflow.com/questions/30015787/random-movement-pygame
class Boss:
    def __init__(self):
        self.y = random.randrange(30, HEIGHT-30) #y position
        self.speed = random.randrange(1,4) #cell speed

    brick_tile = pygame.image.load('boss.png')


mainloop()
