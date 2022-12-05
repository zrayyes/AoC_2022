from collections import defaultdict
from pathlib import Path
import copy

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    crates = defaultdict(list)
    moves = []

    for line in f.read().split("\n"):
        if line == "":
            continue
        elif "move" in line:
            line = line.split(" ")
            moves.append([int(line[1]), int(line[3]), int(line[5])])
        elif "[" in line:
            for crate_index in [i + 1 for i, x in enumerate(line) if x == "["]:
                column_index = crate_index // 4
                crates[column_index].append(line[crate_index])

    crates_A = copy.deepcopy(crates)
    crates_B = copy.deepcopy(crates)

    for move in moves:
        move_count, move_from, move_to = move
        move_to -= 1
        move_from -= 1
        temp = []
        for i in range(move_count):
            crates_A[move_to] = [crates_A[move_from].pop(0)] + crates_A[move_to]
            temp.append(crates_B[move_from].pop(0))
        for i in range(len(temp)):
            crates_B[move_to] = [temp.pop()] + crates_B[move_to]

    print("".join([crates_A[k].pop(0) for k in range(len(crates_A))]))
    print("".join([crates_B[k].pop(0) for k in range(len(crates_B))]))


# BZLVHBWQF
# TDGJQTZSL
