
from random import choice
from constants import CELLSIZE

class Cell(object):
    def __init__(self, index, batch=None):
        self.batch = batch
        self.randomize()
        self.walls = {}
        self.pos = [i*CELLSIZE for i in index]
        while False not in [self.walls[i] for i in self.walls]:
            self.randomize()
        self.draw = []
        self.build_draw()

    def randomize(self):
        self.walls['top'] = choice([True, False])
        self.walls['left'] = choice([True, False])
        self.walls['right'] = choice([True, False])
        self.walls['bottom'] = choice([True, False])

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

    def check(self,side):
        return not self.walls[side.lower()]
