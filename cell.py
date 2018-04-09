
from constants import CELLSIZE, COMPLEXITY_LEVEL
from random import random


def invert_side(side):
    if side == 'top':
        return 'bottom'
    elif side == 'right':
        return 'left'
    elif side == 'left':
        return 'right'
    elif side == 'bottom':
        return 'top'
    return None


def cell_random():
    return random() < COMPLEXITY_LEVEL


class Cell(object):
    def __init__(self, matrix_index):
        self.walls = {}
        self.randomize()
        self.matrix_index = matrix_index
        self.pos = [i*CELLSIZE for i in self.matrix_index]
        while False not in [self.walls[i] for i in self.walls]:
            self.randomize()
        self.draw = []
        self.build_draw()

    def randomize(self):
        self.walls['top'] = cell_random()
        self.walls['left'] = cell_random()
        self.walls['right'] = cell_random()
        self.walls['bottom'] = cell_random()

    def build_draw(self):
        if self.walls['top']:
            self.draw.append(
                [
                    (self.pos[0], self.pos[1]),
                    (self.pos[0]+CELLSIZE, self.pos[1])
                ]
            )

        if self.walls['bottom']:
            self.draw.append(
                [
                    (self.pos[0], self.pos[1]+CELLSIZE),
                    (self.pos[0]+CELLSIZE, self.pos[1]+CELLSIZE)
                ]
            )

        if self.walls['left']:
            self.draw.append(
                [
                    (self.pos[0], self.pos[1]),
                    (self.pos[0], self.pos[1]+CELLSIZE)
                ]
            )

        if self.walls['right']:
            self.draw.append(
                [
                    (self.pos[0]+CELLSIZE, self.pos[1]),
                    (self.pos[0]+CELLSIZE, self.pos[1]+CELLSIZE)
                ]
            )

    def check_leave(self, side):
        return not self.walls[side.lower()]

    def check_enter(self, side):
        return not self.walls[invert_side(side.lower())]
