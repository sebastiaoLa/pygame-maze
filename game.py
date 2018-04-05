"""
mini game de um labirinto para posterior desenvolvimento de algoritimos geneticos e
algoritmos pathfind
"""

import pygame
from grid import Grid
from batch import Batch
from constants import FPS

pygame.init()
clock = pygame.time.Clock()

class Game(object):
    """ game class with all elements of the game"""
    def __init__(self):
        self.main_batch = Batch()
        self.grid = Grid(self.main_batch)
        self.display_surf = pygame.display.get_surface()
        

    def update(self):
        #players.update
        pass

    def draw(self):
        self.grid.draw(self.display_surf)

    def main_loop(self):
        while True:
            self.update()
            self.draw()
            pygame.display.update(self.main_batch)
            clock.tick(FPS)
