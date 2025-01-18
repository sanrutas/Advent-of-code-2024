# DAY 12 PART 2

input = open("inputs/input_day_12.txt", "r").read().splitlines()

def in_bounds (row, col, map = input):
    if 0 <= row < len(map) and 0 <= col < len(map[0]):
        return True

def explore_area(row, col, area, seen, map=input, offsets=[(1, 0), (0, -1), (-1, 0), (0, 1)]):
    ch = map[row][col]
    seen.add((row, col))
    area += 1
    for ox, oy in offsets:
        new_row, new_col = row + ox, col + oy
        if (new_row, new_col) in seen:
            continue
        if in_bounds(new_row, new_col) and map[new_row][new_col] == ch:
            area, seen = explore_area(new_row, new_col, area, seen)
    return area, seen

# count of region sides == count of region corners
# circle_offsets must be arranged clockwise or counterclockwise
def get_sides(region, circle_offsets = [(1, 1), (1, -1), (-1, -1), (-1, 1)]):
    sides = 0
    for row, col in region:
        for ox, oy in circle_offsets:
            nb_row = (row + ox, col)
            nb_col = (row, col + oy)
            nb_diag = (row + ox, col + oy)
            # if 2 side neighbours are missing, that mean's it's a corner
            if nb_row not in region and nb_col not in region:
                sides += 1
            # if side neighbours are present, bug diagonal neighbour is missing, that also means it's a corner
            elif nb_row in region and nb_col in region and nb_diag not in region:
                sides += 1
    return sides

def get_sum(input):
    seen = set()
    price = 0
    for row, row_list in enumerate(input):
        for col, ch in enumerate(row_list):
            if (row, col) not in seen:
                old_seen = seen.copy()
                area, seen = explore_area(row, col, 0, seen)
                curr_region = seen.difference(old_seen)        
                sides = get_sides(curr_region)
                price += sides * area
    return price

print(get_sum(input))
