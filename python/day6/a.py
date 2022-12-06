from pathlib import Path
import sys
from typing import Tuple


marker_length = int(sys.argv[1]) if len(sys.argv) > 1 else 4


def find_duplicate(l: list) -> Tuple[bool, int]:
    for i, e in enumerate(l):
        if e in l[i + 1 :]:
            return (True, i)
    return (False, 0)


p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    line = f.read()
    index = 0
    while index < len(line):
        if index >= len(line) - (marker_length - 1):
            break
        else:
            window = line[index : index + marker_length]
            duplicate_exists, duplicate_index = find_duplicate(window)
            if not duplicate_exists:
                print(index + marker_length)
                break
            index += duplicate_index + 1

# 1034
# 2472
