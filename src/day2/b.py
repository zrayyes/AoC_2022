from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    score = 0

    #       X       Y       Z
    #   A   Scissor Rock    Paper
    #   B   Rock    Paper   Scissor
    #   C   Paper   Scissor Rock
    hands = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]

    for line in f.read().split("\n"):
        opponent = ord(line[0:1]) - ord("A")
        outcome = ord(line[2:3]) - ord("X")
        score += hands[opponent][outcome] + (outcome) * 3

    print(score)
    assert score == 9541


# 9541
