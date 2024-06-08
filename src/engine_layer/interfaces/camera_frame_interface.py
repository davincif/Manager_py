from abc import ABC, abstractmethod

from .engine_types import PointType


class CameraFrameInterface(ABC):
    upper_left: PointType
    size: PointType
    down_right: PointType

    @abstractmethod
    def is_camera_equivalent(self, camera_to_compare):
        pass
