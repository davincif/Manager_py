from enum import Enum, auto


class WorldTitleType(Enum):
    NONE = 0
    GRASS = auto()
    WATER = auto()
    FOREST = auto()
    MOUNTAINS = auto()

    @staticmethod
    def get_value_list():
        return [elem.value for elem in WorldTitleType]
