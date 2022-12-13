import copy
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Set, Tuple


@dataclass(frozen=True, eq=True)
class Square:
    row: int
    col: int
    height: int


class Grid:
    height: int
    width: int
    grid: List[List[Square]]
    distance: int

    def __init__(self, grid: List[List[Square]]) -> None:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.distance = -1

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

    def walk(self, current: Square, visited: Optional[Set[Square]] = None):
        if visited is None:
            visited = set()
        
        xxx = copy.deepcopy(visited)

        if current.height == E:
            if self.distance == -1:
                self.distance = len(visited)
            else:
                if self.distance > len(visited):
                    self.distance = len(visited)
            return

        xxx.add(current)

        for n in self.get_all_neighbors(current):
            if n not in xxx:
                if n.height - current.height == 1 or n.height == current.height:
                    self.walk(n, xxx)

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

grid = Grid(all_squares)

print(grid)

start = grid.get_square(starting_coords[0], starting_coords[1])
grid.walk(start)

print(grid.distance)
