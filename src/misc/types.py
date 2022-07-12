from dataclasses import dataclass
from typing import NamedTuple


class Coordinate(NamedTuple):
    x: int
    y: int


class Size(NamedTuple):
    x: int
    y: int


class GridLayout(NamedTuple):
    x: int
    y: int


class GridPosition(NamedTuple):
    x: int
    y: int


class Color(NamedTuple):
    r: int
    g: int
    b: int


@dataclass
class ColorPaletteBox:
    border1: Color  # border1
    border2: Color  # border2
    misc: Color  # misc
    text: Color  # text
    headline: Color  # headlines
    background: Color = Color(0, 0, 0)


@dataclass
class ColorPaletteContent:
    text: Color  # text
