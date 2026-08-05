"""
Advent of Code 2025 - Day 1, Part Two: Secret Entrance
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


@read_lines(filename="../input.txt")
def solve(lines, start, size):
    passive_counter = 0
    active_counter = 0
    active_value = start
    for curr_line in lines:
        (op, n_clicks) = (curr_line[0], int(curr_line[1:]))
        if op == 'L':
            first_encounter = active_value if active_value > 0 else size
            if n_clicks >= first_encounter:
                active_counter += (n_clicks - first_encounter) // size + 1
            active_value = (active_value - n_clicks) % size
        elif op == 'R':
            active_counter += abs(active_value + n_clicks) // size
            active_value = (active_value + n_clicks) % size
        if active_value == 0:
            active_counter -= 1
            passive_counter += 1
        print("{} => Active Counter: {}".format(curr_line, active_counter))
    return active_counter + passive_counter

if __name__ == "__main__":
    print("Solution: {}".format(solve(start=50, size=100))) # type: ignore
