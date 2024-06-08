#!/usr/bin/env python3

from engine_layer.engine_layer_factory import (
    factory_camera_frame,
    factory_engine_layer,
    factory_surface,
)
from engine_layer.interfaces.engine_layer_interface import (
    EngineLayerInterface,
)
from engine_layer.interfaces.surface_interface import SurfaceInterface
from entites.world_map import WorldMap

engine_layer: EngineLayerInterface
surface: SurfaceInterface


def main():
    load()


def load():
    global engine_layer
    global surface

    engine_layer = factory_engine_layer()
    engine_layer.initialize()

    surface = factory_surface([200, 200])
    camera = factory_camera_frame([0, 0], [30, 30])
    surface.draw(camera)

    world_map = WorldMap(conf=engine_layer.config_loader(addr="src/default.conf.yml"))


if __name__ == "__main__":
    main()
