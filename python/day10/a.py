from pathlib import Path

p = Path(__file__).with_name("input.txt")


with p.open() as f:
    lines = f.read().split("\n")
    x = 1
    current_cycle = 1
    sum_of_cycles = 0
    crt = ""
    for line in lines:
        line = line.split(" ")
        command = line[0]
        count = 0
        if len(line) > 1:
            count = int(line[1])

        cycles_needed = 1
        if command == "addx":
            cycles_needed = 2

        for i in range(cycles_needed):
            if (current_cycle - 20) % 40 == 0:
                signal_strength = x * current_cycle
                print(f"Cycle {current_cycle}: {signal_strength}")
                sum_of_cycles += signal_strength

            CRT_pos = (current_cycle - 1) % 40
            if CRT_pos == 0:
                crt += "\n"

            if x - 1 <= CRT_pos <= x + 1:
                crt += "#"
            else:
                crt += " "

            current_cycle += 1

        if command == "addx":
            x += count

    print(f"Total Signal Strength: {sum_of_cycles}")
    print(crt)

# 13520
# PGPHBEAB