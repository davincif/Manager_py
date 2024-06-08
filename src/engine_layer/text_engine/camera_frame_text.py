from engine_layer.interfaces.camera_frame_interface import CameraFrameInterface
from engine_layer.interfaces.engine_types import PointType


class CameraFrameText(CameraFrameInterface):
    __upper_left: PointType = [0, 0]
    __size: PointType = [0, 0]
    __down_right: PointType = [0, 0]

    def __init__(self, upper_left: PointType, size: PointType) -> None:
        self.upper_left = upper_left
        self.size = size

    @property
    def upper_left(self) -> PointType:
        return self.__upper_left

    @upper_left.setter
    def upper_left(self, value: PointType):
        self.__upper_left = value
        self.__update_down_right()

    @property
    def size(self) -> PointType:
        return self.__size

    @size.setter
    def size(self, value: PointType):
        self.__size = value
        self.__update_down_right()

    @property
    def down_right(self):
        return self.__down_right

    def is_camera_equivalent(self, camera_to_compare: CameraFrameInterface):
        upper_left = camera_to_compare.upper_left
        size = camera_to_compare.size

        return (
            self.__upper_left[0] == upper_left[0]
            and self.__upper_left[1] == upper_left[1]
            and self.size[0] == size[0]
            and self.size[1] == size[1]
        )

    def __update_down_right(self):
        self.__down_right[0] = self.__upper_left[0] + self.__size[0]
        self.__down_right[1] = self.__upper_left[1] + self.__size[1]
