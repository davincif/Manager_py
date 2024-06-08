from abc import ABC, abstractmethod

from utils import Singleton

type EngineConfigurations = object
type SurfaceType = list[list[str]]
type CachedSurface = str
type Point = tuple[int, int]


class CameraFrameInterface(ABC):
    upper_left: Point
    size: Point
    down_right: Point

    @abstractmethod
    def is_camera_equivalent(self, camera_to_compare):
        pass


class SurfaceInterface(ABC):
    def __init__(self, size: Point) -> None:
        pass

    @property
    @abstractmethod
    def size(self) -> Point:
        pass

    @property
    @abstractmethod
    def surface(self) -> SurfaceType:
        pass

    @abstractmethod
    def draw(self, camera: CameraFrameInterface) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass


class EngineLayerInterface(ABC, Singleton):
    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def finish(self) -> None:
        pass

    @abstractmethod
    def config_loader(self, addr: str | None) -> EngineConfigurations:
        pass

    @abstractmethod
    def draw(self, surface: SurfaceInterface) -> None:
        pass
