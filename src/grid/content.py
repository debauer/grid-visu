import time
from typing import List

import cv2
import pygame
from pygame.surface import SurfaceType
from grid.base import get_grid, GridBoxBase, get_grid_box
from misc.font import text_font
from misc.registry import RegisterAble
from misc.types import GridPosition, GridLayout, Coordinate, Size, Color
from settings import content_color, grid_layout


class ContentBase(RegisterAble):
    padding = 15
    header_correction = 50

    def __init__(
            self,
            box_name: str,
            name: str = "",
    ) -> None:
        RegisterAble.__init__(self)
        self.parant_box = get_grid_box(box_name)
        self.grid = get_grid()
        self.layout = self.parant_box.layout
        self.name = name
        self.surface = self.grid.surface
        self.pos = self.parant_box.pos
        self.coordinates = Coordinate(
            int(self.surface.get_width() / grid_layout.x * self.pos.x) + self.padding,
            int(self.surface.get_height() / grid_layout.y * self.pos.y) + self.padding + self.header_correction,
        )
        self.size = Size(
            int(self.surface.get_width() / grid_layout.x) * self.layout.x - 2 * self.padding,
            int(self.surface.get_height() / grid_layout.y * self.layout.y) - 2 * self.padding - self.header_correction,
        )
        print(box_name, self.coordinates, self.size, self.pos, self.layout)

    def draw(self):
        pass

    def __repr__(self):
        return f'ContentBase("{self.name}", {self.__class__})'


class ContentVideo(ContentBase):
    def __init__(self, box_name: str, video_link: str, name: str = "", switch_interval: int = 1.0):
        super().__init__(box_name, name)
        self.active = 0
        self.interval = switch_interval
        self.last_change = time.time()
        self.cap = cv2.VideoCapture(video_link)
        self.link = video_link
        self.video_surface = pygame.Surface((self.size.x, self.size.y ))

    def draw(self):
        success, img = self.cap.read()
        if success == False:
            self.cap = cv2.VideoCapture(self.link)
            success, img = self.cap.read()
        img = cv2.resize(img, (self.size.x, self.size.y), interpolation=cv2.INTER_NEAREST)
        #img = pygame.image.frombuffer(img.tobytes(), (self.size.x, self.size.y), "BGR")
        #self.surface.blit(img, (self.coordinates.x, self.coordinates.y))
        
        #print(self.video_surface.get_height(), self.video_surface.get_width())
        #print(img.shape)
        pygame.surfarray.blit_array(self.video_surface, img.swapaxes(0,1))
        self.surface.blit(self.video_surface, (self.coordinates.x, self.coordinates.y))


class ContentImages(ContentBase):
    def __init__(self, box_name: str, image_links: list[str], name: str = "", switch_interval: int = 5.0):
        super().__init__(box_name, name)
        self.images: list[pygame.Surface] = []
        self.active = 0
        self.interval = switch_interval
        self.last_change = time.time()
        self.init = True
        for link in image_links:
            self.load_image(link)

    def load_image(self, image_link: str):
        img = pygame.image.load(image_link).convert()
        self.images.append(pygame.transform.scale(img, (self.size.x, self.size.y)))

    def draw(self):
        if self.last_change + self.interval < time.time() or self.init:
            self.init = False
            self.active = 0 if self.active + 1 >= len(self.images) else self.active + 1
            self.last_change = time.time()
            if len(self.images) > self.active:
                self.surface.blit(self.images[self.active], (self.coordinates.x, self.coordinates.y))


class ContentValue(ContentBase):
    def __init__(self, box_name: str, name: str = "", value: float = 0.0):
        super().__init__(box_name, name)
        self.threshold: dict[float, Color] = {}
        self.value = value

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
        pygame.draw.polygon(self.surface, (123, 0, 0), (c1, c2, c3, c4))
        text = text_font().render(str(self.value), True, content_color.text)
        text_rect = text.get_rect(center=(self.coordinates.x + self.size.x / 2, self.coordinates.y + self.size.y / 2))
        self.surface.blit(
            text,
            text_rect,
        )


class ContentList(ContentBase):

    def __init__(self, box_name: str, name: str = ""):
        super().__init__(box_name, name)
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
