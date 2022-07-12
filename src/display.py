import pygame
from pygame import surface

from grid.base import GridBox, Grid
from grid.content import ContentList
from misc.types import Coordinate, GridLayout, GridPosition
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, grid_layout

pygame.init()
screen: surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
grid = Grid(screen, grid_layout)
audio = grid.add_box("audio", GridPosition(0, 0), GridLayout(4, 3))
grid.add_box("camera", GridPosition(6, 0), GridLayout(6, 3))
grid.add_box("lala", GridPosition(0, 3), GridLayout(1, 1))
grid.add_box("lulu", GridPosition(1, 3), GridLayout(1, 1))
grid.draw()

pygame.display.flip()
while True:
    pass
