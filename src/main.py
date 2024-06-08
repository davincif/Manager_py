#!/usr/bin/env python3

from engine_layer.engine_layer_factory import factory_camera_frame, factory_engine_layer
from engine_layer.interfaces.engine_layer_interface import EngineLayerInterface
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

    world_map = WorldMap(conf=engine_layer.config_loader(addr="src/default.conf.yml"))
    camera = factory_camera_frame(upper_left=[0, 0], size=[30, 30])


if __name__ == "__main__":
    main()
