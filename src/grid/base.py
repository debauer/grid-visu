from typing import NamedTuple

import pygame
from pygame import surface

from settings import (
    GRID_BOX_COLOR1,
    GRID_BOX_PADDING,
    GRID_DIM_X,
    GRID_DIM_Y,
    GRID_BOX_COLOR2, GRID_BOX_HEADLINE_COLOR, headline_font,
)


class Coordinate(NamedTuple):
    x: int
    y: int


class Size(NamedTuple):
    x: int
    y: int


class GridBase:
    def __init__(self, screen: surface, coordinates: Coordinate, name: str = "") -> None:
        self.name = name
        self.screen = screen
        self.coordinates = coordinates
        screen_size = self.screen.get_size()
        self.size = Size(
            int(screen_size[0] / GRID_DIM_X), int(screen_size[1] / GRID_DIM_Y)
        )

    def draw(self):
        pass


class GridBox(GridBase):
    def _draw_box(self, padding: int, color, size=1):
        c1 = Coordinate(self.coordinates.x + padding, self.coordinates.y + padding)
        c2 = Coordinate(
            self.coordinates.x + padding, self.coordinates.y - padding + self.size.y
        )
        c3 = Coordinate(
            self.coordinates.x - padding + self.size.x,
            self.coordinates.y - padding + self.size.y,
        )
        c4 = Coordinate(
            self.coordinates.x - padding + self.size.x, self.coordinates.y + padding
        )
        print(c1, c2, c3, c4)
        pygame.draw.polygon(self.screen, color, (c1, c2, c3, c4), size)

    def _set_titel(self):
        text = headline_font().render(self.name, True, GRID_BOX_HEADLINE_COLOR)
        self.screen.blit(text, (self.coordinates.x + GRID_BOX_PADDING + 10, self.coordinates.y + GRID_BOX_PADDING + 5))

    def draw(self):
        self._draw_box(GRID_BOX_PADDING, GRID_BOX_COLOR1, 3)
        self._draw_box(GRID_BOX_PADDING + 3, GRID_BOX_COLOR2)
        self._set_titel()
        
