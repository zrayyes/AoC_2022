from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    score = 0
    lose = 0
    draw = 3
    win = 6

    #       X       Y       Z
    #   A   Draw    Win     Lose
    #   B   Lose    Draw    Win
    #   C   Win     Lose    Draw
    hands = [[draw, win, lose], [lose, draw, win], [win, lose, draw]]

    for line in f.read().split("\n"):
        opponent = ord(line[0:1]) - ord("A")
        player = ord(line[2:3]) - ord("X")
        score += hands[opponent][player] + (player + 1)

    print(score)
    assert score == 10595


# 10595
