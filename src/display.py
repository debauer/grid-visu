import time

import pygame
from pygame.surface import SurfaceType
from pygame.time import get_ticks

from grid.base import GridBox, get_grid, create_grid, GridBoxBase
from grid.content import ContentValue, ContentImages, ContentBase, ContentVideo
from misc.registry import get_nodes
from misc.types import GridLayout, GridPosition
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, grid_layout

pygame.display.init()
pygame.font.init()
surface: SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
create_grid(surface, grid_layout)

#GridBox(GridPosition(0, 0), GridLayout(4, 3), name="audio")
GridBox(GridPosition(6, 0), GridLayout(6, 3), name="camera", )
GridBox(GridPosition(6, 3), GridLayout(6, 3), name="galerie", )
GridBox(GridPosition(0, 0), GridLayout(6, 3), name="camera2", )
GridBox(GridPosition(0, 3), GridLayout(6, 3), name="camera3", )
#GridBox(GridPosition(0, 3), GridLayout(1, 1), name="co2")
#GridBox(GridPosition(1, 3), GridLayout(2, 1))

#ContentValue(box_name="co2", value=499.2)
#ContentVideo(box_name="galerie", video_link="img/big_buck_bunny_480p_1mb.mp4")
ContentImages(box_name="galerie", image_links=["img/example.jpg", "img/example2.jpg"])
ContentVideo(box_name="camera", video_link="img/big_buck_bunny_480p_1mb.mp4")
ContentVideo(box_name="camera2", video_link="img/big_buck_bunny_480p_1mb.mp4")
ContentVideo(box_name="camera3", video_link="img/big_buck_bunny_480p_1mb.mp4")

info = pygame.display.Info()
ticks = get_ticks()
perf = time.perf_counter()

while True:
    get_grid().draw()
    for node in get_nodes(ContentBase):
        node.draw()
    pygame.display.update()
    t = get_ticks()
    p = time.perf_counter()
    #print(f"tick: {t - ticks}")
    #print(f"perf: {p - perf}")
    #print(f"{get_nodes(ContentBase)}")
    ticks = t
    perf = p
    time.sleep(0.001)
