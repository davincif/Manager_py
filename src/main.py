from engine_layer import EngineLayer

from entites import WorldMap


def main():
    load()


def load():
    EngineLayer.initialize()
    worldMap = WorldMap()


if __name__ == "__main__":
    main()
