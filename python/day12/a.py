import copy
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import List, Optional, Set, Tuple

sys.setrecursionlimit(10000)


@dataclass(unsafe_hash=True)
class Square:
    row: int
    col: int
    height: int
    distance_from_end: int = -1


class Grid:
    height: int
    width: int
    grid: List[List[Square]]
    start_coords: Tuple[int, int]
    end_coords: Tuple[int, int]

    def __init__(
        self,
        grid: List[List[Square]],
        start_coords: Tuple[int, int],
        end_coords: Tuple[int, int],
    ) -> None:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start_coords = start_coords
        self.end_coords = end_coords

    def __str__(self, visited: Set[Square] = set()) -> str:
        out = ""

        for row_number, _ in enumerate(self.grid):
            for col_number, _ in enumerate(self.grid[row_number]):
                sq = self.get_square(row_number, col_number)
                if sq.row == end_coords[0] and sq.col == end_coords[1]:
                    out += "  E"
                elif sq.row == start_coords[0] and sq.col == start_coords[1]:
                    out += "  S"
                elif sq in visited:
                    out += "  V"
                else:
                    out += str(sq.height).rjust(
                        2, " "
                    )
                out += " "
            out += "\n"

        return out

    def get_square(self, row: int, col: int) -> Square:
        return self.grid[row][col]

    def get_all_neighbors(self, s: Square) -> List[Square]:
        out = []

        if s.col > 0:
            sq = self.grid[s.row][s.col - 1]
            out.append(sq)
        # Right
        if s.col < self.width - 1:
            sq = self.grid[s.row][s.col + 1]
            out.append(sq)
        # Top
        if s.row > 0:
            sq = self.grid[s.row - 1][s.col]
            out.append(sq)
        # Bottom
        if s.row < self.height - 1:
            sq = self.grid[s.row + 1][s.col]
            out.append(sq)

        return out

    def map_distance(self, current: Square, last_distance=0):
        current.distance_from_end = last_distance

        last_distance += 1

        for n in self.get_all_neighbors(current):
            if n.distance_from_end == -1 or n.distance_from_end > last_distance:
                if -10 <= current.height - n.height <= 1:
                    self.map_distance(n, last_distance)


all_squares: List[List[Square]] = []
start_coords = (0, 0)
end_coords = (0, 0)

p = Path(__file__).with_name("input.txt")
with p.open() as f:
    lines = [line for line in f.read().split("\n")]
    for row_number, line in enumerate(lines):
        row = []
        for col_number, char in enumerate(line):
            height = ord(char) - ord("a") + 1
            if char == "S":
                height = 1
                start_coords = (row_number, col_number)
            elif char == "E":
                height = ord("z") - ord("a") + 1
                end_coords = (row_number, col_number)
            s = Square(row_number, col_number, height)
            row.append(s)

        all_squares.append(row)

grid = Grid(all_squares, start_coords, end_coords)

start = grid.get_square(start_coords[0], start_coords[1])
end = grid.get_square(end_coords[0], end_coords[1])
grid.map_distance(end)

print(start.distance_from_end)
# 425

least = min([sq.distance_from_end for row in grid.grid for sq in row if sq.height == 1 and sq.distance_from_end != -1])
print(least)
# 418