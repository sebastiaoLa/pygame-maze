
from pygame import draw, HWSURFACE, Rect
from pygame.surface import Surface

from cell import Cell
from constants import HEIGHT, WALLWIDTH, WHITE, WIDTH, GRID_SET


def checkpos(pos):
    return pos in GRID_SET
    # return pos[0] >= 0 and pos[1] >= 0 and pos[0] < WIDTH/CELLSIZE and pos[1] < HEIGHT/CELLSIZE


class Grid(object):
    def __init__(self, batch=None):
        self.batch = batch
        self.cells = {}
        self.cells_draw = []
        self.surface = None
        for x, y in GRID_SET:
            cell = Cell((x, y))
            self.cells[(x, y)] = cell
            self.cells_draw += cell.draw

    def build(self, disp):
        self.surface = Surface((WIDTH, HEIGHT), HWSURFACE)
        draw.rect(
            self.surface,
            WHITE,
            Rect(
                0,
                0,
                WIDTH-WALLWIDTH,
                HEIGHT-WALLWIDTH
            ),
            WALLWIDTH
        )
        for wall in self.cells_draw:
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
            return self.cells[pos]
        return None

    def get_accessible_cells(self, pos):
        # for each key in pos_dict create a new key in cells with value equals to the cell in
        # that pos
        actual_cell = self.get_cell(pos)
        pos_dict = {
            'top': [0, -1],
            'left': [-1, 0],
            'right': [1, 0],
            'bottom': [0, 1]
        }
        cells = {}
        for i in pos_dict:
            test_cell = self.get_cell((
                pos[0]+pos_dict[i][0],
                pos[1]+pos_dict[i][1]
            ))
            if test_cell:
                if test_cell.check_enter(i) and actual_cell.check_leave(i):
                    cells[i] = test_cell

        return cells
