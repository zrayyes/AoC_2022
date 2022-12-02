from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    score = 0

    #       X       Y       Z
    #   A   Draw    Win     Lose
    #   B   Lose    Draw    Win
    #   C   Win     Lose    Draw
    hands = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

    for line in f.read().split("\n"):
        opponent = ord(line[0:1]) - ord("A")
        player = ord(line[2:3]) - ord("X")
        score += hands[opponent][player] + (player + 1)

    print(score)
    assert score == 10595


# 10595
