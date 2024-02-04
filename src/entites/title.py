from .world_conf import _GlobalTerrains, _GlobalTerrainsProps
from .enums.world_tile_type import WorldTitleType


class Tile:
    position: tuple[int, int]
    """position (i,j) in the map matriz"""

    is_constructable: bool

    _symbol: str
    _graphic_symbol: str
    _font_color: str

    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position
        self._symbol = ""
        self._graphic_symbol = ""
        self._font_color = ""

    def __str__(self) -> str:
        return self._graphic_symbol
