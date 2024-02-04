"""A module focoused on bringing facilitation in regrading number generation and randomness
"""

from random import choice, random, seed
from typing import TypeVar


def update_seed(user_seed: int | float | str | bytes | bytearray | None = None):
    seed(user_seed)


def coin_flip(heads_changes=0.5) -> bool:
    """A simple coin flip, but the odds for each side of the coin can be changed.

    Args:
        heads_changes: the probability of te coin flipping a head face.

    Returns:
        bool: True when head, False when tails.
    """
    return random() < heads_changes


# fmt: off
T = TypeVar("T")
def choose_from(items: list[T]) -> T:
    return choice(items)
