from .world_conf import _GlobalTerrains, _GlobalTerrainsProps
from .enums.world_tile_type import WorldTitleType
from .title import Tile


class WorldTile(Tile):
    type: WorldTitleType

    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(position)

        self.type = WorldTitleType.NONE

    def set_biome(self, terrain_type: WorldTitleType, world_conf: _GlobalTerrains):
        self.type = terrain_type

        match terrain_type:
            case WorldTitleType.GRASS:
                self.__set_title_confs(world_conf.grass)
            case WorldTitleType.WATER:
                self.__set_title_confs(world_conf.water)
            case WorldTitleType.FOREST:
                self.__set_title_confs(world_conf.forest)
            case WorldTitleType.MOUNTAINS:
                self.__set_title_confs(world_conf.mountains)

    def __set_title_confs(self, confs: _GlobalTerrainsProps):
        self.is_constructable = confs.is_constructable
        self._symbol = confs.symbol
        self._graphic_symbol = confs.graphic_symbol
        self._font_color = confs.graphic_symbol
