import copy
from dataclasses import dataclass
import math
from pathlib import Path
from typing import List


@dataclass
class Monkey:
    items: List[int]
    operation: str
    test: int
    test_true: int
    test_false: int
    items_inspected = 0


class Tree:
    def __init__(self) -> None:
        self.monkeys: List[Monkey] = []
        self.round_number = 0
        self.devisor = 1

    def __str__(self) -> str:
        out = ""
        for i, monkey in enumerate(self.monkeys):
            out += f"Monkey {i}: {monkey.items}. Inspected items {monkey.items_inspected} times.\n"
        out += f"Rounds: {self.round_number}\n"
        return out

    def add_monkey(self, monkey: Monkey):
        self.monkeys.append(monkey)
        self.devisor *= monkey.test

    def throw_to_monkey(self, monkey_number: int, item: int):
        self.monkeys[monkey_number].items.append(item)

    def get_monkey_business(self) -> int:
        return math.prod(
            sorted([monkey.items_inspected for monkey in self.monkeys], reverse=True)[
                :2
            ]
        )

    def start_round(self, no_worries=True):
        for monkey in self.monkeys:
            while monkey.items:
                # Inspect
                old = monkey.items.pop(0)
                new_item = eval(monkey.operation)

                if no_worries:
                    new_item = new_item // 3
                else:
                    new_item = new_item % self.devisor

                # Test
                if new_item % monkey.test == 0:
                    self.throw_to_monkey(monkey.test_true, new_item)
                else:
                    self.throw_to_monkey(monkey.test_false, new_item)

                monkey.items_inspected += 1
        self.round_number += 1


tree_1 = Tree()

p = Path(__file__).with_name("input.txt")
with p.open() as f:
    for monkey in f.read().split("\n\n"):
        number = 0
        starting_items = []
        operation = ""
        test = ""
        test_true = ""
        test_false = ""

        lines = monkey.split("\n")
        starting_items = list(map(lambda x: int(x), lines[1][18:].split(", ")))
        operation = lines[2][19:]
        test = int(lines[3][21:])
        test_true = int(lines[4][29:])
        test_false = int(lines[5][30:])

        tree_1.add_monkey(
            Monkey(starting_items, operation, test, test_true, test_false)
        )

tree_2 = copy.deepcopy(tree_1)

# Part 1
for i in range(20):
    tree_1.start_round()
print(tree_1)
print(tree_1.get_monkey_business())
# 111210

# Part 2
for i in range(10000):
    tree_2.start_round(no_worries=False)
print(tree_2)
print(tree_2.get_monkey_business())

# 15447387620