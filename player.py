
from pygame import draw
from constants import CELLSIZE, WIDTH, RED, DESTINY


class Player(object):
    def __init__(self, pos, global_path=None, path=None, batch=None):
        self.pos = pos
        self.global_path = global_path if global_path else []
        self.global_path.append(self.pos)
        self.path = list(path) if path else []
        self.path.append(self.pos)
        self.batch = batch

    def pos_not_in_path(self,pos):
        return pos not in self.global_path[len(self.global_path)-200:]

    def get_child(self, side):
        if side == 'top':
            if self.pos_not_in_path((self.pos[0], self.pos[1]-1)):
                return Player((self.pos[0], self.pos[1]-1), self.global_path, self.path, self.batch)
        elif side == 'left':
            if self.pos_not_in_path((self.pos[0]-1, self.pos[1])):
                return Player((self.pos[0]-1, self.pos[1]), self.global_path, self.path, self.batch)
        elif side == 'right':
            if self.pos_not_in_path((self.pos[0]+1, self.pos[1])):
                return Player((self.pos[0]+1, self.pos[1]), self.global_path, self.path, self.batch)
        elif side == 'bottom':
            if self.pos_not_in_path((self.pos[0], self.pos[1]+1)):
                return Player((self.pos[0], self.pos[1]+1), self.global_path, self.path, self.batch)
        return None

    def done(self):
        return True in [self.pos[0] == i[0] and self.pos[1] == i[1] for i in DESTINY]

    def distance_to_destiny(self):
        return min([i[0]-self.pos[0]+i[1]-self.pos[1] for i in DESTINY])

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
        return [self]

    def draw_path(self):
        points = []
        for i in self.path:
            points.append([(x*CELLSIZE)+(CELLSIZE/2) for x in i])
        return points

    def draw_global_path(self):
        points = []
        for i in self.global_path:
            points.append([(x*CELLSIZE)+(CELLSIZE/2) for x in i])
        return points

    def get_color(self):
        # red = ((1-float(self.pos[0])/((WIDTH/CELLSIZE)-1))*(255-127))+127
        # blue = (float(self.pos[0])/((WIDTH/CELLSIZE)-1))*255
        # green = 0
        # red = 255-len(self.path) if 255-len(self.path)<255 and 255-len(self.path)>255 else 0
        # green = len(self.path)-255 if len(self.path)-255<255 and len(self.path)-255>0 else 0
        # blue = len(self.path) if len(self.path)<255 and len(self.path)>0 else 255
        # if (red,green,blue) == (0,0,0):
        #     return (255,255,255)
        # print (red,green,blue)
        # return (red,green,blue)
        return RED

    def draw(self, disp):
        if self.batch:
            self.batch.add_to_batch(
                draw.circle(
                    disp,
                    self.get_color(),
                    [(x*CELLSIZE)+(CELLSIZE/2) for x in self.pos],
                    CELLSIZE/3
                )
            )
        else:
            draw.circle(
                disp,
                self.get_color(),
                [(x*CELLSIZE)+(CELLSIZE/2) for x in self.pos],
                CELLSIZE/3
            )
