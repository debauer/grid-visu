import time

import pygame
from pygame.surface import SurfaceType

from grid.base import GridBox, get_grid, create_grid
from grid.content import ContentImage
from misc.types import GridLayout, GridPosition
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, grid_layout

pygame.display.init()
pygame.font.init()
surface: SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
create_grid(surface, grid_layout)
GridBox(GridPosition(0, 0), GridLayout(4, 3), "audio")
camera_box = GridBox(GridPosition(6, 0), GridLayout(6, 3), "camera", )
GridBox(GridPosition(0, 3), GridLayout(1, 1), "1")
GridBox(GridPosition(1, 3), GridLayout(1, 1), "2")

cimage = ContentImage(camera_box)

lala = False
while True:
    if lala:
        cimage.load_image("img/example.jpg")
        lala = False
    else:
        cimage.load_image("img/example2.jpg")
        lala = True
    cimage.draw()
    get_grid().draw()
    pygame.display.flip()
    time.sleep(0.5)
