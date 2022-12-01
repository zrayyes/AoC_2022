from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    elves = [0]
    current_elf = 0
    while True:
        line = f.readline()
        if not line:
            break
        food = line.strip()

        if food:
            elves[current_elf] += int(food)
        else:
            current_elf += 1
            elves.append(0)

    print(max(elves))
