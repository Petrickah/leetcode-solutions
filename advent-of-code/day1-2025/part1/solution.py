"""
Advent of Code 2025 - Day 1: Secret Entrance
https://adventofcode.com/2025/day/1
"""

from functools import wraps
from pathlib import Path

def read_lines(filename="input.txt"):
    """Decorator factory: reads `filename` next to the calling script and
    passes a list of stripped, non-empty lines as the wrapped function's
    first argument. Swap `filename` per problem if the input file is named
    differently."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            path = Path(__file__).parent / filename
            with path.open("r") as file:
                lines = [line.strip() for line in file if line.strip()]
            return func(lines, *args, **kwargs)
        return wrapper
    return decorator


@read_lines()
def solve(lines, start, size):
    counter = 0
    value = start
    for curr_line in lines:
        (op, n_clicks) = (curr_line[0], int(curr_line[1:]))
        if op == 'L':
            value = (value - n_clicks) % size
        elif op == 'R':
            value = (value + n_clicks) % size
        if value == 0:
            counter += 1
    return counter

if __name__ == "__main__":
    print("Solution: {}".format(solve(start=50, size=100))) # type: ignore
