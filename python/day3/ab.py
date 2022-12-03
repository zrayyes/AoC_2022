from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    all_backpacks = [
        [ord(item) - 96 if ord(item) >= 96 else ord(item) - 38 for item in list(line)]
        for line in f.read().split("\n")
    ]

    score_A = 0

    for backpack in all_backpacks:
        first_half = backpack[: len(backpack) // 2]
        second_half = backpack[len(backpack) // 2 :]
        score_A += sum(set(first_half).intersection(second_half))

    score_B = 0

    for i in range(0, len(all_backpacks), 3):
        first = all_backpacks[i]
        second = all_backpacks[i + 1]
        third = all_backpacks[i + 2]
        score_B += sum(set(first).intersection(set(second).intersection(third)))

    print(score_A)
    assert score_A == 8233

    print(score_B)
    assert score_B == 2821
