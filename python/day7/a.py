from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import List, Optional


class Node:
    name: str
    _size: int
    is_dir: bool
    parent_node: Optional["Node"]
    children: List["Node"]
    depth: int

    def __init__(
        self,
        name: str,
        is_dir: bool,
        size: int = 0,
        parent_node: Optional["Node"] = None,
        children: List["Node"] = [],
    ) -> None:

        self.name = name
        self.is_dir = is_dir
        self._size = size
        self.parent_node = parent_node
        self.children = children

        if parent_node is None:
            self.depth = 0
        else:
            self.depth = parent_node.depth + 1

    @property
    def size(self):
        if self.is_dir:
            return sum([n.size for n in self.children])
        return self._size

    def __str__(self) -> str:
        prefix = "  " * self.depth
        emoji = "📂" if self.is_dir else "📄"
        node_type = "dir" if self.is_dir else "file"
        out = f"{prefix}- {emoji} {self.name} ({node_type}, {self.size})"
        for child in self.children:
            out = out + "\n"
            out = out + str(child)

        return out

    def get_all_child_nodes(self) -> List["Node"]:
        if not self.is_dir:
            return [self]

        out = []
        for c in self.children:
            out = out + [c] + c.get_all_child_nodes()

        return out


max_length = int(sys.argv[1]) if len(sys.argv) > 1 else 100000

p = Path(__file__).with_name("input.txt")
root_node = Node("/", True, 0, None, [])

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
                    current_node = (
                        current_node.parent_node
                        if current_node.parent_node
                        else root_node
                    )
                else:
                    existing_node = [
                        n for n in current_node.children if n.name == dir_name
                    ]
                    # check if node exists
                    if existing_node is not None:
                        current_node = existing_node[0]
                    # if not create
                    else:
                        new_node = Node(dir_name, True, 0, current_node, [])
                        current_node.children.append(new_node)
                        current_node = new_node
        else:
            # Files
            info, file_name = line.split(" ")
            size = 0
            is_dir = True
            if info != "dir":
                size = int(info)
                is_dir = False
            new_node = Node(file_name, is_dir, size, current_node, [])
            current_node.children.append(new_node)

total_size = root_node.size
free_space_left = 70000000 - root_node.size
space_needed = 30000000 - free_space_left

nodes_with_max_length = [
    n.size for n in root_node.get_all_child_nodes() if n.is_dir and n.size < max_length
]

smallest_deletable = sorted(
    [n for n in root_node.get_all_child_nodes() if n.is_dir and n.size > space_needed],
    key=lambda x: x.size,
)[0]

print(root_node)
print()
print(f"Total size: {root_node.size}")
print(f"Free size: {free_space_left}")
print(f"Space needed: {space_needed}")
print()
print(f"Sum of dirs smaller than {max_length}: {sum(nodes_with_max_length)}")
print(f"Size of smallest directory to delete: {smallest_deletable.size}")


# 1118405
# 12545514
