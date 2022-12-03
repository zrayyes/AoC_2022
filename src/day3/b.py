from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    score = 0

    all_backpacks = []

    for line in f.read().split("\n"):
        backpack = []
        for elf in list(line):
            if ord(elf) >= ord("a"):
                backpack.append(ord(elf) - ord("a") + 1)
            else:
                backpack.append(ord(elf) - ord("A") + 27)
        all_backpacks.append(backpack)

    for i in range(0, len(all_backpacks), 3):
        first = all_backpacks[i]
        second = all_backpacks[i + 1]
        third = all_backpacks[i + 2]
        score += sum(set(first).intersection(set(second).intersection(third)))

    print(score)

# 2821
