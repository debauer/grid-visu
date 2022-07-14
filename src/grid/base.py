from typing import Optional, List

import pygame
from pygame.surface import SurfaceType

from misc.registry import RegisterAble
from misc.font import headline_font
from misc.types import Coordinate, Size, GridLayout, GridPosition
from settings import (
    box_colors,
    grid_layout,
)


class GridBoxBase(RegisterAble):
    padding = 3
    unamed_count = 0

    def __init__(self, pos: GridPosition, layout: GridLayout = (1, 1), name: str = "") -> None:
        RegisterAble.__init__(self)
        self.grid = get_grid()
        self.layout = layout
        self.name = f"unnamed_{self.unamed_count}" if name == "" else name
        self.surface = self.grid.surface
        self.pos = pos
        self.coordinates = Coordinate(
            int(self.surface.get_width() / grid_layout.x * self.pos.x),
            int(self.surface.get_height() / grid_layout.y * self.pos.y),
        )
        self.size = Size(
            int(self.surface.get_width() / grid_layout.x) * self.layout.x,
            int(self.surface.get_height() / grid_layout.y * self.layout.y),
        )
        self.grid.add_box(self)

    def draw(self):
        pass

    def __repr__(self):
        return f'GridBoxBase("{self.name}")'


class GridBox(GridBoxBase):
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
        pygame.draw.polygon(self.surface, color, (c1, c2, c3, c4), size)

    def _set_titel(self):
        text = headline_font().render(self.name, True, box_colors.headline)
        self.surface.blit(
            text,
            (
                self.coordinates.x + self.padding + 10,
                self.coordinates.y + self.padding + 8,
            ),
        )

        padding = self.padding + 10
        padding_top = padding + 40
        c1 = Coordinate(self.coordinates.x + padding, self.coordinates.y + padding_top)
        c2 = Coordinate(
            self.coordinates.x + self.size.x - padding, self.coordinates.y + padding_top
        )
        pygame.draw.line(self.surface, box_colors.border2, c1, c2, 1)

    def draw(self):
        self._draw_box(self.padding, box_colors.border1, 3)
        self._draw_box(self.padding + 3, box_colors.border2)
        self._set_titel()


class Grid:
    layout: GridLayout = (3, 2)
    boxes: List[GridBox] = []

    def __init__(self, surface: SurfaceType, layout: GridLayout = GridLayout(1, 1)):
        self.surface = surface
        self._layout = layout
        self.grid_width = self.surface.get_width() / self._layout.x
        self.grid_height = self.surface.get_height() / self._layout.y

    def add_box(self, box: GridBox):
        self.boxes.append(box)

    def draw(self):
        for box in self.boxes:
            box.draw()


__grid: Optional[Grid] = None


def create_grid(screen: SurfaceType, layout: GridLayout):
    global __grid
    assert __grid is None
    __grid = Grid(screen, layout)
    return __grid


def get_grid_box(name: str) -> Optional[GridBox]:
    assert __grid is not None
    for box in __grid.boxes:
        if box.name == name:
            return box
    return


def get_grid():
    global __grid
    assert __grid is not None
    return __grid
