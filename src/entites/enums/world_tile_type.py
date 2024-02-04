from enum import Enum, auto


class WorldTitleType(Enum):
    GRASS = 1
    WATER = auto()
    FOREST = auto()
    MOUNTAINS = auto()

    @staticmethod
    def get_value_list():
        return [elem.value for elem in WorldTitleType]
