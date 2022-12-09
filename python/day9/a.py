from dataclasses import dataclass, replace
from pathlib import Path
from typing import List


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int


class Grid:
    height: int
    width: int
    start = Point(0, 0)
    head = Point(0, 0)
    tail = Point(0, 0)
    visited: set[Point] = set()

    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        self.width = width
        self.height = height
        self.visited.add(self.start)

    def __str__(self) -> str:
        out = ""
        for y in reversed(range(self.height)):
            for x in range(self.width):
                p = Point(x, y)
                if self.head == p:
                    out += "H"
                elif self.tail == p:
                    out += "T"
                elif self.start == p:
                    out += "s"
                elif p in self.visited:
                    out += "#"
                else:
                    out += "."
            out += "\n"
        return out

    @property
    def is_tail_touching_head(self) -> bool:
        return (
            abs(self.head.x - self.tail.x) <= 1 and abs(self.head.y - self.tail.y) <= 1
        )

    def move(self, direction: str):
        if direction == "R":
            self.head = replace(self.head, x=self.head.x + 1)
        elif direction == "L":
            self.head = replace(self.head, x=self.head.x - 1)
        elif direction == "U":
            self.head = replace(self.head, y=self.head.y + 1)
        elif direction == "D":
            self.head = replace(self.head, y=self.head.y - 1)

    def move_tail(self):
        if self.is_tail_touching_head:
            return

        x_diff = self.head.x - self.tail.x
        y_diff = self.head.y - self.tail.y
        new_location = self.tail

        if x_diff > 1:
            new_location = Point(x=self.tail.x + 1, y=self.head.y)
        elif x_diff < -1:
            new_location = Point(x=self.tail.x - 1, y=self.head.y)
        elif y_diff > 1:
            new_location = Point(y=self.tail.y + 1, x=self.head.x)
        elif y_diff < -1:
            new_location = Point(y=self.tail.y - 1, x=self.head.x)

        self.tail = new_location
        self.visited.add(new_location)


p = Path(__file__).with_name("input.txt")

with p.open() as f:
    grid = Grid(100, 100)
    for line in f.read().split("\n"):
        direction, times = line.split(" ")
        times = int(times)
        print(f"== {direction} {times} ==")
        for t in range(times):
            grid.move(direction)
            grid.move_tail()
    
    print(grid)
    print(len(grid.visited))
