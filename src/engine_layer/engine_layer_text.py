import platform
from os import system

from colorama import just_fix_windows_console, init as colorama_init
from yaml import YAMLError, safe_load

from engine_layer.engine_layer_interface import SurfaceInterface

from .engine_layer_interface import (
    CachedSurface,
    CameraFrameInterface,
    EngineConfigurations,
    EngineLayerInterface,
    Point,
    SurfaceType,
)


class CameraFrameText(CameraFrameInterface):
    __upper_left: Point = [0, 0]
    __size: Point = [0, 0]
    __down_right: Point = [0, 0]

    def __init__(self, upper_left: Point, size: Point) -> None:
        self.upper_left = upper_left
        self.size = size

    @property
    def upper_left(self) -> Point:
        return self.__upper_left

    @upper_left.setter
    def upper_left(self, value: Point):
        self.__upper_left = value
        self.__update_down_right()

    @property
    def size(self) -> Point:
        return self.__size

    @size.setter
    def size(self, value: Point):
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


class EngineLayerText(EngineLayerInterface):
    __is_windows = False

    def initialize(self) -> None:
        print("loading...")

        # system
        self.__identify_system()

        # initing colorama
        just_fix_windows_console()
        colorama_init()

        # finishing loading
        self.__clear_terminal()
        print("game started!", end="\n\n")

    def finish(self) -> None:
        print("The game is closed!")

    def config_loader(self, addr: str | None) -> EngineConfigurations:
        loaded_info = None

        with open(addr, "r", encoding="utf-8") as stream:
            try:
                loaded_info = safe_load(stream)
            except YAMLError as exc:
                print(exc)

        return loaded_info

    def draw(self, surface: SurfaceInterface) -> None:
        raise NotImplementedError()

    def __identify_system(self):
        self.__is_windows = platform.system().lower().startswith("windows")

    def __clear_terminal(self):
        if self.__is_windows:
            system("cls")
        else:
            system("clear")


class SurfaceText(SurfaceInterface):
    __TERRAIN_SIZE = 3

    __size: Point
    __drawble: SurfaceType
    __cache: CachedSurface
    __last_drew_camera: CameraFrameText | None

    def __init__(self, size: Point) -> None:
        self.__size = size
        self.__drawble = []

        self.clear()

        self.__update_cache()

    @property
    def size(self) -> Point:
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
            print("cliped_upper_left", cliped_upper_left)
            print("cliped_down_right", cliped_down_right)

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
