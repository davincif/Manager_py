from engine_layer.interfaces.engine_types import (
    CachedSurfaceType,
    PointType,
    SurfaceType,
)
from engine_layer.interfaces.surface_interface import SurfaceInterface
from engine_layer.text_engine.camera_frame_text import CameraFrameText


class SurfaceText(SurfaceInterface):
    __TERRAIN_SIZE = 3

    __size: PointType
    __drawble: SurfaceType
    __cache: CachedSurfaceType
    __last_drew_camera: CameraFrameText | None

    def __init__(self, size: PointType) -> None:
        self.__size = size
        self.__drawble = []

        self.clear()

        self.__update_cache()

    @property
    def size(self) -> PointType:
        return self.__drawble[0], len(self.__drawble)

    @property
    def surface(self) -> SurfaceType:
        return self.__cache

    def draw(self, camera: CameraFrameText | None = None) -> None:
        # if last used camare is the same used now, use cached data and save computational time
        if camera is None or (
            self.__last_drew_camera is not None
            and self.__last_drew_camera.is_camera_equivalent(camera)
        ):
            print(self.__cache)
            return

        self.__last_drew_camera = camera

        self.__update_cache()
        print(self.__cache)

    def clear(self) -> None:
        for _ in range(self.__size[0]):
            self.__drawble.append(" • " * self.__size[1])
        self.__last_drew_camera = None

    def __update_cache(self):
        clipped_map: SurfaceType

        if self.__last_drew_camera is None:
            clipped_map = self.__drawble
        else:
            cliped_camera = self.__clip_camera(self.__last_drew_camera)
            cliped_upper_left = cliped_camera.upper_left
            cliped_down_right = cliped_camera.down_right

            clipped_map = list(
                map(
                    lambda line: line[
                        cliped_upper_left[0]
                        * self.__TERRAIN_SIZE : cliped_down_right[0]
                        * self.__TERRAIN_SIZE
                    ],
                    self.__drawble[cliped_upper_left[1] : cliped_down_right[1]],
                )
            )

        self.__cache = "\n".join(clipped_map)

    def __clip_camera(self, camera: CameraFrameText) -> CameraFrameText:
        upper_left = camera.upper_left

        if upper_left[0] < 0 or upper_left[0] >= len(self.__drawble[0]):
            upper_left[0] = 0

        if upper_left[1] < 0 or upper_left[1] >= len(self.__drawble):
            upper_left[1] = 0

        size = camera.size

        if size[0] < 0:
            size[0] = 0
        elif upper_left[0] + size[0] > len(self.__drawble[0]):
            size[0] = len(self.__drawble[0]) - upper_left[0]

        if size[1] < 0:
            size[1] = 0
        elif upper_left[1] + size[1] > len(self.__drawble):
            size[1] = len(self.__drawble) - upper_left[1]

        return CameraFrameText(upper_left, size)
