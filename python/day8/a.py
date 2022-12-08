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


    def walk(self):
        scenic_scores = []
        visible_counter = 0
        for y in range(self.height):
            for x in range(self.width):
                tree = self.grid[y][x]
                counter = 1
                # Left
                left_counter = 0
                left_visible = True
                for left_tree in self.get_left_trees(y, x):
                    left_counter += 1
                    if tree <= left_tree:
                        left_visible = False
                        break
                counter *= left_counter
                # Right
                right_counter = 0
                right_visible = True
                for right_tree in self.get_right_trees(y, x):
                    right_counter += 1
                    if tree <= right_tree:
                        right_visible = False
                        break
                counter *= right_counter
                # Top
                top_counter = 0
                top_visible = True
                for top_tree in self.get_top_trees(y, x):
                    top_counter += 1
                    if tree <= top_tree:
                        top_visible = False
                        break
                counter *= top_counter
                # Bottom
                bot_counter = 0
                bot_visible = True
                for bot_tree in self.get_bottom_trees(y, x):
                    bot_counter += 1
                    if tree <= bot_tree:
                        bot_visible = False
                        break
                counter *= bot_counter

                scenic_scores.append(counter)

                if left_visible or right_visible or top_visible or bot_visible:
                    visible_counter += 1
        print(f"Trees Visible: {visible_counter}")
        print(f"Max Scenic Score: {max(scenic_scores)}")

    def __str__(self) -> str:
        out = f"Width: {self.width}, Height: {self.height}\n"
        return out


with p.open() as f:
    input = [[int(c) for c in line] for line in f.read().split("\n")]
    grid = Grid(input)
    print(grid)
    visible = grid.walk()

# 1787
# 440640
