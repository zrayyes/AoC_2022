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
    knots: List[Point] = []
    visited: set[Point] = set()

    def __init__(self, width: int, height: int, knots: int) -> None:
        self.width = width
        self.height = height
        self.visited.add(self.start)

        # 2 knots = head + 1 knot
        for i in range(knots - 1):
            self.knots.append(Point(0, 0))

    def __str__(self) -> str:
        out = ""
        for y in reversed(range(self.height)):
            for x in range(self.width):
                p = Point(x, y)
                if self.head == p:
                    out += "H"
                elif p in self.knots:
                    out += str(self.knots.index(p))
                elif self.start == p:
                    out += "s"
                elif p in self.visited:
                    out += "#"
                else:
                    out += "."
            out += "\n"
        return out

    def is_tail_touching_head(self, head: Point, tail: Point) -> bool:
        return abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1

    def move(self, direction: str):
        if direction == "R":
            self.head = replace(self.head, x=self.head.x + 1)
        elif direction == "L":
            self.head = replace(self.head, x=self.head.x - 1)
        elif direction == "U":
            self.head = replace(self.head, y=self.head.y + 1)
        elif direction == "D":
            self.head = replace(self.head, y=self.head.y - 1)

    def move_tail(self, head: Point, tail: Point) -> Point:
        new_location = tail

        if self.is_tail_touching_head(head, tail):
            return new_location

        x_diff = head.x - tail.x
        y_diff = head.y - tail.y

        if x_diff > 1:
            new_location = Point(x=tail.x + 1, y=head.y)
        elif x_diff < -1:
            new_location = Point(x=tail.x - 1, y=head.y)
        elif y_diff > 1:
            new_location = Point(y=tail.y + 1, x=head.x)
        elif y_diff < -1:
            new_location = Point(y=tail.y - 1, x=head.x)

        return new_location

    def move_all_knots(self):
        for i, knots in enumerate(self.knots):
            head = self.head
            if i > 1:
                head = self.knots[i - 1]
            tail = knots
            new_location = self.move_tail(head, tail)
            self.knots[i] = new_location
            self.visited.add(new_location)


p = Path(__file__).with_name("input.txt")

with p.open() as f:
    grid = Grid(10, 10, 2)
    for line in f.read().split("\n"):
        direction, times = line.split(" ")
        times = int(times)
        print(f"== {direction} {times} ==")
        for t in range(times):
            grid.move(direction)
            grid.move_all_knots()

    print(grid)
    print(len(grid.visited))
