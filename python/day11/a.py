from dataclasses import dataclass
import math
from pathlib import Path
from typing import List


@dataclass
class Monkey:
    number: int
    items: List[int]
    operation: str
    test: str
    test_true: str
    test_false: str
    items_inspected = 0


class Tree:
    monkeys: List[Monkey] = []
    round_number = 0

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        out = ""
        for monkey in self.monkeys:
            out += f"Monkey {monkey.number}: {monkey.items}. inspected items {monkey.items_inspected} times.\n"
        out += f"Rounds: {self.round_number}\n"
        return out

    def add_monkey(self, monkey: Monkey):
        self.monkeys.append(monkey)

    def get_monkey_index_by_number(self, monkey_number: int) -> int:
        return [
            i for i, monkey in enumerate(self.monkeys) if monkey.number == monkey_number
        ][0]

    def throw_to_monkey(self, monkey_number: int, item: int):
        monkey_index = self.get_monkey_index_by_number(monkey_number)
        self.monkeys[monkey_index].items.append(item)

    def get_monkey_business(self) -> int:
        return math.prod(
            sorted([monkey.items_inspected for monkey in self.monkeys], reverse=True)[
                :2
            ]
        )

    def start_round(self):
        for monkey in self.monkeys:
            while monkey.items:
                # Inspect
                old = monkey.items.pop(0)
                new_item = eval(monkey.operation)
                new_item = new_item // 3
                monkey.items_inspected += 1

                # Test
                test = monkey.test[13:]
                # Divisible by ...
                if new_item % int(test) == 0:
                    new_monkey = int(monkey.test_true[16:])
                    self.throw_to_monkey(new_monkey, new_item)
                else:
                    new_monkey = int(monkey.test_false[16:])
                    self.throw_to_monkey(new_monkey, new_item)

        self.round_number += 1


tree = Tree()

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
        number = int(lines[0][7])
        starting_items = list(map(lambda x: int(x), lines[1][18:].split(", ")))
        operation = lines[2][19:]
        test = lines[3][8:]
        test_true = lines[4][13:]
        test_false = lines[5][14:]

        monkey = Monkey(number, starting_items, operation, test, test_true, test_false)
        tree.add_monkey(monkey)

print(tree)
for i in range(20):
    tree.start_round()
print(tree)
print(tree.get_monkey_business())
