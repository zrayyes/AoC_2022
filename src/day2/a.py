from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    score = 0
    draw = 3
    win = 6
    rounds = [[letter for letter in line.split(" ")] for line in f.read().split("\n")]

    for (opponent, player) in rounds:
        # Rock
        if opponent == "A":
            # Rock
            if player == "X":
                score += draw
            # Paper
            elif player == "Y":
                score += win
            # Scissor
            elif player == "Z":
                pass
        # Paper
        elif opponent == "B":
            # Rock
            if player == "X":
                pass
            # Paper
            elif player == "Y":
                score += draw
            # Scissor
            elif player == "Z":
                score += win
        # Scissor
        elif opponent == "C":
            # Rock
            if player == "X":
                score += win
            # Paper
            elif player == "Y":
                pass
            # Scissor
            elif player == "Z":
                score += draw

        # Extra
        if player == "X":
            score += 1
        if player == "Y":
            score += 2
        if player == "Z":
            score += 3

    print(score)


# 10595
