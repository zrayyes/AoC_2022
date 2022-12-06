from pathlib import Path
import sys


marker_length = int(sys.argv[1]) if len(sys.argv) > 1 else 4

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    line = f.read()
    for i, c in enumerate(line):
        if i >= len(line) - (marker_length - 1):
            break
        else:
            window = line[i : i + marker_length]
            if len(window) == len(set(window)):
                print(i + marker_length)
                exit(0)

# 1034
# 2472
