"""
mini game de um labirinto para posterior desenvolvimento de algoritimos geneticos e
algoritmos pathfind
"""
import sys
from threading import Thread

import pygame
from pygame.constants import QUIT, KEYUP, K_p, K_1, K_2, K_3, K_PLUS, K_MINUS, K_r, K_f

from batch import Batch
from constants import FPS, WIDTH, HEIGHT, GREEN, WALLWIDTH, CELLSIZE, RED, BLUE
from grid import Grid
from player import Player

pygame.init()
CLOCK = pygame.time.Clock()


def sair():
    sys.exit()
    pygame.quit()
    exit()


class Game(object):
    """ game class with all elements of the game"""

    def __init__(self):
        self.fps = FPS
        self.show_player = True
        self.main_batch = Batch()
        self.grid = Grid(self.main_batch)
        self.display_surf = pygame.display.set_mode(
            (WIDTH, HEIGHT),
            pygame.HWSURFACE  # |pygame.DOUBLEBUF
        )
        self.players = [Player((0, 0), batch=self.main_batch)]
        for i in range(1, HEIGHT/CELLSIZE):
            self.players.append(
                Player(
                    (0, i),
                    global_path=self.players[0].global_path,
                    batch=self.main_batch
                )
            )
        self.player_done = None
        self.do_once = False
        pygame.display.set_caption('Carregando labirinto')

    def restart(self):
        pygame.display.set_caption('Carregando labirinto')
        self.grid = Grid(self.main_batch)
        self.players = [Player((0, 0), batch=self.main_batch)]
        for i in range(1, HEIGHT/CELLSIZE):
            self.players.append(
                Player(
                    (0, i),
                    global_path=self.players[0].global_path,
                    batch=self.main_batch
                )
            )
        self.player_done = None
        self.do_once = False

    def check(self):
        self.player_done = self.get_done()

    def update(self):
        children = []
        for i in self.players:
            children += i.move(
                self.grid.get_cell(i.pos),
                self.grid.get_adjacent_cells(i.pos)
            )
        self.players = children
        if not self.players:
            self.restart()

    def get_done(self):
        if self.player_done:
            return self.player_done
        for i in self.players:
            if i.done():
                self.player_done = i
                return i
        return None

    def draw(self):
        self.grid.draw(self.display_surf)
        if self.show_player:
            if not self.player_done:
                for i in self.players:
                    i.draw(self.display_surf)
            else:
                self.main_batch.add_to_batch(
                    pygame.draw.lines(
                        self.display_surf,
                        GREEN,
                        False,
                        self.player_done.draw_path(),
                        WALLWIDTH
                    )
                )
        if self.player_done:
            self.main_batch.add_to_batch([
                self.display_surf.fill(
                    RED,
                    pygame.Rect(
                        self.grid.get_cell(
                            self.player_done.path[0]).pos[0]+int(CELLSIZE*0.1),
                        self.grid.get_cell(
                            self.player_done.path[0]).pos[1]+int(CELLSIZE*0.1),
                        int(CELLSIZE*0.8),
                        int(CELLSIZE*0.8)
                    )
                ),
                self.display_surf.fill(
                    BLUE,
                    pygame.Rect(
                        self.grid.get_cell(
                            self.player_done.path[-1]).pos[0]+int(CELLSIZE*0.1),
                        self.grid.get_cell(
                            self.player_done.path[-1]).pos[1]+int(CELLSIZE*0.1),
                        int(CELLSIZE*0.8),
                        int(CELLSIZE*0.8)
                    )
                )
            ])

    def main_loop(self):
        while True:
            if not self.player_done:
                self.update()
                self.check()
            elif not self.do_once:
                pygame.display.set_caption('Done!')
            for event in pygame.event.get():
                if event.type == QUIT:
                    sair()
                if event.type == KEYUP:
                    if event.key == K_p:
                        self.show_player = not self.show_player
                    elif event.key == K_1:
                        self.fps = 5
                    elif event.key == K_f:
                        pygame.display.toggle_fullscreen()
                    elif event.key == K_2:
                        self.fps = 15
                    elif event.key == K_3:
                        self.fps = 60
                    elif event.key == K_r:
                        self.restart()
                    elif event.key == K_MINUS:
                        if self.fps > 5:
                            self.fps -= 5
                        if self.fps <= 0:
                            self.fps = 1
                    elif event.key == K_PLUS:
                        if self.fps <= 55:
                            self.fps += 5
                        if self.fps > 60:
                            self.fps = 60
            self.draw()
            pygame.display.update(self.main_batch.draw())
            print CLOCK.get_fps()
            CLOCK.tick(self.fps)


GAME = Game()
GAME.main_loop()
