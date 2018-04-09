
from pygame import draw
from constants import CELLSIZE, WIDTH, RED, DESTINY, COMPLEXITY_LEVEL


class Player(object):
    def __init__(self, pos, global_path=None, path=None, batch=None):
        self.pos = pos
        self.global_path = global_path if global_path else set()
        self.global_path.add(self.pos)
        self.path = list(path) if path else []
        self.path.append(self.pos)
        self.batch = batch
        self.children = []

    def pos_in_path(self, pos):
        return pos in self.global_path

        # for i in xrange(1, int(len(self.global_path)*COMPLEXITY_LEVEL)):
        #     if pos == self.global_path[(i*-1)]:
        #         return True
        # return False

        # for i in self.global_path[int(len(self.global_path)*(COMPLEXITY_LEVEL*0.5))*-1:][::-1]:
        #     if pos == i:
        #         return True
        # return False
        # return pos in self.global_path[int(len(self.global_path)*(COMPLEXITY_LEVEL*0.5))*-1:]

    def get_child(self, side):
        if side == 'top':
            if not self.pos_in_path((self.pos[0], self.pos[1]-1)):
                self.children.append(
                    Player((self.pos[0], self.pos[1]-1), self.global_path, self.path, self.batch))
        elif side == 'left':
            if not self.pos_in_path((self.pos[0]-1, self.pos[1])):
                self.children.append(
                    Player((self.pos[0]-1, self.pos[1]), self.global_path, self.path, self.batch))
        elif side == 'right':
            if not self.pos_in_path((self.pos[0]+1, self.pos[1])):
                self.children.append(
                    Player((self.pos[0]+1, self.pos[1]), self.global_path, self.path, self.batch))
        elif side == 'bottom':
            if not self.pos_in_path((self.pos[0], self.pos[1]+1)):
                self.children.append(
                    Player((self.pos[0], self.pos[1]+1), self.global_path, self.path, self.batch))

    def done(self):
        return self.pos in DESTINY

    def move(self, cells):
        for i in cells:
            self.get_child(i)
        return self.children

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
