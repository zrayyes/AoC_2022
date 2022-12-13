from dataclasses import dataclass
from pathlib import Path
from typing import List, Set, Tuple


@dataclass(frozen=True, eq=True)
class Square:
    row: int
    col: int
    height: int


class Grid:
    height: int
    width: int
    grid: List[List[Square]]
    starting_coords: Tuple[int, int]

    def __init__(self, grid: List[List[Square]], starting_coords: Tuple[int, int]) -> None:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.starting_coords = starting_coords

    def get_square(self, row: int, col: int) -> Square:
        return self.grid[row][col]

    def __str__(self, visited: Set[Square] = set()) -> str:
        out = ""

        for row_number, _ in enumerate(self.grid):
            for col_number, _ in enumerate(self.grid[row_number]):
                sq = self.get_square(row_number, col_number)
                if sq.height == E:
                    out += " E"
                elif sq.height == S:
                    out += " S"
                elif sq in visited:
                    out += " V"
                else:
                    out += str(self.get_square(row_number, col_number).height).rjust(
                        2, " "
                    )
                out += " "

            out += "\n"

        return out


S = 0
E = 27

all_squares: List[List[Square]] = []
starting_coords = (0, 0)

p = Path(__file__).with_name("input.txt")
with p.open() as f:
    lines = [line for line in f.read().split("\n")]
    for row_number, line in enumerate(lines):
        row = []
        for col_number, char in enumerate(line):
            height = ord(char) - ord("a") + 1
            if char == "S":
                height = S
                starting_coords = (row_number, col_number)
            elif char == "E":
                height = E
            s = Square(row_number, col_number, height)
            row.append(s)

        all_squares.append(row)

grid = Grid(all_squares, starting_coords)

print(grid)
