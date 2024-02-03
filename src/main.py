from colorama import just_fix_windows_console, init as colorama_init
from os import system

GAME_NAME = "GAME_NAME"


def main():
    load()


def load():
    print("loading...")

    # initing colorama
    just_fix_windows_console()
    colorama_init()

    # finishing loading
    system("clear")
    print("game started!", end="\n\n")


if __name__ == "__main__":
    main()
