from .enums.world_tile_type import WorldTitleType
from .title import Tile


class WorldTile(Tile):
    type: WorldTitleType

    def __init__(self) -> None:
        super().__init__()
