from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    pairs = [
        [[int(number) for number in pair.split("-")] for pair in line.split(",")]
        for line in f.read().split("\n")
    ]

    counter = 0
    for a, b in pairs:
        if ((a[0] <= b[0]) and (a[1] >= b[1])) or ((b[0] <= a[0]) and (b[1] >= a[1])):
            counter += 1

    print(counter)
