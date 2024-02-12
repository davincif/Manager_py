from engine_layer import EngineLayer

from entites.world_map import WorldMap


def main():
    load()


def load():
    EngineLayer.initialize()
    worldMap = WorldMap()
    print(worldMap)


if __name__ == "__main__":
    main()
