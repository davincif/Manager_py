import platform
from os import system
from typing import Union

from colorama import just_fix_windows_console, init as colorama_init
from yaml import YAMLError, safe_load

from .engine_layer_interface import EngineLayerInterface


class EngineLayerText(EngineLayerInterface):
    __is_windows = False

    def initialize(self):
        print("loading...")

        # system
        self.__identify_system()

        # initing colorama
        just_fix_windows_console()
        colorama_init()

        # finishing loading
        self.__clear_terminal()
        print("game started!", end="\n\n")

    def finish(self):
        print("The game is closed!")

    def configLoader(self, addr: str) -> Union[object, None]:
        loaded_info = None

        with open(addr, "r") as stream:
            try:
                loaded_info = safe_load(stream)
            except YAMLError as exc:
                print(exc)

        return loaded_info

    def __identify_system(self):
        self.__is_windows == platform.system().lower().startswith("windows")

    def __clear_terminal(self):
        if self.__is_windows:
            system("cls")
        else:
            system("clear")
