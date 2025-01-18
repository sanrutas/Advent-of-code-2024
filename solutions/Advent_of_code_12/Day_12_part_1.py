# DAY 12 PART 1

input = open("inputs/input_day_12.txt", "r").read().splitlines()

def in_bounds (row, col, map = input):
    if 0 <= row < len(map) and 0 <= col < len(map[0]):
        return True

def fence_counter(row, col, map = input, offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]):
    ch = map[row][col]
    fences = 4
    for ox, oy in offsets:
        new_row, new_col = row + ox, col + oy
        if in_bounds(new_row, new_col) and input[new_row][new_col] == ch:
            fences -= 1
    return fences

def explore_area(row, col, area, perim, seen, map=input, offsets=[(1, 0), (-1, 0), (0, 1), (0, -1)]):
    ch = map[row][col]
    seen.add((row, col))
    perim += fence_counter(row, col)
    area += 1
    for ox, oy in offsets:
        new_row, new_col = row + ox, col + oy
        if (new_row, new_col) in seen:
            continue
        if in_bounds(new_row, new_col) and map[new_row][new_col] == ch:
            area, perim = explore_area(new_row, new_col, area, perim, seen)
    return area, perim

def get_sum(input):
    seen = set()
    price = 0
    for row, row_list in enumerate(input):
        for col, ch in enumerate(row_list):
            if (row, col) not in seen:
                area, perim = explore_area(row, col, 0, 0, seen)
                price += area * perim
    return price

print(get_sum(input))
