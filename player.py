
from pygame import draw
from random import randint
from constants import CELLSIZE, WHITE, WIDTH, HEIGHT


class Player(object):
    def __init__(self, pos, global_path=None, path=None, batch=None):
        self.pos = pos
        self.global_path = global_path if global_path else []
        self.global_path.append(self.pos)
        self.path = list(path) if path else []
        self.path.append(self.pos)
        self.batch = batch

    def get_child(self, side):
        if side == 'top':
            if (self.pos[0], self.pos[1]-1) not in self.global_path:
                return Player((self.pos[0], self.pos[1]-1), self.global_path, self.path, self.batch)
        elif side == 'left':
            if (self.pos[0]-1, self.pos[1]) not in self.global_path:
                return Player((self.pos[0]-1, self.pos[1]), self.global_path, self.path, self.batch)
        elif side == 'right':
            if (self.pos[0]+1, self.pos[1]) not in self.global_path:
                return Player((self.pos[0]+1, self.pos[1]), self.global_path, self.path, self.batch)
        elif side == 'bottom':
            if (self.pos[0], self.pos[1]+1) not in self.global_path:
                return Player((self.pos[0], self.pos[1]+1), self.global_path, self.path, self.batch)
        return None

    def done(self):
        return self.pos[0] == (WIDTH/CELLSIZE)-1 #and self.pos[1] == (HEIGHT/CELLSIZE)-1

    def move(self, cell, cells):
        if not self.done():
            children = []
            for i in ['top', 'left', 'right', 'bottom']:
                if cell.check_leave(i):
                    if cells[i]:
                        if cells[i].check_enter(i):
                            child = self.get_child(i)
                            if child:
                                children.append(child)
            return children
        else:
            return [self]

    def draw_path(self):
        points = []
        for i in self.path:
            points.append([(x*CELLSIZE)+(CELLSIZE/2) for x in i])
        return points

    def get_color(self):
        red = (1-float(self.pos[0])/((WIDTH/CELLSIZE)-1))*255
        blue = (float(self.pos[0])/((WIDTH/CELLSIZE)-1))*255
        return (red,0,blue)

    def draw(self, disp):
        if self.batch:
            self.batch.add_to_batch(
                draw.circle(
                    disp,
                    self.get_color(),
                    [(x*CELLSIZE)+(CELLSIZE/2) for x in self.pos],
                    CELLSIZE/4
                )
            )
        else:
            draw.circle(
                disp,
                self.get_color(),
                [(x*CELLSIZE)+(CELLSIZE/2) for x in self.pos],
                CELLSIZE/6
            )
