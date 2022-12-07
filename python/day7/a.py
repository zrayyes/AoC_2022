from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


class Node:
    name: str
    parent_node: Optional["Node"]
    children: List["Node"]
    depth: int

    def __init__(
        self,
        name: str,
        parent_node: Optional["Node"] = None,
        children: List["Node"] = [],
    ) -> None:

        self.name = name
        self.parent_node = parent_node
        self.children = children

        if parent_node is None:
            self.depth = 0
        else:
            self.depth = parent_node.depth + 1

    def __str__(self) -> str:
        prefix = "---" * self.depth
        out = prefix + " " + self.name
        for child in self.children:
            out = out + "\n"
            out = out + prefix + str(child)

        return out


p = Path(__file__).with_name("input.txt")
root_node = Node("/", None, [])

with p.open() as f:
    current_node = root_node
    for line in f.read().split("\n"):
        if line == "$ cd /":
            current_node = root_node
            continue
        if line.startswith("$"):
            # Commands
            line = line[2:]
            if line.startswith("cd"):
                dir_name = line[3:]
                if dir_name == "..":
                    current_node = current_node.parent_node
                else:
                    existing_node = [
                        n for n in current_node.children if n.name == dir_name
                    ]
                    # check if node exists
                    if existing_node is not None:
                        current_node = existing_node[0]
                    # if not create
                    else:
                        new_node = Node(dir_name, current_node, [])
                        current_node.children.append(new_node)
                        current_node = new_node
        else:
            # Files
            line = line.split(" ")
            new_node = Node(line[1], current_node, [])
            current_node.children.append(new_node)

print(root_node)
