from itertools import combinations
from collections import defaultdict

input = open("inputs/input_day_8.txt", "r").read().splitlines()

def new_coords(point1, point2):
    r1, c1 = point1[0], point1[1]
    r2, c2 = point2[0], point2[1]
    dr = r2 - r1
    dc = c2 - c1
    valid_points = set()
    
    for i in range(len(input)):
        new_p1 = (r1 - dr * i, c1 - dc * i)
        if 0 <= new_p1[0] < len(input) and 0 <= new_p1[1] < len(input[0]):
            valid_points.add(new_p1)
        else:
            break
        
    for i in range(len(input)):
        new_p2 = (r2 + dr * i, c2 + dc * i)
        if 0 <= new_p2[0] < len(input) and 0 <= new_p2[1] < len(input[0]):
            valid_points.add(new_p2)    
        else:
            break
    return valid_points

positions = defaultdict(list)
for r, row in enumerate(input):
    for c, val in enumerate(row):
        if val != '.':
            positions[val].append((r, c))
            
hashpos = set()
for letter, coords in positions.items():
    for (point1), (point2) in combinations(coords, 2):
        items = (new_coords((point1), (point2)))
        hashpos.update(items)

print(len(hashpos))