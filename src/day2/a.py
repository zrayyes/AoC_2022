from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lose = 0
    draw = 3
    win = 6

    rounds = [
        [
            ord(letter) - ord("A") + 1
            if ord(letter) <= ord("C")
            else ord(letter) - ord("X") + 1
            for letter in line.split(" ")
        ]
        for line in f.read().split("\n")
    ]

    #               X       Y       Z
    #   A           Draw    Win     Lose
    #   B           Lose    Draw    Win
    #   C           Win     Lose    Draw
    hands = [[draw, win, lose], [lose, draw, win], [win, lose, draw]]

    score = sum(
        [hands[opponent - 1][player - 1] + player for (opponent, player) in rounds]
    )

    print(score)
    assert score == 10595


# 10595
