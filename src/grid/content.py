from typing import List

import pygame
from pygame.surface import SurfaceType
from grid.base import get_grid, GridBoxBase
from misc.font import text_font
from misc.types import GridPosition, GridLayout, Coordinate, Size
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
        img = pygame.image.load(image)
        self.img = pygame.transform.scale(img, (self.size.x, self.size.y))

    def draw(self):
        if self.img:
            print("Asdasd")
            self.surface.blit(self.img, (self.coordinates.x, self.coordinates.y))


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
                self.coordinates.x + self.padding + 10,
                self.coordinates.y + self.padding + 8,
            ),
        )

    def draw(self):
        text = text_font().render(self.name, True, content_color.text)
        self.surface.blit(
            text,
            (
                self.coordinates.x + self.padding + 10,
                self.coordinates.y + self.padding + 8,
            ),
        )
