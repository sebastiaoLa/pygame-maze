
from random import randint
from constants import CELLSIZE, invert_side

def random():
    return randint(0, 2) < 1

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
        self.walls['top'] = random()
        self.walls['left'] = random()
        self.walls['right'] = random()
        self.walls['bottom'] = random()

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
