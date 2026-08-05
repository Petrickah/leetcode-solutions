"""
<Platform> - <Problem Title>
<URL>
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
def solve(lines):
    pass

if __name__ == "__main__":
    print(solve()) # type: ignore
