from typing import NamedTuple, Type, Dict

import pygame
from pygame import surface
from pygame.surface import SurfaceType

from grid.content import ContentBase
from misc.font import headline_font
from misc.types import Coordinate, Size, GridLayout, GridPosition
from settings import (
    box_colors,
    grid_layout,
)


class GridBoxBase:
    padding = 3

    def __init__(
        self,
        screen: SurfaceType,
        pos: GridPosition,
        layout: GridLayout = (1, 1),
        name: str = "",
    ) -> None:
        self.layout = layout
        self.name = name
        self.screen = screen
        self.pos = pos
        self.coordinates = Coordinate(
            int(self.screen.get_width() / grid_layout.x * self.pos.x),
            int(self.screen.get_height() / grid_layout.y * self.pos.y),
        )
        self.size = Size(
            int(self.screen.get_width() / grid_layout.x) * self.layout.x,
            int(self.screen.get_height() / grid_layout.y * self.layout.y),
        )
        self.child: ContentBase | None = None

    def add_child(self, child: Type[ContentBase]) -> ContentBase:
        self.child = child(self.screen, self.pos)
        return self.child

    def draw(self):
        pass


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
        print(c1, c2, c3, c4)
        pygame.draw.polygon(self.screen, color, (c1, c2, c3, c4), size)

    def _set_titel(self):
        text = headline_font().render(self.name, True, box_colors.headline)
        self.screen.blit(
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
        pygame.draw.line(self.screen, box_colors.border2, c1, c2, 1)

    def draw(self):
        self._draw_box(self.padding, box_colors.border1, 3)
        self._draw_box(self.padding + 3, box_colors.border2)
        self._set_titel()


class Grid:
    layout: GridLayout = (3, 2)
    boxes: Dict[str, GridBoxBase] = {}

    def __init__(self, screen: SurfaceType, layout: GridLayout = GridLayout(1, 1)):
        self._screen = screen
        self._layout = layout
        self.grid_width = self._screen.get_width() / self._layout.x
        self.grid_height = self._screen.get_height() / self._layout.y

    def add_box(self, name: str, pos: GridPosition, layout: GridLayout = (1, 1)) -> GridBoxBase:
        self.boxes[name] = GridBox(
            screen=self._screen,
            pos=pos,
            layout=layout,
            name=name,
        )
        return self.boxes[name]

    def draw(self):
        for key in self.boxes:
            self.boxes[key].draw()
