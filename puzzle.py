"""Example coding puzzle for the SimonBarracloughCV portfolio.

Puzzle: highest_even(numbers)
Return the highest even integer in a list of numbers.
If the list contains no even integers, return None.
"""

from __future__ import annotations

from typing import Iterable


PUZZLE = {
    "name": "highest_even",
    "description": "Return the highest even integer from a list, or None if there are no even integers.",
    "examples": [
        {"input": [1, 2, 3, 4], "output": 4},
        {"input": [9, 7, 5], "output": None},
        {"input": [-4, -2, -9], "output": -2},
    ],
}


def highest_even(numbers: Iterable[int]) -> int | None:
    """Return the highest even integer from numbers.

    Args:
        numbers: An iterable of integers.

    Returns:
        The highest even integer, or None when no even values exist.
    """
    evens = [number for number in numbers if number % 2 == 0]
    if not evens:
        return None
    return max(evens)


if __name__ == "__main__":
    sample = [1, 8, 3, 10, 5]
    print(f"Highest even number in {sample}: {highest_even(sample)}")
