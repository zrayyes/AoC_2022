from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    line = f.read()
    for i, c in enumerate(line):
        if i >= len(line) - 3:
            break
        else:
            window = [line[i],line[i+1],line[i+2],line[i+3]]
            if len(window) == len(set(window)):
                print(i+4)
                exit(0)

# 1034