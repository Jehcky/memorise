import pygame
import random
import time

screen = pygame.display.set_mode((800,600))

def main():
    pygame.init()
    
    pygame.display.set_caption("Memorise")
    w_surface = pygame.display.get_surface() 
    game = Game(w_surface)
    game.play()
    pygame.quit()

class Game:
    def __init__(self, surface):
        pass
    def update(self):
        pass
    def play(self):
        pass

class Tile:

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
        screen.blit(pygame.image.load(self.imagelist),(self.pos_x,self.pos_y))

if __name__ == "__main__":
    main()