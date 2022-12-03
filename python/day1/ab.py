from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    elves_food = [
        [int(food) for food in elf.split("\n")]
        for elf in f.read().split("\n\n")
    ]
    food_sum = sorted([sum(food) for food in elves_food], reverse=True)

    print(food_sum[0])
    print(sum(food_sum[:3]))
