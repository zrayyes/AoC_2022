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

    def walk(self) -> List[bool]:
        out = []
        for y in range(self.height):
            for x in range(self.width):
                tree = self.grid[y][x]
                # if tree on edge
                if y == 0 or x == 0 or x == self.height - 1 or y == self.width - 1:
                    out.append(True)
                else:
                    # Left
                    if tree > max(self.grid[y][:x]):
                        out.append(True)
                    # Right
                    elif tree > max(self.grid[y][x + 1 :]):
                        out.append(True)
                    # Top
                    elif tree > max([self.grid[v][x] for v in range(y)]):
                        out.append(True)
                    # Bottom
                    elif tree > max(
                        [self.grid[v][x] for v in range(y + 1, self.height)]
                    ):
                        out.append(True)

        return out

    def walk_again(self) -> List[int]:
        out = []
        for y in range(self.height):
            for x in range(self.width):
                tree = self.grid[y][x]
                # if tree on edge
                if y == 0 or x == 0 or x == self.height - 1 or y == self.width - 1:
                    out.append(0)
                else:
                    counter = 1
                    # Left
                    left_counter = 0
                    for left_tree in reversed(self.grid[y][:x]):
                        left_counter += 1
                        if tree <= left_tree:
                            break
                    counter *= left_counter
                    # Right
                    right_counter = 0
                    for right_tree in self.grid[y][x + 1 :]:
                        right_counter += 1
                        if tree <= right_tree:
                            break
                    counter *= right_counter
                    # Top
                    top_counter = 0
                    for top_tree in reversed([self.grid[v][x] for v in range(y)]):
                        top_counter += 1
                        if tree <= top_tree:
                            break
                    counter *= top_counter
                    # Bottom
                    bot_counter = 0
                    for bot_tree in [
                        self.grid[v][x] for v in range(y + 1, self.height)
                    ]:
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