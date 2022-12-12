from dataclasses import dataclass
from pathlib import Path
from typing import List, Set


@dataclass(frozen=True, eq=True)
class Square:
    row: int
    col: int
    height: int


S = 0
E = 27

grid: List[List[Square]] = []
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

        grid.append(row)


def find_next_square(s: Square, visited: Set[Square]) -> Set[Square]:
    visited.add(s)
    if s.height == E:
        print(len(visited))
        print("ONE PIECE")
        return visited

    all_sides = []
    # Left
    if s.col > 0:
        sq = grid[s.row][s.col - 1]
        if sq not in visited and 0 <= sq.height - s.height <= 1:
            print("Going Left")
            visited_left = find_next_square(sq, visited)
            if len(visited_left) > 0:
                all_sides.append(visited_left)
    # Right
    if s.col < len(grid[s.row]) - 1:
        sq = grid[s.row][s.col + 1]
        if sq not in visited and 0 <= sq.height - s.height <= 1:
            print("Going Right")
            visited_right = find_next_square(sq, visited)
            if len(visited_right) > 0:
                all_sides.append(visited_right)
    # Top
    if s.row > 0:
        sq = grid[s.row - 1][s.col]
        if sq not in visited and 0 <= sq.height - s.height <= 1:
            print("Going Top")
            visited_top = find_next_square(sq, visited)
            if len(visited_top) > 0:
                all_sides.append(visited_top)
    # Bottom
    if s.row < len(grid) - 1:
        sq = grid[s.row + 1][s.col]
        if sq not in visited and 0 <= sq.height - s.height <= 1:
            print("Going Bottom")
            visited_bottom = find_next_square(sq, visited)
            if len(visited_bottom) > 0:
                all_sides.append(visited_bottom)

    # Pick shortest side
    if all_sides:
        shortest_side = all_sides[0]
        print([len(side) for side in all_sides])
        for side in all_sides:
            if len(side) < len(shortest_side):
                visited = side
        return visited
    else:
        return set()


current_square = grid[starting_coords[0]][starting_coords[1]]
all_visited: Set[Square] = set()
find_next_square(current_square, all_visited)
print(len(all_visited))
