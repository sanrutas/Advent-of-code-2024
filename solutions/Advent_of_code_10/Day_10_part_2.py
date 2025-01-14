input = open("inputs/input_day_10.txt", "r").read().split()

def in_bounds(row, col):
    if 0 <= row < len(input) and 0 <= col < len(input[0]):
        return True

def count_trails(input, row, col, curr_num=0, offsets = None):
    if offsets is None:
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if curr_num == 9:
        return 1
    trail_count = 0
    for ox, oy in offsets:
        new_row, new_col = row + ox, col + oy
        if in_bounds(new_row, new_col) and int(input[new_row][new_col]) == curr_num + 1:
            trail_count += count_trails(input, new_row, new_col, curr_num + 1)
    return trail_count


def get_sum(input):
    sum = 0
    for row_id, row_num in enumerate(input):
        for col_id, col_num in enumerate(input[row_id]):
            if col_num == '0':
                sum += count_trails(input, row_id, col_id)
    return sum

print(get_sum(input))