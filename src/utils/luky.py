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


T = TypeVar("T")


def choose_from(items: list[T], probability_distribution: list[float | int] = []) -> T:
    """Return one of the given item radombly in a flat distribution.
    If any probabilty distribution is given, the randomness is going to flow this given curve.

    Args:
        items: items to be choosen
        probability_distribution: the "weight" of each element in the probability curve. Consider flat if none is provided

    Raises:
        ValueError: if probability_distribution is provided, must  have the same time as the items list.

    Returns:
        T: one of the given elements in the item list.
    """
    probability_distribution_len = len(probability_distribution)

    # simple case, where the distribution must be considered flat
    if probability_distribution_len == 0:
        return choice(items)

    # params checking
    if probability_distribution_len != len(items):
        raise ValueError("you must have as mush probability_distribution as items")

    # transforming
    cumulative_distribution = []  # CDF - cumulative distribution function
    dist_sim = 0
    for weight in probability_distribution:
        dist_sim += weight
        cumulative_distribution.append(dist_sim)

    # TODO: cumulative_distribution PODE TER SOMENTE 1 ELEMENTO!!!
    coin = random_in_range(
        cumulative_distribution[0],
        cumulative_distribution[probability_distribution_len - 1],
    )
    index = __find_point_index_in_cdf(coin, cumulative_distribution)

    return items[index]


def random_in_range(x: float | int, y: float | int):
    return x - (y - x) * random()


def __find_point_index_in_cdf(point: float | int, cdf: list[float | int]):
    """Finds the index of the given point in a cumulative distribution function (CDF)."""
    las_cdf_index = len(cdf) - 1
    for index, cdf_point in enumerate(cdf):
        if point <= cdf_point or index == las_cdf_index:
            return index
