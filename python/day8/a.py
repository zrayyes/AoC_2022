from pathlib import Path
from typing import List, Tuple

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

    def get_all_sides(self, x, y) -> List[List[int]]:
        return [
            self.get_left_trees(x, y),
            self.get_right_trees(x, y),
            self.get_top_trees(x, y),
            self.get_bottom_trees(x, y),
        ]

    def get_scenic_score_and_visibility(
        self, y: int, x: int, trees: List[int]
    ) -> Tuple[int, bool]:
        tree = self.grid[y][x]
        scenic_score = 0
        visible = True
        for left_tree in trees:
            if left_tree == -1:
                break
            scenic_score += 1
            if tree <= left_tree:
                visible = False
                break
        return (scenic_score, visible)

    def walk(self):
        scenic_scores = []
        visible_counter = 0
        for y in range(self.height):
            for x in range(self.width):
                scenic_score = 1
                visible = False

                for side in self.get_all_sides(x, y):
                    side_counter, side_visible = self.get_scenic_score_and_visibility(
                        x, y, side
                    )
                    scenic_score *= side_counter
                    visible = visible or side_visible

                scenic_scores.append(scenic_score)

                if visible:
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
