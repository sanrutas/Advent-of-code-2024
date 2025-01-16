# DAY 11 PART 1
# Intuitive but inefficient, part 2 asked to do the same but forced to rethink efficiency 
import math
input = open("inputs/input_day_11.txt", "r").read().strip()

def blinker(stones, blinks):
    for blink in range(blinks):
        new_stones = []
        for st in stones:
            if st == 0:
                new_stones.append(1)
                continue
            digits = math.floor(math.log10(abs(st))) + 1
            if digits % 2 == 0:
                new_stones.append(int(st / pow(10, digits/2)))
                new_stones.append(int(st % pow(10, digits/2)))
                continue
            new_stones.append(st * 2024)
        stones = new_stones
    return stones

stones = [int(num) for num in input.split(' ')]
blinks  = 25
new_stones = blinker(stones, blinks)

print(len(new_stones))
