
FULLSCREEN = True

if FULLSCREEN:
    import pygame
    # SCREEN SIZE
    pygame.display.init()
    SCREEN = pygame.display.Info()
    WIDTH = int(SCREEN.current_w*0.9)
    HEIGHT = int(SCREEN.current_h*0.9)
else:
    WIDTH = 800
    HEIGHT = 600

# consts :
#	COLORS
RED = (255, 000, 000)
GREEN = (000, 255, 000)
BLUE = (000, 000, 255)
WHITE = (255, 255, 255)
BLACK = (000, 000, 000)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
PINK = (248, 24, 148)

FPS = 60

WALLWIDTH = 4
CELLSIZE = 20


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
