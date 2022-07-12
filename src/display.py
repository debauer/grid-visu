import time

import pygame
from pygame.surface import SurfaceType
from pygame.time import get_ticks

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

c1image = ContentImage(camera_box)
c2image = ContentImage(camera_box)
c1image.load_image("img/example.jpg")
c2image.load_image("img/example2.jpg")

lala = False
ticks = get_ticks()
perf = time.perf_counter()
while True:
    if lala:
        lala = False
        c1image.draw()
    else:
        lala = True
        c2image.draw()
    get_grid().draw()
    pygame.display.flip()
    t = get_ticks()
    p = time.perf_counter()
    print(f"tick: {t - ticks}")
    print(f"perf: {p - perf}")
    ticks = t
    perf = p
