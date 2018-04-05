
from pygame import draw, Rect, HWSURFACE
from pygame.surface import Surface

from cell import Cell
from constants import HEIGHT, WALLWIDTH, WHITE, WIDTH, RED, BLUE, CELLSIZE

POS_DICT = {
    'top': [0, -1],
    'left': [-1, 0],
    'right': [1, 0],
    'bottom': [0, 1]
}


def checkpos(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < WIDTH/CELLSIZE and pos[1] < HEIGHT/CELLSIZE


class Grid(object):
    def __init__(self, batch=None):
        self.batch = batch
        self.cells = []
        self.surface = None
        for i in range(0, (WIDTH/CELLSIZE)):
            line = []
            for j in range(0, (HEIGHT/CELLSIZE)):
                line.append(Cell((i, j)))
            self.cells.append(line)

    def build(self, disp):
        self.surface = Surface((WIDTH, HEIGHT), HWSURFACE)
        for line in self.cells:
            for cell in line:
                for wall in cell.draw:
                    draw.line(self.surface, WHITE, wall[0], wall[1], WALLWIDTH)
                # if cell.matrix_index == (0, 0):
                #     self.surface.fill(
                #         RED,
                #         Rect(
                #             cell.pos[0]+int(CELLSIZE*0.1),
                #             cell.pos[1]+int(CELLSIZE*0.1),
                #             int(CELLSIZE*0.8),
                #             int(CELLSIZE*0.8)
                #         )
                #     )
                # elif cell.matrix_index == (WIDTH/CELLSIZE-1, HEIGHT/CELLSIZE-1):
                #     self.surface.fill(
                #         BLUE,
                #         Rect(
                #             cell.pos[0]+int(CELLSIZE*0.1),
                #             cell.pos[1]+int(CELLSIZE*0.1),
                #             int(CELLSIZE*0.8),
                #             int(CELLSIZE*0.8)
                #         )
                #     )
        self.surface.convert(disp)

    def draw(self, disp):
        if not self.surface:
            self.build(disp)
        rect = self.surface.get_rect()
        rect.center = (WIDTH/2, HEIGHT/2)
        if self.batch:
            self.batch.add_to_batch(disp.blit(self.surface, rect))
            # self.batch.add_to_batch(disp.fill((0,0,0)))
        else:
            disp.blit(self.surface, rect)

    def get_cell(self, pos):
        if checkpos(pos):
            return self.cells[pos[0]][pos[1]]
        return None

    def get_adjacent_cells(self, pos):
        # for each key in pos_dict create a new key in cells with value equals to the cell in
        # that pos
        cells = {
            key: self.get_cell([x[0]+x[1] for x in zip(POS_DICT[key], pos)]) for key in POS_DICT
        }
        return cells
