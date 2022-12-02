from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    score_A = 0
    score_B = 0

    for line in f.read().split("\n"):
        opponent = ord(line[0:1]) - ord("A")
        player = ord(line[2:3]) - ord("X")
        score_A += 1 + player + 3 * ((2 * opponent + player + 1) % 3)
        score_B += 1 + player * 3 + (3 + opponent + player - 1) % 3

    print(score_A)
    print(score_B)
    assert score_A == 10595
    assert score_B == 9541
