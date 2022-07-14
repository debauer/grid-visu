from typing import List

import pygame
from pygame.surface import SurfaceType
from grid.base import get_grid, GridBoxBase
from misc.font import text_font
from misc.types import GridPosition, GridLayout, Coordinate, Size, Color
from settings import content_color, grid_layout


class ContentBase:
    padding = 15
    header_correction = 50

    def __init__(
        self,
        box: GridBoxBase,
        name: str = "",
    ) -> None:
        self.parant_box = box
        self.grid = get_grid()
        self.layout = box.layout
        self.name = name
        self.surface = self.grid.surface
        self.pos = box.pos
        self.coordinates = Coordinate(
            int(self.surface.get_width() / grid_layout.x * self.pos.x) + self.padding,
            int(self.surface.get_height() / grid_layout.y * self.pos.y) + self.padding + self.header_correction,
        )
        self.size = Size(
            int(self.surface.get_width() / grid_layout.x) * self.layout.x - 2*self.padding,
            int(self.surface.get_height() / grid_layout.y * self.layout.y) - 2*self.padding - self.header_correction,
        )
        print(self.coordinates, self.size, self.pos, self.layout)

    def draw(self):
        pass


class ContentImage(ContentBase):
    def __init__(self, box: GridBoxBase, name: str = ""):
        super().__init__(box, name)
        self.img = None

    def load_image(self, image: str):
        img = pygame.image.load(image).convert()
        self.img = pygame.transform.scale(img, (self.size.x, self.size.y))

    def draw(self):
        if self.img:
            self.surface.blit(self.img, (self.coordinates.x, self.coordinates.y))


class ContentValue(ContentBase):
    def __init__(self, box: GridBoxBase, name: str = ""):
        super().__init__(box, name)
        self.threshold: dict[float, Color] = {}
        self.value = 0.0

    def set_threshold(self, value: float, color: Color):
        self.threshold[value] = color
        
    def set_value(self, value: float):
        self.value = value

    def draw(self):
        c1 = Coordinate(self.coordinates.x, self.coordinates.y)
        c2 = Coordinate(
            self.coordinates.x, self.coordinates.y + self.size.y
        )
        c3 = Coordinate(
            self.coordinates.x + self.size.x,
            self.coordinates.y + self.size.y,
        )
        c4 = Coordinate(
            self.coordinates.x + self.size.x, self.coordinates.y
        )
        pygame.draw.polygon(self.surface, (123,0,0), (c1, c2, c3, c4))
        text = text_font().render(str(self.value), True, content_color.text)
        text_rect = text.get_rect(center=(self.coordinates.x + self.size.x/2, self.coordinates.y + self.size.y/2))
        self.surface.blit(
            text,
            text_rect,
        )

class ContentList(ContentBase):

    def __init__(self, box: GridBoxBase, name: str = ""):
        super().__init__(box, name)
        self.str_list = []

    def add_list(self, str_list: List[str]):
        self.str_list = str_list

    def _draw_text(self):
        text = text_font().render(self.name, True, content_color.text)
        pygame.screen.blit(
            text,
            (
                self.coordinates.x + 10,
                self.coordinates.y + 8,
            ),
        )

    def draw(self):
        text = text_font().render(self.name, True, content_color.text)
        self.surface.blit(
            text,
            (
                self.coordinates.x + 10,
                self.coordinates.y + 8,
            ),
        )
