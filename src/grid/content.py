from typing import List

from pygame.surface import SurfaceType

from misc.font import text_font
from misc.types import GridPosition, GridLayout, Coordinate, Size
from settings import content_color, grid_layout


class ContentBase:
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

    def draw(self):
        pass


class ContentList(ContentBase):
    padding = 10

    def __init__(self, screen: SurfaceType, pos: GridPosition):
        super().__init__(screen, pos)
        self.str_list = []

    def add_list(self, str_list: List[str]):
        self.str_list = str_list

    def _draw_text(self):
        text = text_font().render(self.name, True, content_color.text)
        self.screen.blit(
            text,
            (
                self.coordinates.x + self.padding + 10,
                self.coordinates.y + self.padding + 8,
            ),
        )

    def draw(self):
        text = text_font().render(self.name, True, content_color.text)
        self.screen.blit(
            text,
            (
                self.coordinates.x + self.padding + 10,
                self.coordinates.y + self.padding + 8,
            ),
        )
