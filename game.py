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

    
    game_menu()

    # Infinite loop 'til user choose to quit the game
    while (True):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                game_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print()


            
def options_menu():
    print("This is here so I don't get an error")

def game_menu():
    
    # Loads an image and put is on screen 
    intro_img = pygame.image.load(os.path.join('img','intro.png'))
    screen.blit(intro_img,(80,60))

    # Loads a text with the specified color and puts it on screen
    # Each group of elements is an item of the game menu
    color_white = (255,255,255)

    font_small = pygame.font.SysFont("Corbel", 35)
    text = font_small.render('Start', True, color_white)
    screen.blit(text, (340,300))

    font_small = pygame.font.SysFont("Corbel", 35)
    text = font_small.render('Options', True, color_white)
    screen.blit(text, (320,380))

    font_small = pygame.font.SysFont("Corbel", 35)
    text = font_small.render('Quit', True, color_white)
    screen.blit(text, (340,460))

    pygame.display.update()

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

