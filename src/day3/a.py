from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    score = 0
    for line in f.read().split("\n"):
        items = []
        for item in list(line):
            if ord(item) >= ord("a"):
                items.append(ord(item) - ord("a") + 1)
            else:
                items.append(ord(item) - ord("A") + 27)

        first_half = items[: len(items) // 2]
        second_half = items[len(items) // 2 :]
        score += sum(set(first_half).intersection(second_half))

    print(score)

# 8233