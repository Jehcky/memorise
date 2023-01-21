import pygame
import random
#import time
import sys
import os

screen = pygame.display.set_mode((800,600))

def main():
    pygame.init()
    window_size = window_width, window_height = 800, 600
    pygame.display.set_caption("Memorise")
    intro_img = pygame.image.load(os.path.join('img','intro.png'))
    screen.blit(intro_img,(80,60))
    pygame.display.flip()

    # Infinite loop 'til user choose to quit the game
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

class Memorise:
    def __init__(self, surface):
        print("This is here so I don't get an error")

if __name__ == "__main__":
    main()

'''class Tile:

    def __init__(self, pos_x, pos_y, tile_x, tile_y, imagelist, surface):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.numx = tile_x
        self.numy = tile_y
        self.imagelist = imagelist
        self.surface = surface

    @classmethod
    def set_surface(cls, surface):
        cls.surface = surface

    def draw(self):
        x = 0
        y = 0
        screen.blit(pygame.image.load(self.imagelist),(self.pos_x,self.pos_y))'''

