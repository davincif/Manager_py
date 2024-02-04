from colorama import just_fix_windows_console, init as colorama_init
from os import system

from .engine_layer_interface import EngineLayerInterface


class EngineLayerText(EngineLayerInterface):
    def initialize_engine(self):
        print("loading...")

        # initing colorama
        just_fix_windows_console()
        colorama_init()

        # finishing loading
        system("clear")
        print("game started!", end="\n\n")

    def finish_engine(self):
        print("The game is closed!")
