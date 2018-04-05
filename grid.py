
from constants import WIDTH, HEIGHT, WHITE, WALLWIDTH
from cell import Cell
from pygame import draw
from pygame.surface import Surface
from pygame.locals import HWSURFACE


class Grid(object):
    def __init__(self, batch=None):
        self.batch = batch
        self.cells = []
        self.surface = None
        for i in range(0, (WIDTH/10)):
            for j in range(0, (HEIGHT/10)):
                self.cells.append(Cell((i, j), self.batch))

    def build(self,disp):
        self.surface = Surface((WIDTH,HEIGHT),HWSURFACE)
        for cell in self.cells:
            for wall in cell.draw:
                draw.line(self.surface, WHITE, wall[0], wall[1], WALLWIDTH)
        self.surface.convert(disp)

    def draw(self, disp):
        if not self.surface:
            self.build(disp)
        rect = self.surface.get_rect()
        rect.center = (WIDTH/2,HEIGHT/2)
        if self.batch:
            self.batch.add_to_batch(disp(self.surface, rect))
        else:
            disp.blit(self.surface, rect)
