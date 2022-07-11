import pygame
from pygame import surface

from grid.base import Coordinate, GridBox
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_DIM_X, GRID_DIM_Y, GRID_HEIGHT

pygame.init()
screen: surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
boxes = []
for x in range(GRID_DIM_X):
    for y in range(GRID_DIM_Y):
        GRID_WIDTH = SCREEN_WIDTH / GRID_DIM_X
        boxes.append(GridBox(screen, Coordinate(GRID_WIDTH * x, GRID_HEIGHT * y), name=f"{x},{y}"))

boxes[0].name = "audio source"

for box in boxes:
    box.draw()
pygame.display.flip()
while True:
    pass
