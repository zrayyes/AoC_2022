from collections import defaultdict
from pathlib import Path

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

    for move in moves:
        move_count, move_from, move_to = move
        for i in range(move_count):
            crates[move_to - 1] = [crates[move_from - 1].pop(0)] + crates[move_to - 1]

    print("".join([crates[k].pop(0) for k in range(len(crates))]))
