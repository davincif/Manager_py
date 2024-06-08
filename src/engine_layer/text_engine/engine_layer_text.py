from os import system
import platform

from colorama import colorama_text, just_fix_windows_console
from yaml import YAMLError, safe_load

from engine_layer.interfaces.engine_layer_interface import EngineLayerInterface
from engine_layer.interfaces.engine_types import EngineConfigurationsType
from engine_layer.interfaces.surface_interface import SurfaceInterface


class EngineLayerText(EngineLayerInterface):
    __is_windows = False

    def initialize(self) -> None:
        print("loading...")

        # system
        self.__identify_system()

        # initing colorama
        just_fix_windows_console()
        colorama_text()

        # finishing loading
        self.__clear_terminal()
        print("game started!", end="\n\n")

    def finish(self) -> None:
        print("The game is closed!")

    def config_loader(self, addr: str | None) -> EngineConfigurationsType:
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
