from abc import ABC, abstractmethod

from .surface_interface import SurfaceInterface
from .camera_frame_interface import CameraFrameInterface
from .engine_types import (
    EngineConfigurationsType,
)
from utils import Singleton


class EngineLayerInterface(ABC, Singleton):
    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def finish(self) -> None:
        pass

    @abstractmethod
    def config_loader(self, addr: str | None) -> EngineConfigurationsType:
        pass

    @abstractmethod
    def draw(self, surface: SurfaceInterface) -> None:
        pass
