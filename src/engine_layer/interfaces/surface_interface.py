from abc import ABC, abstractmethod

from .camera_frame_interface import CameraFrameInterface
from .engine_types import PointType, SurfaceType


class SurfaceInterface(ABC):
    def __init__(self, size: PointType) -> None:
        pass

    @property
    @abstractmethod
    def size(self) -> PointType:
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
