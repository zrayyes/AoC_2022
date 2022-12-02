from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    score = 0
    draw = 3
    win = 6
    rock = 1
    paper = 2
    scissor = 3
    rounds = [[letter for letter in line.split(" ")] for line in f.read().split("\n")]

    for (opponent, player) in rounds:
        # Rock
        if opponent == "A":
            # Lose
            if player == "X":
                score += scissor
            # Draw
            elif player == "Y":
                score += rock + draw
            # Win
            elif player == "Z":
                score += paper + win
        # Paper
        elif opponent == "B":
            # Lose
            if player == "X":
                score += rock
            # Draw
            elif player == "Y":
                score += paper + draw
            # Win
            elif player == "Z":
                score += scissor + win
        # Scissor
        elif opponent == "C":
            # Lose
            if player == "X":
                score += paper
            # Draw
            elif player == "Y":
                score += scissor + draw
            # Win
            elif player == "Z":
                score += rock + win

    print(score)


# 9541
