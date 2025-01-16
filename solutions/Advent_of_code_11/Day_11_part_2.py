# DAY 11 PART 2
from collections import defaultdict
import math
input = open("inputs/input_day_11.txt", "r").read().strip()

def blinker(stones, blinks):
    def merge_dicts(dict1, dict2):
        for key, count in dict2.items():
            if key in dict1:
                dict1[key] += count
            else:
                dict1[key] = count

            if dict1[key] == 0:
                del dict1[key]
        
        return dict1
    
    stone_counts = defaultdict(int)
    for st in stones:
        stone_counts[st] += 1

    for bl in range(blinks):
        add_stones = defaultdict(int)
        for num, count in stone_counts.items():
            if num == 0:
                add_stones[1] += count
                add_stones[0] -= count
                continue
            
            digits = math.floor(math.log10(abs(num))) + 1
            if digits % 2 == 0:
                first_half = int(num / pow(10, digits/2))
                second_half = int(num % pow(10, digits/2))
                add_stones[first_half] += count 
                add_stones[second_half] += count
                add_stones[num] -= count 
                continue
            
            add_stones[num * 2024] += count
            add_stones[num] -= count 
        stone_counts = merge_dicts(stone_counts, add_stones)
    return stone_counts

stones = [int(num) for num in input.split(' ')]
blinks = 75
out = blinker(stones, blinks)

print(sum(out.values()))