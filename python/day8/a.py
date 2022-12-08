from pathlib import Path
from typing import List

p = Path(__file__).with_name("input.txt")


class Grid:
    height: int
    width: int
    grid: List[List[int]]

    def __init__(self, input: List[List[int]]) -> None:
        self.grid = input
        self.height = len(input)
        self.width = len(input[0])

    def get_left_trees(self, y: int, x: int) -> List[int]:
        if x == 0:
            return [-1]
        return list(reversed(self.grid[y][:x]))

    def get_right_trees(self, y: int, x: int) -> List[int]:
        if x == self.width - 1:
            return [-1]
        return self.grid[y][x + 1 :]

    def get_top_trees(self, y: int, x: int) -> List[int]:
        if y == 0:
            return [-1]
        return list(reversed([self.grid[v][x] for v in range(y)]))

    def get_bottom_trees(self, y: int, x: int) -> List[int]:
        if y == self.height - 1:
            return [-1]
        return [self.grid[v][x] for v in range(y + 1, self.height)]

    def walk(self) -> List[bool]:
        out = []
        for y in range(self.height):
            for x in range(self.width):
                tree = self.grid[y][x]
                # Left
                if tree > max(self.get_left_trees(y, x)):
                    out.append(True)
                # Right
                elif tree > max(self.get_right_trees(y, x)):
                    out.append(True)
                # Top
                elif tree > max(self.get_top_trees(y, x)):
                    out.append(True)
                # Bottom
                elif tree > max(self.get_bottom_trees(y, x)):
                    out.append(True)

        return out

    def walk_again(self) -> List[int]:
        out = []
        for y in range(self.height):
            for x in range(self.width):
                tree = self.grid[y][x]
                counter = 1
                # Left
                left_counter = 0
                for left_tree in self.get_left_trees(y, x):
                    left_counter += 1
                    if tree <= left_tree:
                        break
                counter *= left_counter
                # Right
                right_counter = 0
                for right_tree in self.get_right_trees(y, x):
                    right_counter += 1
                    if tree <= right_tree:
                        break
                counter *= right_counter
                # Top
                top_counter = 0
                for top_tree in self.get_top_trees(y, x):
                    top_counter += 1
                    if tree <= top_tree:
                        break
                counter *= top_counter
                # Bottom
                bot_counter = 0
                for bot_tree in self.get_bottom_trees(y, x):
                    bot_counter += 1
                    if tree <= bot_tree:
                        break
                counter *= bot_counter

                out.append(counter)

        return out

    def __str__(self) -> str:
        out = f"Width: {self.width}, Height: {self.height}\n"
        return out


with p.open() as f:
    input = [[int(c) for c in line] for line in f.read().split("\n")]
    grid = Grid(input)
    print(grid)
    visible = grid.walk()
    print(len(visible))
    scenic_score = grid.walk_again()
    print(max(scenic_score))

# 1787
# 440640
